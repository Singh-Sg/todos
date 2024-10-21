from django.contrib import admin
from .models import ToDoItem

# Register your models here.


class ToDoItemModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "status"]


admin.site.register(ToDoItem, ToDoItemModelAdmin)
