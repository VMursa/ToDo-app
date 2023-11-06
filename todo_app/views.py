# todo_list/todo_app/views.py
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from .form import CustomLoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Category, Task


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('index')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')  

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Assume 'login' is the name of your login URL pattern
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class ListListView(ListView):
    model = Category
    template_name = "todo_app/index.html"


class ItemListView(ListView):
    model = Task
    template_name = "todo_app/todo_list.html"

    def get_queryset(self):
        return Task.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = Category.objects.get(id=self.kwargs["list_id"])
        return context


class ListCreate(CreateView):
    model = Category
    fields = ["title"]

    def get_context_data(self):
        context = super().get_context_data()
        context["title"] = "Add a new list"
        return context


class ItemCreate(CreateView):
    model = Task
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]

    def get_initial(self):
        initial_data = super().get_initial()
        todo_list = Category.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super().get_context_data()
        todo_list = Category.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])


class ItemUpdate(UpdateView):
    model = Task
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])


class ListDelete(DeleteView):
    model = Category
    # You have to use reverse_lazy() instead of reverse(),
    # as the urls are not loaded when the file is imported.
    success_url = reverse_lazy("index")


class ItemDelete(DeleteView):
    model = Task

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context
