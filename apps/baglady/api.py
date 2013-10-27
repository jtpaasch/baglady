# We'll extend Tastypie's model resource.
from tastypie.resources import ModelResource

# We'll need our own models too.
from apps.baglady.models import Bag, Category, Scribble

# Use Tastypie's fields module for foreign keys.
from tastypie import fields

# We'll use tastypie's authorization class.
from tastypie.authorization import Authorization

# We'll use our own utils class.
from apps.baglady.utils import Utils

# We'll use Tastypie's HTTP methods and exceptions.                             
from tastypie import http
from tastypie.exceptions import ImmediateHttpResponse


class AbstractBagladyModelResource(ModelResource):
    """
    Provides some basic functionality for API resources.

    """

    def obj_create(self, bundle, **kwargs):
        """
        This method is called when the API tries to create a resource.

        """

        # What is the public key?
        public_key = Utils.get_value(bundle.request, 'public_key')

        # If no public key, we should exit with a 401.
        if public_key is None:
            raise ImmediateHttpResponse(response=http.HttpUnauthorized())

        # Otherwise, get the bag associated with the public key.
        bag = Bag.objects.get(public_key=public_key)

        # Get the owner of this bag.
        owner = bag.owner

        # Now we can create the object.
        return super(AbstractBagladyModelResource, self).obj_create(bundle, bag=bag, owner=owner)


class BagResource(AbstractBagladyModelResource):
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
        authorization = Authorization()


class CategoryResource(AbstractBagladyModelResource):
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

        # Which class should handle authorization
        authorization = Authorization()


class ScribbleResource(AbstractBagladyModelResource):
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

        # Which class should handle authorization?
        authorization = Authorization()
