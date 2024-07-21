from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def my_todo_list(request):
    return HttpResponse("Hello, Blog!")