from django.urls import path

from .views import *

urlpatterns = [
    path('', TaskList.as_view(), name='tasks_list'),
    path('task/<int:pk>/', TaskDetails.as_view(), name='task_details'),
    path('task/create/', TaskCreate.as_view(), name='create_task'),
]
