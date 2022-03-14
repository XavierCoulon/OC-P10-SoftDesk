from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import Issue, Comment
from users.models import Contributor


class HasIssuePermission(BasePermission):

    # Rule implemented:
    def has_permission(self, request, view):
        if Contributor.objects.filter(project_id=view.kwargs.get("project_pk"), user_id=request.user):
            return True

    def has_object_permission(self, request, view, obj):
        if Issue.objects.filter(id=obj.id, author_user_id=request.user):
            return True


class HasCommentPermission(BasePermission):

    # Rule implemented:
    def has_permission(self, request, view):
        if Contributor.objects.filter(project_id=view.kwargs.get("project_pk"), user_id=request.user):
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS and Contributor.objects.filter(project_id=view.kwargs.get("project_pk"), user_id=request.user):
            return True
        if Comment.objects.filter(id=obj.id, author_user_id=request.user):
            return True
