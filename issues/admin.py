from django.contrib import admin

from issues.models import Issue, Comment


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
	list_display = (
		"title",
		"tag",
		"description",
	)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = (
		"author_user_id",
		"issue_id",
		"description",
	)