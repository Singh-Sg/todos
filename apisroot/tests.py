from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import ToDoItem


class ToDoItemAPITestCase(APITestCase):
    def setUp(self):
        """
        Create a URL for testing and set up any required data.
        """
        self.todo_url = reverse("todoitem-list")
        self.todo_item_data = {
            "name": "Sample Task",
            "description": "This is a sample task.",
            "status": False,
        }
        self.todo_item = ToDoItem.objects.create(**self.todo_item_data)

    def test_create_todo_item(self):
        """
        Test creating a new ToDoItem.
        """
        response = self.client.post(
            self.todo_url, data=self.todo_item_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            ToDoItem.objects.count(), 2
        )  # One from setUp, one created here
        self.assertEqual(
            ToDoItem.objects.get(id=response.data["id"]).name, "Sample Task"
        )

    def test_get_todo_items(self):
        """
        Test retrieving the list of ToDoItems.
        """
        response = self.client.get(self.todo_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only the one created in setUp

    def test_get_todo_item(self):
        """
        Test retrieving a specific ToDoItem by ID.
        """
        response = self.client.get(reverse("todoitem-detail", args=[self.todo_item.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.todo_item.name)

    def test_update_todo_item(self):
        """
        Test updating an existing ToDoItem.
        """
        update_data = {"name": "Updated Task", "status": True}
        response = self.client.put(
            reverse("todoitem-detail", args=[self.todo_item.id]),
            data=update_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.todo_item.refresh_from_db()
        self.assertEqual(self.todo_item.name, "Updated Task")
        self.assertEqual(self.todo_item.status, True)

    def test_partial_update_todo_item(self):
        """
        Test partially updating an existing ToDoItem.
        """
        partial_update_data = {"status": True}
        response = self.client.patch(
            reverse("todoitem-detail", args=[self.todo_item.id]),
            data=partial_update_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.todo_item.refresh_from_db()
        self.assertEqual(self.todo_item.status, True)

    def test_delete_todo_item(self):
        """
        Test deleting an existing ToDoItem.
        """
        response = self.client.delete(
            reverse("todoitem-detail", args=[self.todo_item.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ToDoItem.objects.count(), 0)  # It should be deleted

    def test_get_non_existent_todo_item(self):
        """
        Test retrieving a non-existent ToDoItem.
        """
        response = self.client.get(
            reverse("todoitem-detail", args=[999])
        )  # Using an ID that doesn't exist
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_non_existent_todo_item(self):
        """
        Test updating a non-existent ToDoItem.
        """
        update_data = {"name": "Updated Task", "status": True}
        response = self.client.put(
            reverse("todoitem-detail", args=[999]), data=update_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_non_existent_todo_item(self):
        """
        Test deleting a non-existent ToDoItem.
        """
        response = self.client.delete(reverse("todoitem-detail", args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
