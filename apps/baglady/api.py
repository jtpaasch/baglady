# We'll extend Tastypie's model resource.
from tastypie.resources import ModelResource

# We'll need our own models too.
from apps.baglady.models import Bag, Category, Scribble

# Use Tastypie's fields module for foreign keys.
from tastypie import fields

# We'll use Tastypie's basic auth for authentication.
from tastypie.authentication import BasicAuthentication

# We'll use our own Authorization class for authorization.
from apps.baglady.authorization import CustomAuthorization

# We'll use our own utils class.
from apps.baglady.utils import Utils


class AbstractModelResource(ModelResource):
    """
    The `AbstractModelResource` class provides generic
    functionality for sub resources.

    """

    def obj_create(self, bundle, **kwargs):
        """
        Sets the owner as the requesting user.

        """
        owner = bundle.request.user
        parent = super(AbstractModelResource, self)
        return parent.obj_create(bundle, owner=owner)


class BagResource(AbstractModelResource):
    """
    The `BagResource` class handles the API for Bags.

    """

    class Meta:
        """
        Details about this resource.

        """

        # Which objects should we serve up to the API?
        queryset = Bag.objects.all()

        # Which class should handle authentication?
        authentication = BasicAuthentication()

        # Which class should handle authorization?
        authorization = CustomAuthorization()


class CategoryResource(AbstractModelResource):
    """
    The `CategoryResource` class handles the API for Categories.

    """

    # Add a 'bag' property to this resource.
    bag = fields.ForeignKey(BagResource, 'bag')

    class Meta:
        """
        Details about this resource.

        """

        # Which objects should we serve up to the API?
        queryset = Category.objects.all()

        # Which class should handle authentication?
        authentication = BasicAuthentication()

        # Which class should handle authorization?
        authorization = CustomAuthorization()


class ScribbleResource(AbstractModelResource):
    """
    The `ScribbleResource` class handles the API for Scribbles.

    """

    # Add a 'category' property to this resource.
    category = fields.ForeignKey(CategoryResource, 'category')

    class Meta:
        """
        Details about this resource.

        """

        # Which objects should we serve up to the API?
        queryset = Scribble.objects.all()

        # Which class should handle authentication?
        authentication = BasicAuthentication()

        # Which class should handle authorization?
        authorization = CustomAuthorization()
