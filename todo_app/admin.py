# todo_list/todo_app/admin.py

from django.contrib import admin
from todo_app.models import Category, Task

admin.site.register(Category)
admin.site.register(Task)
