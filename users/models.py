from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

from projects.models import Project


class CustomUserManager(BaseUserManager):
	def create_user(self, email, first_name, password=None):
		if not email:
			raise ValueError("You must enter an email.")

		user = self.model(email=self.normalize_email(email), first_name=first_name)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, first_name, password=None):
		user = self.create_user(email=email, first_name=first_name, password=password)
		user.is_staff = True
		user.save()
		return user


class CustomUser(AbstractBaseUser):
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128, blank=True, default=True)
	email = models.EmailField(unique=True, max_length=255, blank=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["first_name"]
	objects = CustomUserManager()


class Contributor(models.Model):

	ROLES = [
		("A", "Auteur"),
		("C", "Contributeur"),
	]

	user_id = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, related_name="contributors")
	project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name="contributors")
	role = models.CharField(choices=ROLES, max_length=128)

	class Meta:
		unique_together = ("user_id", "project_id")

