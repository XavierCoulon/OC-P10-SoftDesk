from rest_framework.generics import CreateAPIView
from rest_framework import response, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from users.models import Contributor
from .serializers import CustomUserSerializer, ContributorSerializer


class SignUpAPIView(CreateAPIView):

	serializer_class = CustomUserSerializer

	def post(self, request, *args, **kwargs):
		user = request.data
		serializer = CustomUserSerializer(data=user)

		if serializer.is_valid():
			serializer.save()
			return response.Response(serializer.data, status=status.HTTP_201_CREATED)

		return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContributorViewset(ModelViewSet):
	serializer_class = ContributorSerializer
	permission_classes = [IsAuthenticated, ]

	def get_queryset(self, *args, **kwargs):
		return Contributor.objects.filter(project_id=self.kwargs.get("pk"))

	def create(self, request, *args, **kwargs):
		data = request.data.copy()
		serialized_data = ContributorSerializer(data=data)
		serialized_data.is_valid(raise_exception=True)
		serialized_data.save()

		return response.Response(serialized_data.data, status=status.HTTP_201_CREATED)