from rest_framework.generics import (
        ListAPIView,
        CreateAPIView,
        RetrieveAPIView,
        RetrieveUpdateAPIView,
        RetrieveDestroyAPIView,
    )

from ..models import Task
from .serializers import TaskSerializer


class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreateAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveAPIView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
