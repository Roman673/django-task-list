from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.tasks, name='tasks'),        
    path('delete/<int:pk>/', views.task_delete, name='delete'),
]
