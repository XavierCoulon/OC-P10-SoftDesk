from rest_framework.permissions import BasePermission, SAFE_METHODS

from users.models import Contributor


class HasIssuePermission(BasePermission):
    # has to be a contributor of the project to get /create issue
    def has_permission(self, request, view):
        if Contributor.objects.filter(project_id=view.kwargs.get("project_pk"), user_id=request.user):
            return True

    # has to be the author of the issue to update / delete
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author_user_id


class HasCommentPermission(BasePermission):
    # has to be a contributor of the project to get /create issue
    def has_permission(self, request, view):
        if Contributor.objects.filter(project_id=view.kwargs.get("project_pk"), user_id=request.user):
            return True

    # has to be a contributor to get or create. The author to update / delete.
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS and Contributor.objects.filter(project_id=view.kwargs.get("project_pk"),
                                                                         user_id=request.user):
            return True
        return request.user == obj.author_user_id
