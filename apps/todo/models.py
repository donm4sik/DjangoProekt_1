from django.db import models

from apps.todo.models_helpers import create_default_description

class Task(models.Model):
    title = models.CharField(
        max_length=75,
        default="DEFAULT TITLE!!!",
        unique_for_date="date_started"
    )
    description = models.TextField(
        max_length=1500,
        verbose_name="task details",
        default=create_default_description

                                   )
    date_started = models.DateField(help_text="День когда задача должна начаться")
    deadline = models.DateField(help_text="День когда задача должна быть выполнена")
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
