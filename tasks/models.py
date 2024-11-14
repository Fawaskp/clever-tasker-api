from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    start = models.DateTimeField()
    status = models.CharField(
        max_length=20, 
        choices=[('pending', 'Pending'), ('completed', 'Completed')], 
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ['title','user','start']
        ordering = ['start','title']
    
    def __str__(self):
        return self.title