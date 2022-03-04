from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import response, status

from projects.models import Project
from projects.serializers import ProjectSerializer
from projects.permissions import HasProjectPermission
from users.models import Contributor


class ProjectViewset(ModelViewSet):
	serializer_class = ProjectSerializer
	permission_classes = [IsAuthenticated, HasProjectPermission]

	def get_queryset(self):
		user = self.request.user
		return Project.objects.filter(contributors__user_id=user)

	def create(self, request, *args, **kwargs):
		data = request.data.copy()
		serialized_data = ProjectSerializer(data=data)
		serialized_data.is_valid(raise_exception=True)
		project = serialized_data.save()

		contributor = Contributor.objects.create(user_id=request.user, project_id=project, role="Auteur")
		contributor.save()

		return response.Response(serialized_data.data, status=status.HTTP_201_CREATED)



