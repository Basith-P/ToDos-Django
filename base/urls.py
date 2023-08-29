from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import *

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('', TaskList.as_view(), name='tasks_list'),
    # path('task/<int:pk>/', TaskDetails.as_view(), name='task_details'),
    path('task/create/', TaskCreate.as_view(), name='create_task'),
    path('task/edit/<int:pk>/', TaskUpdate.as_view(), name='udpate_task'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(), name='delete_task'),
]
