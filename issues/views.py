from rest_framework import response, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Issue
from .permissions import HasIssuePermission
from .serializers import IssueSerializer


class IssueViewset(ModelViewSet):
	serializer_class = IssueSerializer
	permission_classes = [IsAuthenticated, HasIssuePermission]

	def get_queryset(self, *args, **kwargs):
		return Issue.objects.filter(project_id=self.kwargs.get("project_pk"))

	def create(self, request, *args, **kwargs):
		data = request.data.copy()
		# where comes from self.kwars below ?
		data["project_id"] = self.kwargs.get("project_pk")
		data["author_user_id"] = request.user.id
		serialized_data = IssueSerializer(data=data)
		serialized_data.is_valid(raise_exception=True)
		serialized_data.save()

		return response.Response(serialized_data.data, status=status.HTTP_201_CREATED)
