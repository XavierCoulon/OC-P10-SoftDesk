from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import Contributor


class HasContributorPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            if Contributor.objects.filter(project_id=view.kwargs.get("project_pk"), user_id=request.user):
                return True
        if Contributor.objects.filter(project_id=view.kwargs.get("project_pk"), user_id=request.user, role="Author"):
            return True
