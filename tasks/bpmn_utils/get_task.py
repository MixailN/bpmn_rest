from tasks.models import Task
from tasks.serializers import TaskSerializer

class GetTask:
    def is_empty(self, task_id):
        return task_id == ""

    def get_tasks(self):
        return TaskSerializer(list(Task.objects.all()), many=True)

    def get_task(self, task_id):
        return TaskSerializer(Task.objects.get(pk=task_id))

    def get_tasks_response_data(self, serializer):
        return serializer.data