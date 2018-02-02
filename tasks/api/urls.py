from django.urls import path

from .views import (
    TaskListAPIView,
    )

app_name = 'tasks-api'

urlpatterns = [
    path('', TaskListAPIView.as_view()),
]
