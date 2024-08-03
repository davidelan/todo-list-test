from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage, Todo_list
from django.contrib.auth.views import LogoutView

#from todo_list.views import my_todo_list

urlpatterns = [
    #path('', views.TaskList.as_view(), name='home'),
    path('', views.TodoList.as_view(), name='home'),
    #path('', TodoList.as_view(), name="todo-list"),
    #path('', TaskList.as_view(), name="task"),
    path('task-create/', TaskCreate.as_view(), name="task-create"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('register/', RegisterPage.as_view(), name="register"),
    path('task/<int:pk>/', TaskDetail.as_view(), name="tasks-detail"),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name="tasks-update"),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name="tasks-delete"),
    
    #path('todo_list/', my_todo_list, name='todo_list'),
]