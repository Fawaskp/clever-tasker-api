from .models import Task
from .serializers import TaskSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


class TaskListCreateView(ListCreateAPIView):
    serializer_class = TaskSerializer
    filterset_fields = ('status',)
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        filtered_queryset = self.filter_queryset(queryset)
        serilizer = self.get_serializer(filtered_queryset,many=True)
        total_count = filtered_queryset.count()
        return Response({
            "results": serilizer.data,
            "total_count": total_count
        })

class TaskUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskMarkCompletedView(APIView):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.status = 'completed'
        task.completed_at = timezone.now()
        task.save()
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)