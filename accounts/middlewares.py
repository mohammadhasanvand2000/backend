from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings


class BlacklistMiddleware(APIView):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # ابتدا پاسخ اصلی را از تابع اصلی دریافت می‌کنیم
        response = self.get_response(request)
        
        # اگر کاربر ادمین (is_staff=True) باشد، پاسخ اصلی را بدون تغییر برمی‌گردانیم
        if request.user and request.user.is_authenticated and request.user.is_staff:
            return response

        # آی‌پی کاربر را از درخواست دریافت می‌کنیم
        client_ip = self.get_client_ip(request)
        
        # اگر آی‌پی کاربر در لیست بلک لیست باشد، پاسخ 403 ارسال می‌شود
        if client_ip in settings.BLACKLIST:
            return Response("دسترسی انکار شد: شما در لیست بلک لیست قرار دارید.", status=status.HTTP_403_FORBIDDEN)
        
        # در غیر این صورت، پاسخ اصلی بدون تغییر برگردانده می‌شود
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
