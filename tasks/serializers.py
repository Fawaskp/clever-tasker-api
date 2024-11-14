from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.CharField(source='get_status_display', read_only=True)
    class Meta:
        model = Task
        fields = '__all__'