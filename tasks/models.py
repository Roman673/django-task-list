from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_by']

    def __str__(self):
        return self.name
