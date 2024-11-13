from django.urls import path
from .views import TaskListCreateView,TaskScheduledView,TaskScheduleView,TaskMarkCompletedView

urlpatterns =[
    path('list-create/',TaskListCreateView.as_view(),name='list-create-task'),
    path('list-scheduled/',TaskScheduledView.as_view(),name='list-scheduled'),
    path('schedule/<int:pk>/',TaskScheduleView.as_view(),name='schedule-task'),
    path('mark-completed/<int:pk>/',TaskMarkCompletedView.as_view(),name='mark-task-completed'),
]