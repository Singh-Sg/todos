from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ToDoItem
from .serializers import ToDoItemSerializer


class ToDoItemAPIView(APIView):
    """
    API View for handling ToDoItem CRUD operations.
    """

    def get(self, request):
        """
        Retrieve a list of ToDoItems.
        """
        todos = ToDoItem.objects.all()
        serializer = ToDoItemSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a new ToDoItem.
        """
        serializer = ToDoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToDoItemDetailAPIView(APIView):
    """
    API View for handling individual ToDoItem operations.
    """

    def get_object(self, pk):
        """
        Helper method to get a ToDoItem by its primary key.
        """
        try:
            return ToDoItem.objects.get(pk=pk)
        except ToDoItem.DoesNotExist:
            return None

    def get(self, request, pk):
        """
        Retrieve a specific ToDoItem by ID.
        """
        todo_item = self.get_object(pk)
        if todo_item is None:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ToDoItemSerializer(todo_item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """
        Update an existing ToDoItem.
        """
        todo_item = self.get_object(pk)
        if todo_item is None:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ToDoItemSerializer(todo_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        """
        Partially update an existing ToDoItem.
        """
        todo_item = self.get_object(pk)
        if todo_item is None:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ToDoItemSerializer(todo_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete an existing ToDoItem.
        """
        todo_item = self.get_object(pk)
        if todo_item is None:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        todo_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
