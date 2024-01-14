from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from tasks.models import Task
from tasks.serializers import TaskCreateSerializer, TaskSerializer
from BPMN_RPA.WorkflowEngine import WorkflowEngine

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

    def post(self, request):
        pad = 'tasks/bpmn_diagrams/CreateTask.xml'
        input_parameter = request.data
        engine = WorkflowEngine(input_parameter=input_parameter)
        doc = engine.open(filepath=pad)
        steps = engine.get_flow(doc)
        result = engine.run_flow(steps)
        return Response(data=TaskSerializer(result).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        pad = 'tasks/bpmn_diagrams/GetTask.xml'
        input_parameter = {"task_id": ""}
        engine = WorkflowEngine(input_parameter=input_parameter)
        doc = engine.open(filepath=pad)
        steps = engine.get_flow(doc)
        result = engine.run_flow(steps)
        return Response(data=result, status=status.HTTP_200_OK)


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

    def get(self, request, task_id):
        pad = 'tasks/bpmn_diagrams/GetTask.xml'
        input_parameter = {"task_id": task_id}
        engine = WorkflowEngine(input_parameter=input_parameter)
        doc = engine.open(filepath=pad)
        steps = engine.get_flow(doc)
        result = engine.run_flow(steps)
        return Response(data=result, status=status.HTTP_200_OK)
