from django.urls import path
from .views import ToDoItemAPIView, ToDoItemDetailAPIView

urlpatterns = [
    path(
        "todos/", ToDoItemAPIView.as_view(), name="todoitem-list"
    ),  # For listing and creating ToDoItems
    path(
        "todos/<int:pk>/", ToDoItemDetailAPIView.as_view(), name="todoitem-detail"
    ),  # For retrieving, updating, and deleting a specific ToDoItem
]
