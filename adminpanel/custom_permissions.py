from rest_framework import permissions

class ApiKeyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        
        api_key = request.META.get('HTTP_API_KEY')
        return api_key == '643760c5-90e7-4082-8f23-7739f17b7085'  
