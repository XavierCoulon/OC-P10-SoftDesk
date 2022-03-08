from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from projects.models import Project
from projects.serializers import ProjectSerializer
from projects.permissions import HasProjectPermission


class ProjectViewset(ModelViewSet):
	serializer_class = ProjectSerializer
	permission_classes = [IsAuthenticated, HasProjectPermission]
	queryset = Project.objects.all()

	def get_serializer_context(self):
		context = super().get_serializer_context()
		context["user"] = self.request.user
		return context

	def list(self, request, *args, **kwargs):
		queryset = Project.objects.filter(contributors__user_id=request.user)
		serializer = ProjectSerializer(queryset, many=True)
		return Response(serializer.data)
