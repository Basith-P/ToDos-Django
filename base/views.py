from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from base.models import Task


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('tasks_list')


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetails(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'tasks'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks_list')


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks_list')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks_list')
