from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from .models import Issue, Comment
from users.models import CustomUser


class IssueSerializer(ModelSerializer):
	class Meta:
		model = Issue
		fields = "__all__"
		read_field_only = ["id", "project_id", "author_user_id"]

	def create(self, validated_data):
		if not CustomUser.objects.filter(
			contributor__user_id=validated_data["assignee_user_id"],
			contributor__project_id=validated_data["project_id"]):
			raise ValidationError("Assigned user is not a contributor of the project")
		return super().create(validated_data)

	def update(self, instance, validated_data):
		if "assignee_user_id" in validated_data and not CustomUser.objects.filter(
			contributor__user_id=validated_data["assignee_user_id"], contributor__project_id=instance.project_id_id):
			raise ValidationError("Assigned user is not a contributor of the project")
		return super().update(instance, validated_data)


class CommentSerializer(ModelSerializer):
	class Meta:
		model = Comment
		fields = "__all__"
		read_field_only = ["id", "issue_id", "author_user_id"]
