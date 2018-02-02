from django.db import models


class Tasks(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
