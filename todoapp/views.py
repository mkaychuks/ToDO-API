from django.shortcuts import get_object_or_404


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST,
    HTTP_204_NO_CONTENT
) 
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView


from todoapp.models import Todo
from todoapp.serializers import TodoSerializer
from todoapp.permissions import IsAuthor


class HomePageView(APIView):
    """ Lists the first 10 latest todos"""
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        latest_todo = Todo.objects.order_by('-date_created')[:11]
        serializer = TodoSerializer(latest_todo, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class ListTodoView(APIView):
    """Enable a logged in user view a TODO created by them"""

    permission_classes = (IsAuthenticated, IsAuthor)

    def get(self, request, format=None):
        user = request.user
        owners_todo = Todo.objects.filter(owner=user)
        serializer = TodoSerializer(owners_todo, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class CreateTodo(CreateAPIView):
    """Allows logged in users to create a TODO"""

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DeleteTodo(APIView):
    """Allows for users to delete TODO"""
    permission_classes = (IsAuthenticated, IsAuthor)

    def delete(slf, request, pk, format=None):
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class UpdateTodo(RetrieveUpdateAPIView):
    """ Allows for retriving and updating a particular TODO"""
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated, IsAuthor)
    queryset = Todo.objects.all()
