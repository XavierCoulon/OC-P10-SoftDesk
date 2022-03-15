from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Contributor, CustomUser

from .permissions import HasContributorPermission
from .serializers import CustomUserSerializer, ContributorSerializer


class SignUpAPIView(CreateAPIView):
	serializer_class = CustomUserSerializer


class ContributorViewset(ModelViewSet):
	serializer_class = ContributorSerializer
	permission_classes = [IsAuthenticated, HasContributorPermission]

	def get_queryset(self, *args, **kwargs):
		return Contributor.objects.filter(project_id=self.kwargs.get("project_pk"))

	def create(self, request, *args, **kwargs):
		data = request.data.copy()
		data["project_id"] = self.kwargs.get("project_pk")
		serialized_data = ContributorSerializer(data=data)
		serialized_data.is_valid(raise_exception=True)
		serialized_data.save()

		return Response(serialized_data.data, status=status.HTTP_201_CREATED)


class CustomUserViewset(ModelViewSet):
	serializer_class = CustomUserSerializer
	queryset = CustomUser.objects.all()

	# def get_queryset(self, *args, **kwargs):
	# 	print(self.request.user.id)
	# 	print(CustomUser.objects.filter(id=self.request.user.id))
	# 	return CustomUser.objects.filter(id=self.request.user.id)
