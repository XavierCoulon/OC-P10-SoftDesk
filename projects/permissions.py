from rest_framework.permissions import BasePermission, SAFE_METHODS

from users.models import Contributor


class HasProjectPermission(BasePermission):

    def has_permission(self, request, view):
        return True
        # return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if Contributor.objects.filter(project_id=obj, user_id=request.user, role="Auteur"):
            return True
        return False
