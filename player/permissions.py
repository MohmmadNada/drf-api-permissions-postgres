from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read Only permissions
        if request.method in permissions.SAFE_METHODS:
            return True
        # If the logged in user same as the author
        # Write persmission
        return request.user == obj.addBy  
        # return request.owner == obj.author  