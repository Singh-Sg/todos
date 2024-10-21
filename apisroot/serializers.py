from rest_framework import serializers
from .models import ToDoItem


class ToDoItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the ToDoItem model.

    This serializer converts ToDoItem model instances to JSON format
    and validates incoming data before saving to the database.
    It includes all the fields needed for creating and updating to-do items.
    """

    class Meta:
        # Metadata for the serializer, which specifies the model and fields to be included.
        model = ToDoItem  # The model that this serializer is based on.
        fields = [
            "id",
            "name",
            "description",
            "status",
        ]  # Fields to be serialized and deserialized.
