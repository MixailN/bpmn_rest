from tasks.serializers import TaskCreateSerializer

class CreateTask:
    def create_serializer_instance(self, data):
        return TaskCreateSerializer(data=data)

    def validate_serializer_data(self, serializer):
        serializer.is_valid()
        return serializer

    def create_task(self,serializer):
        return serializer.create(serializer.validated_data)