from .models import Task
from .serializers import TaskSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


class TaskListCreateView(ListCreateAPIView):
    serializer_class = TaskSerializer
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskScheduledView(APIView):
    def get(self, request):
        scheduled_tasks = Task.objects.filter(user=request.user, is_scheduled=True)
        serializer = TaskSerializer(scheduled_tasks, many=True)
        return Response(serializer.data)


class TaskScheduleView(APIView):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.is_scheduled = True
        task.save()
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskMarkCompletedView(APIView):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.status = 'completed'
        task.completed_at = timezone.now()
        task.save()
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)