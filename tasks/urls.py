"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

# from . import views, apiviews
from .views import *
from .apiviews import *

# from tasks.views import *
# from tasks.apiviews import *

from django.contrib.auth.views import LogoutView


from rest_framework.routers import SimpleRouter

router = SimpleRouter(trailing_slash=True)

router.register("api/tasks", TaskViewSet)

router.register("api/status_history", TaskHistoryViewSet, basename="status_history")

router.register("api/history", TaskHistoryApiViewset, basename="history")

# new for level 8, email notification
# router.register("api/email", EmailTaskView, basename="report")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("update-task/<pk>/", GenericTaskUpdateView.as_view()),
    path("detail-task/<pk>", GenericTaskDetailView.as_view()),
    path("delete-task/<pk>", GenericTaskDeleteView.as_view()),
    path("create-task", GenericTaskCreateView.as_view()),
    path("user/signup", UserCreateView.as_view()),
    path("user/login", UserLoginView.as_view()),
    path("user/logout", LogoutView.as_view()),
    path("home/all", GenericTaskViewAll.as_view()),
    path("", redirect),
    path("home/pending", GenericTaskViewPend.as_view()),
    path("home/complete", GenericTaskViewComp.as_view()),
    path("email", EmailTaskView.as_view()),
] + router.urls
