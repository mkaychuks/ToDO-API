from rest_framework import serializers

from todoapp.models import Todo


# creating a serializer class for the todos
class TodoSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(source='owner')

    class Meta:
        model = Todo
        fields = [
            'id', 'title', 'tag', 'description', 'date_created',
            'time_created', 'user',
        ]
