from rest_framework.serializers import ModelSerializer
from .models import Project


class ProjectSerializer(ModelSerializer):
	class Meta:
		model = Project
		fields = ["id", "title", "description", "type"]
		extra_kwargs = {
			"title": {"required": True},
			"type": {"required": True}
		}

