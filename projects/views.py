from rest_framework.viewsets import ModelViewSet

from projects.models import Project
from projects.serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated


class ProjectViewset(ModelViewSet):
	serializer_class = ProjectSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return Project.objects.all()
