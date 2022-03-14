from rest_framework.serializers import ModelSerializer
from .models import Issue, Comment


class IssueSerializer(ModelSerializer):
	class Meta:
		model = Issue
		fields = "__all__"
		read_field_only = ["id", "project_id", "author_user_id"]

	def validate(self, data):
		if not "assignee_user_id":
			data["assignee_user_id"] = data["author_user_id"]
		return data


class CommentSerializer(ModelSerializer):
	class Meta:
		model = Comment
		fields = "__all__"
		read_field_only = ["id", "issue_id", "author_user_id"]