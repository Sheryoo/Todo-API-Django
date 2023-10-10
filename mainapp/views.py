from django.http import JsonResponse
from rest_framework import generics
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.


class TodoList(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class CreateTodo(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DeleteTodo(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class EditTodo(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class EditStatus(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.completed = not request.data.get('completed', instance.completed)
        instance.save()
        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data)
