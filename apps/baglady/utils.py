# For decoding json
from django.utils import simplejson


class Utils:
    """
    A class with some helpful methods.

    """

    @staticmethod
    def get_value(request, property):
        """
        Find the value of the requested `property`,
        be it json, a GET param, or a POST var.

        """

        # If there's a body, try to get json values from it.
        if hasattr(request, 'body'):
            try:
                json = simplejson.loads(request.body)
            except:
                value = None
            else:
                return json[property]

        # Now let's look for POST vars.
        if property in request.POST:
            return request.POST[property]

        # Finally, let's look for a GET param.
        if property in request.GET:
            return request.GET[property]

        # At this point, we've found nothing.
        return None


