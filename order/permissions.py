from rest_framework import permissions

#post랑 patch만 가능
Allowed_Methods = ['POST']

class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in Allowed_Methods: #POST 이면 모든 사용자 가능
            return True
        else: #GET 이면 superuser만 가능
            return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser