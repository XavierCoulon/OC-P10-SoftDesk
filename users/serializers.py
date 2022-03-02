from rest_framework.serializers import ModelSerializer
from .models import CustomUser


class UserSerializer(ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ["first_name", "email", "password"]
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		return CustomUser.objects.create_user(**validated_data)