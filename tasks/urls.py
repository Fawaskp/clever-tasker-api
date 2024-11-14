from django.urls import path
from .views import TaskListCreateView,TaskMarkCompletedView

urlpatterns =[
    path('list-create/',TaskListCreateView.as_view(),name='list-create-task'),
    path('mark-completed/<int:pk>/',TaskMarkCompletedView.as_view(),name='mark-task-completed'),
]