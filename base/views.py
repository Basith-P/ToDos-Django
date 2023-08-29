from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from base.models import Task


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('tasks_list')


class RegistrationView(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('tasks_list')

    def form_valid(self, form: Any) -> HttpResponse:
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistrationView, self).form_valid(form)

    def get(self, *args: str, **kwargs: Any) -> HttpResponse:
        if self.request.user.is_authenticated:
            return redirect('tasks_list')
        return super().get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(is_done=False).count()

        search_key = self.request.GET.get('search_field') or ''
        if search_key:
            context['tasks'] = context['tasks'].filter(
                title__icontains=search_key)
        context['search_key'] = search_key

        return context


# class TaskDetails(LoginRequiredMixin, DetailView):
#     model = Task
#     context_object_name = 'tasks'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'desc', 'is_done']
    success_url = reverse_lazy('tasks_list')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'desc', 'is_done']
    success_url = reverse_lazy('tasks_list')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks_list')
