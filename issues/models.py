from django.db import models
from django.conf import settings

from projects.models import Project


class Issue(models.Model):

    PRIORITY = [
        ("L", "Low"),
        ("M", "Middle"),
        ("H", "High"),
    ]

    TAG = [
        ("B", "BUG"),
        ("E", "ENHANCEMENT"),
        ("T", "TASK"),
    ]

    STATUS = [
        ("T", "TO DO"),
        ("I", "IN PROGRESS"),
        ("C", "CLOSED"),
    ]

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    tag = models.CharField(choices=TAG, max_length=64)
    priority = models.CharField(choices=PRIORITY, max_length=64)
    status = models.CharField(choices=STATUS, max_length=64)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="author_issue")
    assignee_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="assignee_issue")
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.CharField(max_length=128)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
