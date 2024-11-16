from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/',include('auth_handler.urls')),
    path('api/tasks/', include('tasks.urls')),
]