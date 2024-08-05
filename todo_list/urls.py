from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage, Todo_list
from django.contrib.auth.views import LogoutView

#from todo_list.views import my_todo_list

urlpatterns = [
    #path('', views.TaskList.as_view(), name='home'),
    path('', views.TodoList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
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

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('register/', views.register, name='register'),
#     path('login/', views.login_view, name='login'),
#     path('logout/', views.logout_view, name='logout'),
#     path('todo_lists/', views.todo_lists, name='todo_lists'),
#     path('todo_lists/add/', views.add_todo_list, name='add_todo_list'),
#     path('todo_lists/<int:pk>/', views.todo_list_detail, name='todo_list_detail'),
#     path('todo_lists/<int:pk>/edit/', views.edit_todo_list, name='edit_todo_list'),
#     path('todo_lists/<int:pk>/delete/', views.delete_todo_list, name='delete_todo_list'),
#     path('todo_lists/<int:list_pk>/items/add/', views.add_todo_item, name='add_todo_item'),
#     path('todo_lists/<int:list_pk>/items/<int:item_pk>/edit/', views.edit_todo_item, name='edit_todo_item'),
#     path('todo_lists/<int:list_pk>/items/<int:item_pk>/delete/', views.delete_todo_item, name='delete_todo_item'),
# ]