# We'll use Django's built-in admin app.
from django.contrib import admin

# We'll need our Brain models too.
from apps.brain import models


class AbstractBrainAdmin(admin.ModelAdmin):
    """
    A class that provides some basic functionality
    for other admin classes.
    """

    # Hide the owner. This is assigned automatically.
    exclude = ['owner',]

    def save_model(self, request, obj, form, change):
        """
        This method is called whenever a user clicks "Save" in the admin.

        """

        # Set the owner to the user saving this.
        obj.owner = request.user

        # Now we can save.
        super(AbstractBrainAdmin, self).save_model(request, obj, form, change)

    def queryset(self, request):
        """
        Defines the set of items available to the admin interface.

        """

        # Get the full set.
        full_set = super(AbstractBrainAdmin, self).queryset(request)

        # The superuser can see everything.
        if request.user.is_superuser:
            return full_set

        # Filter it down to the owner's items.
        return full_set.filter(owner=request.user)

def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        This method defines the items available to 
        a foreign key field in the admin.

        """

        # The superuser can see everything.
        if request.user.is_superuser:
            parent = super(AbstractBrainAdmin, self)
            return parent.formfield_for_foreignkey(db_field, request, **kwargs)

        # Otherwise, the user can only see their own items.
        else:

            # Is there a model that matches the name of this db field?
            # If so, use that model for our queryset.
            # (We'll ignore db fields that aren't pointing to a model).
            if hasattr(models.__dict__, db_field.name.title()):
                model = models.__dict__[db_field.name.title()]
                kwargs['queryset'] = model.objects.filter(owner=request.user)

            return db_field.formfield(**kwargs)


class NetworkAdmin(AbstractBrainAdmin):
    """
    This class handles the admin interface for Networks.

    """

    # Which fields should be displayed when viewing a list of networks?
    list_display = ['name', 'description']

# Register Networks with the admin.
admin.site.register(models.Network, NetworkAdmin)


class LayerAdmin(AbstractBrainAdmin):
    """
    This class handles the admin interface for Layers.

    """

    # Which fields should be displayed when viewing a list of layers?
    list_display = ['name', 'description', 'level', 'network']

# Register Layers with the admin.
admin.site.register(models.Layer, LayerAdmin)


class PoolAdmin(AbstractBrainAdmin):
    """
    This class handles the admin interface for Pools.

    """

    # Which fields should be displayed when viewing a list of pools?
    list_display = ['name', 'description', 'layer']

# Register Pools with the admin.
admin.site.register(models.Pool, PoolAdmin)


class NeuronAdmin(AbstractBrainAdmin):
    """
    This class handles the admin interface for Neurons.

    """

    # Which fields should be displayed when viewing a list of neurons?
    list_display = ['name', 'description', 'pool', 'bias']

# Register Neurons with the admin.
admin.site.register(models.Neuron, NeuronAdmin)


class LinkAdmin(AbstractBrainAdmin):
    """
    This class handles the admin interface for Links.

    """

    # Which fields should be displayed when viewing a list of links?
    list_display = ['weight', 'linked_from', 'linked_to']

# Register links with the admin.
admin.site.register(models.Link, LinkAdmin)
