from django.shortcuts import render, redirect
from .models import Task, Image
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth  import login

import os
# Create your views here.

class Login(LoginView):
    template_name = 'tasks/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class Register(FormView):
    template_name = 'tasks/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(Register, self).get(*args, **kwargs)

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)

        ftr = self.request.GET.get('q') or ''
        if ftr:
            if ftr == 'creation_date':
                context['tasks'] = context['tasks'].order_by('-created')
            elif ftr == 'due_date':
                context['tasks'] = context['tasks'].order_by('-due_date')
            elif ftr == 'completed':
                context['tasks'] = context['tasks'].filter(is_complete=True)
            else:
                context['tasks'] = context['tasks'].filter(priority__iexact=ftr)

        search_input = self.request.GET.get('search') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)
        
        context['search_input'] = search_input
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        images = Image.objects.filter(task=self.object)

        context['images'] = images

        return context

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'priority', 'due_date']
    success_url = reverse_lazy('tasks')


    def form_valid(self, form):
        form.instance.user = self.request.user

        task_instance = super().form_valid(form)

        images = self.request.FILES.getlist('images')
        for image in images:
            photo = Image.objects.create(
                task=self.object,
                image=image,
            )
        return task_instance
    

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'priority', 'due_date', 'is_complete']
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

    def delete(self, request, *args, **kwargs):
     
        task_instance = self.get_object()

        images = task_instance.image_set.all()

        print(task_instance.title)
        
        for image in images:
            image_path = image.image.path
            os.remove(image_path)

        response = super().delete(request, *args, **kwargs)

        return response

class TaskComplete(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['is_complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        # Toggle the value of is_complete
        form.instance.is_complete = not form.instance.is_complete

        # Save the form and redirect to the success URL
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('tasks')