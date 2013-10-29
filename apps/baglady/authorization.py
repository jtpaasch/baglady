# We'll extend Tastypie's base Authorization class.
from tastypie.authorization import Authorization


class CustomAuthorization(Authorization):
    """
    The `CustomAuthorization` class only allows access 
    to objects owned by the requesting user.

    """

    def read_detail(self, object_list, bundle):
        """
        Can the requested record be read?

        Returns a Boolean.

        """
        return bundle.obj.owner == bundle.request.user

    def create_detail(self, object_list, bundle):
        """
        Can the requested record be created?

        Returns a Boolean.

        """
        return bundle.obj.owner == bundle.request.user

    def update_detail(self, object_list, bundle):
        """
        Can the requested record be updated?

        Returns a Boolean.

        """
        return bundle.obj.owner == bundle.request.user

    def delete_detail(self, object_list, bundle):
        """
        Can the requested record be deleted?

        Returns a Boolean.

        """
        return bundle.obj.owner == bundle.request.user

    def read_list(self, object_list, bundle):
        """
        What list of objects can be read?

        Returns a query set.

        """
        return object_list.filter(owner=bundle.request.user)

    def create_list(self, object_list, bundle):
        """
        Which list of objects can be created?

        Returns a query set.

        """
        for item in object_list:
            item.owner == bundle.request.user
        return object_list

    def update_list(self, object_list, bundle):
        """
        Which list of objects can be updated?

        Returns a query set.

        """
        allowed = []
        for item in object_list:
            if item.owner == bundle.request.user:
                allowed.append(item)
        return allowed

    def delete_list(self, object_list, bundle):
        """
        Which list of objects can be deleted?

        Returns a query set.

        """
        allowed = []
        for item in object_list:
            if item.owner == bundle.request.user:
                allowed.append(item)
        return allowed

