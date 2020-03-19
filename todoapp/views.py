from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK


from todoapp.models import Todo
from todoapp.serializers import TodoSerializer


class HomePageView(APIView):
    """ Lists the first 10 latest todos"""
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        latest_todo = Todo.objects.order_by('-date_created')[:11]
        serializer = TodoSerializer(latest_todo, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
