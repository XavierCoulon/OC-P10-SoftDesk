"""SoftDesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework_nested import routers
from users.views import SignUpAPIView, ContributorViewset
from projects.views import ProjectViewset
from issues.views import IssueViewset, CommentViewset

router = routers.SimpleRouter()
router.register("projects", ProjectViewset, basename="projects")

contributor_router = routers.NestedSimpleRouter(router, "projects", lookup="project")
contributor_router.register("users", ContributorViewset, basename="users")

issue_router = routers.NestedSimpleRouter(router, "projects", lookup="project")
issue_router.register("issues", IssueViewset, basename="issues")

comment_router = routers.NestedSimpleRouter(issue_router, "issues", lookup="issue")
comment_router.register("comments", CommentViewset, basename="comments")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/signup/', SignUpAPIView.as_view()),
    path('api/', include(router.urls)),
    path('api/', include(contributor_router.urls)),
    path('api/', include(issue_router.urls)),
    path('api/', include(comment_router.urls)),
]
