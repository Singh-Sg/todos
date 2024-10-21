from django.db import models


class ToDoItem(models.Model):
    """
    A model representing a to-do item.

    Attributes:
        name (str): The name of the to-do item. This field is required and has a maximum length of 255 characters.
        description (str): An optional field for a more detailed description of the to-do item.
        status (bool): Indicates whether the to-do item is completed. Defaults to False (not completed).
    """

    name = models.CharField(
        max_length=255
    )  # The name field is required and should be concise.
    description = models.TextField(
        blank=True, null=True
    )  # The description is optional and can be left blank or null.
    status = models.BooleanField(
        default=False
    )  # The status defaults to False (not completed).

    def __str__(self):
        """
        Returns a string representation of the to-do item, which is useful for displaying in the admin interface and debugging.
        """
        return self.name
