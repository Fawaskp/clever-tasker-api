from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    is_scheduled = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20, 
        choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')], 
        default='pending'
    )
    priority = models.CharField(
        max_length=10, 
        choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], 
        default='medium'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name