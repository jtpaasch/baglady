# Use django's built-in admin app.
from django.contrib import admin

# We also need our models.
from apps.baglady import models


class AbstractBagladyAdminModel(admin.ModelAdmin):
    """
    This class provides some generic functionality for all admin models.

    """

    def queryset(self, request):
        """
        This method defines the set of items the admin displays.

        """

        # Get the full set of items.
        parent = super(AbstractBagladyAdminModel, self)
        full_set = parent.queryset(request)

        # If the requesting user is the admin, return all bags.
        if request.user.is_superuser:
            return full_set

        # Otherwise, filter it down to just the requesting user's bags.
        else:
            return full_set.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        """
        This method is called whenever anyone clicks 'Save' in the admin.

        """

        # If the user is anyone but the admin, set them as the owner.
        if not request.user.is_superuser:
            obj.owner = request.user

        # Now let the parent/super class save it.
        parent = super(AbstractBagladyAdminModel, self)
        parent.save_model(request, obj, form, change)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        This method defines the set of foreign key items the admin displays.

        """

        # The superuser can see everything.
        if request.user.is_superuser:
            parent = super(AbstractBagladyAdminModel, self)
            return parent.formfield_for_foreignkey(db_field, request, *kwargs)

        # Otherwise, the user can only see their own items.
        else:
            model = models.__dict__[db_field.name.title()]
            kwargs['queryset'] = model.objects.filter(owner=request.user)
            return db_field.formfield(**kwargs)


class BagAdmin(AbstractBagladyAdminModel):
    """
    This class handles the admin for the `Bag` model.

    """

    # Which fields should we show in the list display?
    list_display = ['name', 'description', 'owner']

    # Which fields should we hide in the detail view? 
    exclude = ['owner']


# Register Bags with the admin.
admin.site.register(models.Bag, BagAdmin)


class CategoryAdmin(AbstractBagladyAdminModel):
    """
    This class handles the admin for the `Category` model.

    """

    # Which fields should we show in the list display?
    list_display = ['name', 'description', 'owner', 'bag']

    # Which fields should we hide in the detail view?
    exclude = ['owner']


# Register Categories with the admin.
admin.site.register(models.Category, CategoryAdmin)


class ScribbleAdmin(AbstractBagladyAdminModel):
    """
    This class handles the admin for the `Scribble` model.

    """

    # Which fields should we show in the list display?
    list_display = [
        'content', 
        'category', 
        'time_sent', 
        'group_key', 
        'session_key'
    ]

    # Which fields should we hide in the detail view?
    exclude = ['owner']

    # Which fields can't be editide?
    readonly_fields = ['time_received']


# Register Scribbles with the admin.
admin.site.register(models.Scribble, ScribbleAdmin)
