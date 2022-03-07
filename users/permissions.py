from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import Contributor


class HasContributorPermission(BasePermission):

    # Rule implemented: only a contributor on a project can create a contributor on this project
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if Contributor.objects.filter(project_id=view.kwargs.get("project_id"), user_id=request.user):
            return True

    # def has_object_permission(self, request, view, obj):
    #     if Contributor.objects.filter(project_id=obj, user_id=request.user):
    #         print("permission OK?")
    #         return True
