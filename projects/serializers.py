from rest_framework.serializers import ModelSerializer
from .models import Project
from users.models import Contributor


class ProjectSerializer(ModelSerializer):
	class Meta:
		model = Project
		fields = ["id", "title", "description", "type"]
		extra_kwargs = {
			"title": {"required": True},
			"type": {"required": True},
		}

	def create(self, validated_data):
		project = super().create(validated_data)
		# The creator of the project is automatically recorded as Contributor / Author
		Contributor.objects.create(user_id=self.context["user"], project_id=project, role="Author")
		return project
