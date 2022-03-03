from rest_framework.generics import CreateAPIView
from rest_framework import response, status

from .serializers import CustomUserSerializer


class SignUpAPIView(CreateAPIView):

	serializer_class = CustomUserSerializer

	def post(self, request, *args, **kwargs):
		user = request.data
		serializer = CustomUserSerializer(data=user)

		if serializer.is_valid():
			serializer.save()
			return response.Response(serializer.data, status=status.HTTP_201_CREATED)

		return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
