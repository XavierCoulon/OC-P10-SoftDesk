from rest_framework.serializers import ModelSerializer
from .models import CustomUser, Contributor


class CustomUserSerializer(ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ["first_name", "email", "password"]
		extra_kwargs = {'password': {'write_only': True}}

	# Use to hash the password ?
	def create(self, validated_data):
		return CustomUser.objects.create_user(**validated_data)


class ContributorSerializer(ModelSerializer):
	class Meta:
		model = Contributor
		fields = ["user_id", "project_id", "role"]
		read_field_only = ["id", "project_id"]
