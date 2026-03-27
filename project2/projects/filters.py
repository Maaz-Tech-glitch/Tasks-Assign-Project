from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class TaskFilterSearchOrderingMixin:
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["status", "priority"]  
    search_fields = ["title", "description","status"]
    ordering_fields = ["due_date"]
    ordering = ["due_date"]   