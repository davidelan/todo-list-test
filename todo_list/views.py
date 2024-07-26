from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Task

# Create your views here.

class TaskList(ListView):
    model = Task
    context_object_name = 'task'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['task'] = context['task'].filter(user=self.request.user)
    #     context['count'] = context['task'].filter(complete=False).count()

    #     search_input = self.request.GET.get('search-area') or ''
    #     if search_input:
    #         context['task'] = context['task'].filter(title__icontains = search_input)
    #         context['search_input'] = search_input
    #     return context


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = "todo_list/task.html"


class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    success_urs = reverse_lazy('task')


class TaskUpdate(UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('task')


class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task')