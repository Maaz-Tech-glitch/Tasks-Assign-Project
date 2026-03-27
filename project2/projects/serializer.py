from rest_framework import serializers
from .models import Project , Task
from datetime import date
# ProjectSerializer
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields="__all__"
        
# TaskSerializer
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields="__all__"
        
    def validate(self, data):
        status = data.get("status")
        assigned_to = data.get("assigned_to")
        if status == "done" and not assigned_to:
            raise serializers.ValidationError(
                "Task cannot be marked done without assigning a user.")
        return data
    
    def validate_due_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value
