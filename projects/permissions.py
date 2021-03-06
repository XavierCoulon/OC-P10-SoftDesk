from rest_framework.permissions import BasePermission, SAFE_METHODS

from users.models import Contributor


class HasProjectPermission(BasePermission):

    # has to be a contributor / author of the project to update / delete
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if Contributor.objects.filter(project_id=obj, user_id=request.user, role="Author"):
            return True
