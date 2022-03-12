from rest_framework.permissions import BasePermission

from .models import Contributor


class HasContributorPermission(BasePermission):

    # Rule implemented: only a contributor on a project can access
    def has_permission(self, request, view):
        if Contributor.objects.filter(project_id=view.kwargs.get("project_pk"), user_id=request.user):
            return True

    # Rule implemented: only a contributor / author on a project can delete a contributor
    def has_object_permission(self, request, view, obj):
        if Contributor.objects.filter(project_id=view.kwargs.get("project_pk"), user_id=request.user, role="Author"):
            return True
