from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Todo_list(models.Model):
    """
    A model representing a TO-DO List.

    Attributes:
        todo_list_id (CharField): Unique identifier for the todo_list.
        slug (CharField): Name of the todo_list.
        due_date (DateField): Due date for the todo_list.
        description (TextField): Description of the todo_list.
        created_by (ForeignKey): User who created the todo_list.
        created_on (DateTimeField): Timestamp when the todo_list was created.
        updated_at (DateTimeField): Timestamp when the todo_list was last
        updated.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="todo_list_lists"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Task(models.Model):
    """
    A model representing a Task in the TO-DO list.

    Attributes:
        task_id (CharField): Unique identifier for the todo_list.

        due_date (DateField): Due date for the todo_list.
        description (TextField): Description of the todo_list.
        created_by (ForeignKey): User who created the todo_list.
        created_on (DateTimeField): Timestamp when the todo_list was created.
        updated_at (DateTimeField): Timestamp when the todo_list was last
        updated.
    """
    #todo_list = models.ForeignKey(Todo_list, on_delete=models.CASCADE, related_name="todo_list_items")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="item_creator")
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | created {self.user}"
        


    # def __str__(self):
    #     return self.title

    # class Meta:
    #     ordering = ['complete']


    

