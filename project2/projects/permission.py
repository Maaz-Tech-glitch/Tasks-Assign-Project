from rest_framework.permissions import BasePermission

class IsProjectOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user

class IsAssignedUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["PATCH", "PUT"]:
            if request.data.get("status") == "done":
                return obj.assigned_to == request.user
        return True