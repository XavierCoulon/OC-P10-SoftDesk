from django.db import models

from projects.models import Project
from users.models import CustomUser

PRIORITY = ["Faible", "Moyenne", "Elevée"]
TAG = ["Bug", "Amélioration", "Tâche"]
STATUS = ["A faire", "En cours", "Terminé"]


class Issue(models.Model):

    PRIORITY = [
        ('F', 'Faible'),
        ('M', 'Moyenne'),
        ('E', 'Elevée'),
    ]

    TAG = [
        ('B', 'Bug'),
        ('A', 'Amélioration'),
        ('T', 'Tâche'),
    ]

    STATUS = [
        ('A', 'A faire'),
        ('E', 'En cours'),
        ('T', 'Terminé'),
    ]

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    tag = models.CharField(choices=TAG, max_length=64)
    priority = models.CharField(choices=PRIORITY, max_length=64)
    status = models.CharField(choices=STATUS, max_length=64)
    author_user_id = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, related_name="author")
    assignee_user_id = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, related_name="assignee")
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.CharField(max_length=128)
    author_user_id = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
