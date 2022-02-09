from django.urls import path
from .views import *

urlpatterns = [
    path('', Home),
    path('api/todos/get', getAllTodo),
    path('api/todos/post', createTodo)
]
