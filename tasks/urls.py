from django.urls import path

from tasks import views


urlpatterns = [
    path("", views.TaskListCreateView.as_view()),
    path("<uuid:task_id>/", views.TaskRetrieveDestroyView.as_view()),
]
