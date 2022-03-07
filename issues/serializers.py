from rest_framework.serializers import ModelSerializer
from .models import Issue


class IssueSerializer(ModelSerializer):
	class Meta:
		model = Issue
		fields = "__all__"
		read_field_only = ["id", "project_id", "author_user_id"]

