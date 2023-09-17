from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_api_key.permissions import HasAPIKey
from .models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework import generics

from .models import User
from django.contrib.auth import logout
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserRegistrationSerializer,SetNewPasswordSerializer,ResetPasswordEmailRequestSerializer, UserLoginSerializer,UserSerializer
from django.contrib.auth import authenticate, login
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,force_str,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from .Util import Util
from django.utils.encoding import smart_bytes

from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import smart_bytes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .serializers import ResetPasswordEmailRequestSerializer
from .models import User
from django.utils.translation import gettext as _
from django.contrib.auth.tokens import default_token_generator


class UserRegistrationAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny,]
    queryset= User.objects.all()
    serializer_class = UserRegistrationSerializer







class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        phoneNumber = serializer.validated_data.get('phoneNumber')
        password = serializer.validated_data.get('password')
        username=email or phoneNumber
        backend = 'accounts.authentication.UserPhoneBackend' if username.isdigit() else 'django.contrib.auth.backends.ModelBackend'
        
        
        user = authenticate(request=request, backend=backend, username= email or phoneNumber, password=password)
        print(email)
        if user is not None:
            login(request, user)
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
            
        else:
            return Response({"message": "یوزر وجود ندارد"}, status=status.HTTP_401_UNAUTHORIZED)
        #else:
            #return Response({"message": "اطلاعات اشتباه است."}, status=status.HTTP_400_BAD_REQUEST)


        






class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        logout(request)
        return Response({"message": " عزیز دلم ، شما با موفقیت خارج شدید (بوس بوس)."}, status=status.HTTP_200_OK)







class UserListView(generics.ListAPIView):
    permission_classes = [IsAdminUser|HasAPIKey]
    queryset= User.objects.all()
    serializer_class = UserRegistrationSerializer







class RequestPasswordResetEmail(GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        email = request.data.get('email')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(str(user.id).encode())
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request).domain
            relative_link = reverse(
                'password_reset_confrim', kwargs={'uidb64': uidb64, 'token': token}
            )
            abs_url = 'http://' + current_site + relative_link
            email_body = f"برای بازیابی رمز عبور خود، لطفاً روی لینک زیر کلیک کنید:\n{abs_url}"
            data = {'email_body': email_body, 'to_email': user.email, 'email_subject': _('بازیابی رمز عبور')}
            Util.send_email(data)
            return Response({'message': _('ایمیل بازیابی رمز عبور با موفقیت ارسال شد.')}, status=status.HTTP_200_OK)
        else:
            return Response({'message': _('کاربری با این ایمیل وجود ندارد.')}, status=status.HTTP_400_BAD_REQUEST)
        
class PasswordTokenCheckAPI(generics.GenericAPIView):
    permission_classes = [AllowAny]
    
    def get(self,request,uidb64,token):
        try:
            id =smart_str(urlsafe_base64_decode(uidb64))
            user =User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                return Response({'error':'Token is not valid,please request a new one'})

            return Response({'success':True, 'message':'Credentials valid', 'uidb64':uidb64, 'token':token},status=status.HTTP_200_OK)
        
        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response({'error':'توکن صحیح نیست دوباره امتحان کنید '})



class SetNewPasswordAPI(generics.GenericAPIView):
    serializer_class=SetNewPasswordSerializer
    permission_classes = [AllowAny]
    def patch(self,request):
        serializer= self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success':True , 'message':'پسورد با موفقیت عوض شد '}, status=status.HTTP_200_OK)