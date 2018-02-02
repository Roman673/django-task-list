from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('tasks.urls')),
    path('admin/', admin.site.urls),
    path('api/tasks/', include('tasks.api.urls', namespace='tasks-api')),
]
