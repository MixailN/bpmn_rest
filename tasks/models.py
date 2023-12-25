import uuid

from django.contrib.auth.models import User
from django.db import models


class TaskStatus(models.IntegerChoices):
    CREATED = 1, "CREATED"
    CANCELLED = 2, "CANCELLED"


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    header = models.CharField(max_length=128)
    description = models.TextField()
    status = models.IntegerField(choices=TaskStatus.choices, default=TaskStatus.CREATED)

