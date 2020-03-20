from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED,HTTP_400_BAD_REQUEST
from rest_framework.generics import CreateAPIView


from todoapp.models import Todo
from todoapp.serializers import TodoSerializer


class HomePageView(APIView):
    """ Lists the first 10 latest todos"""
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        latest_todo = Todo.objects.order_by('-date_created')[:11]
        serializer = TodoSerializer(latest_todo, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class ListTodoView(APIView):
    """Enable a logged in user create a TODO"""

    permission_classes = (IsAuthenticated,)

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