from django.urls import path

from .views import *

urlpatterns = [
    path('', TaskList.as_view(), name='tasks_list')
]
