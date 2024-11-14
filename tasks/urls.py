from django.urls import path
from .views import TaskListCreateView,TaskMarkCompletedView,TaskUpdateView

urlpatterns =[
    path('list-create/',TaskListCreateView.as_view(),name='list-create-task'),
    path('detail/<int:pk>/',TaskUpdateView.as_view(),name='task-update'),
    path('mark-completed/<int:pk>/',TaskMarkCompletedView.as_view(),name='mark-task-completed'),
]