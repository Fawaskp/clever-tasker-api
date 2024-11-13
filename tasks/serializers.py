from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Task
        fields = ['id', 'name', 'user', 'description', 'is_scheduled', 'status', 'priority', 'created_at', 'updated_at', 'completed_at']