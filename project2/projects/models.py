from django.db import models
from users.models import UserProfile 


# Project model..........
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name="projects")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name    
# Task model..........
class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "Todo"),
        ("in_progress", "In Progress"),
        ("done", "Done"),]
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),]
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="todo")
    priority = models.CharField(max_length=10,choices=PRIORITY_CHOICES,default="medium")
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name="tasks")
    assigned_to = models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True,blank=True,related_name="assigned_tasks")
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
