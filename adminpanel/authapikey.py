from .models import APIKey 






authorization_header = request.META.get('HTTP_AUTHORIZATION')

def check_doing (request,authorization_header):
    key =APIKey.objects.get(key=authorization_header)
        if key:
            parts = authorization_header.split()
            if len(parts) == 2 and parts[0].lower() == 'bearer':
            token = parts[1]
        else:
            token = None
        else:
            token = None