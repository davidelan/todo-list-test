from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Todo_list(models.Model):
    """
    A model representing a TO-DO List.

    Attributes:
        todo_list_id (CharField): Unique identifier for the todo_list.
        list_name (CharField): Name of the todo_list.
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
    User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
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
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, unique=True, null=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(defualt=False)
    created_on = models.DateTimeField(auto_now_add=True)

    

