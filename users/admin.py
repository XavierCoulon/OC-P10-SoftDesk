from django.contrib import admin

from users.models import CustomUser, Contributor


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
	list_display = (
		"id",
		"email",
		"first_name"
	)


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
	list_display = (
		"user_id",
		"project_id",
		"permission",
		"role"
	)
