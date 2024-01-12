from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField(
        max_length=1500,
        validators="task details"
    )
    date_started = models.DateField()
    deadline = models.DateField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
