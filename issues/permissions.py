from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import Issue
from users.models import Contributor


class HasIssuePermission(BasePermission):

    # Rule implemented:
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and Contributor.objects.filter(project_id=view.kwargs.get("project_id"), user_id=request.user):
            return True

    def has_object_permission(self, request, view, obj):
        if Issue.objects.filter(id=obj.id, project_id=view.kwargs.get("project_id"), author_user_id=request.user):
            return True
