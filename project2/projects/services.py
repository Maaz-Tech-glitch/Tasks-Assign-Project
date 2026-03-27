from rest_framework.exceptions import ValidationError

def delete_project(project):
    incomplete_tasks = project.tasks.filter(status__in=["todo", "in_progress"])
    if incomplete_tasks.exists():
        raise ValidationError("Project cannot be deleted because it contains incomplete tasks.")
    project.delete()