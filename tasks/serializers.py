from django.contrib.auth.models import User
from rest_framework import serializers

from tasks.models import Task, TaskStatus


class TaskStatusField(serializers.ChoiceField):
    def to_internal_value(self, data):
        return {x.label: x for x in TaskStatus}[data]

    def to_representation(self, value):
        return TaskStatus(value).label


class TaskUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(allow_blank=True)
    last_name = serializers.CharField(allow_blank=True)
    email = serializers.EmailField(allow_blank=True)

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
        ]


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    owner = TaskUserSerializer()
    header = serializers.CharField()
    description = serializers.CharField()
    status = TaskStatusField(choices=TaskStatus)

    class Meta:
        model = Task
        fields = [
            "id",
            "owner",
            "header",
            "description",
            "status",
        ]


class TaskCreateSerializer(serializers.ModelSerializer):
    owner_id = serializers.IntegerField()
    header = serializers.CharField()
    description = serializers.CharField()

    def to_representation(self, instance):
        return TaskSerializer(instance).data
    
    class Meta:
        model = Task
        fields = [
            "owner_id",
            "header",
            "description",
        ]
