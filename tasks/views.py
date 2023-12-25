from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from tasks.models import Task
from tasks.serializers import TaskCreateSerializer, TaskSerializer

__all__ = [
    "TaskListCreateView",
    "TaskRetrieveDestroyView",
]


@method_decorator(
    name="post",
    decorator=swagger_auto_schema(
        operation_summary="Создать задачу",
        request_body=TaskCreateSerializer,
        responses={
            status.HTTP_201_CREATED: TaskSerializer(),
        },
    ),
)
@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        operation_summary="Получить список задач",
        responses={
            status.HTTP_200_OK: TaskSerializer(many=True),
        },
    ),
)
class TaskListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()

    def get_serializer_class(self):
        return {"GET": TaskSerializer, "POST": TaskCreateSerializer}[self.request.method]


@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        operation_summary="Получить конкретную задачу",
        responses={
            status.HTTP_200_OK: TaskSerializer(),
        },
    ),
)
class TaskRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "task_id"
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
