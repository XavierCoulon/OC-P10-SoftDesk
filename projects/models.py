from django.db import models


class Project(models.Model):

	PROJECT_TYPE = [
		('BE', 'Back End'),
		('FE', 'Front End'),
		('IOS', 'IOS'),
		('A', 'Android'),
	]

	title = models.CharField(max_length=64)
	description = models.TextField(max_length=128, blank=True)
	type = models.CharField(choices=PROJECT_TYPE, max_length=64)
	#author_user_id = models.ForeignKey(to=Contributor, on_delete=models.CASCADE)


