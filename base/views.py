from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from base.models import Task


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetails(DetailView):
    model = Task
    context_object_name = 'tasks'


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks_list')


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks_list')
