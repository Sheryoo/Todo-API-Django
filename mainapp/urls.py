from django.urls import path
from .views import *

urlpatterns = [
    path('get/all/', TodoList.as_view()),
    path('get/<int:pk>/', TodoDetail.as_view()),
    path('create/', CreateTodo.as_view()),
    path('delete/<int:pk>/', DeleteTodo.as_view()),
    path('edit/<int:pk>/', EditTodo.as_view()),
    path('edit/status/<int:pk>/', EditStatus.as_view()),
]
