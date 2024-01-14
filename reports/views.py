import io

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView

import pandas as pd

from tasks.models import Task


@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        operation_summary="Получить конкретную задачу",
    ),
)
class RetrieveReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> HttpResponse:
        tasks = Task.objects.all().values("id", "header", "description", "status")

        df = pd.DataFrame.from_dict(tasks)
        response_bytes = io.BytesIO()

        df.to_excel(response_bytes, index=False)

        filename = "report"

        response = HttpResponse(response_bytes.getvalue(), content_type="application/vnd.ms-excel")
        response['Content-Disposition'] = f'attachment; filename={filename}.xlsx'

        return response

