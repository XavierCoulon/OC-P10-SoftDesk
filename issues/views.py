from rest_framework import response, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Issue, Comment
from .permissions import HasIssuePermission, HasCommentPermission
from .serializers import IssueSerializer, CommentSerializer


class IssueViewset(ModelViewSet):
	serializer_class = IssueSerializer
	permission_classes = [IsAuthenticated, HasIssuePermission]

	def get_queryset(self, *args, **kwargs):
		return Issue.objects.filter(project_id=self.kwargs.get("project_pk"))

	def create(self, request, *args, **kwargs):
		data = request.data.copy()
		data["project_id"] = self.kwargs.get("project_pk")
		data["author_user_id"] = request.user.id
		if "assignee_user_id" not in data:
			data["assignee_user_id"] = request.user.id
		serialized_data = IssueSerializer(data=data)
		serialized_data.is_valid(raise_exception=True)
		serialized_data.save()

		return response.Response(serialized_data.data, status=status.HTTP_201_CREATED)


class CommentViewset(ModelViewSet):
	serializer_class = CommentSerializer
	permission_classes = [IsAuthenticated, HasCommentPermission]

	def get_queryset(self, *args, **kwargs):
		return Comment.objects.filter(issue_id=self.kwargs.get("issue_pk"))

	def create(self, request, *args, **kwargs):
		data = request.data.copy()
		data["project_id"] = self.kwargs.get("project_pk")
		data["issue_id"] = self.kwargs.get("issue_pk")
		data["author_user_id"] = request.user.id
		serialized_data = CommentSerializer(data=data)
		serialized_data.is_valid(raise_exception=True)
		serialized_data.save()

		return response.Response(serialized_data.data, status=status.HTTP_201_CREATED)
