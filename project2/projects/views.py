from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Project , Task
from .serializer import ProjectSerializer , TaskSerializer
from .permission import IsProjectOwner  ,  IsAssignedUser
from .filters import TaskFilterSearchOrderingMixin
from .paginations import Pagination
# project class view
class Projects(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated , IsProjectOwner]
    
# Tasks class view
class Tasks(TaskFilterSearchOrderingMixin, ModelViewSet):
    queryset = Task.objects.select_related("project", "assigned_to").all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsAssignedUser]
    pagination_class = Pagination