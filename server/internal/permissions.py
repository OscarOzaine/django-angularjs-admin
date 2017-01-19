from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user

class MyUserPermissions(permissions.BasePermission):
    """
    Handles permissions for users.  The basic rules are
    - owner may GET, PUT, POST, DELETE
    - nobody else can access
    """
    def has_permission(self, request, view):
        # Allow get requests for all
        if request.method == 'GET':
            #print 'user='
            print request.user
            #print obj
            if str(request.user) != "AnonymousUser" and str(request.user) != "":
                return True
                
            return False
            #return request.user == obj
        else:
            if 'obj' in globals():
                return request.user == obj

            return False

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True

