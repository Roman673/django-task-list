from django.urls import path

from .views import (
    TaskListAPIView,
    TaskCreateAPIView,
    TaskDestroyAPIView,
    TaskRetrieveAPIView,
    TaskUpdateAPIView,
    )

app_name = 'tasks-api'

urlpatterns = [
    path('', TaskListAPIView.as_view(), name="tasks-list"),
    path('create/', TaskCreateAPIView.as_view(), name="task-create"),
    path('<int:pk>/detail/', TaskRetrieveAPIView.as_view(), name="task-detail"),
    path('<int:pk>/update/', TaskUpdateAPIView.as_view(), name="task-update"),
    path('<int:pk>/delete/', TaskDestroyAPIView.as_view(), name="task-delete"),
]
