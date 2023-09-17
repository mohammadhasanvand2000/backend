from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate, login
from .validators import validate_iranian_phoneNumber
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,force_str,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from rest_framework.exceptions import AuthenticationFailed





class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'phoneNumber', 'email', 'is_active', 'is_staff']





class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    phoneNumber = serializers.CharField(required=False)
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        phoneNumber = data.get('phoneNumber')
        password = data.get('password')

        if not email and not phoneNumber:
            raise serializers.ValidationError("باید حداقل یکی از «ایمیل» یا «شماره موبایل» را وارد کنید.")

        user = None
        if email:
            user = authenticate(username=email, password=password)
        elif phoneNumber and phoneNumber.isdigit():
            user = authenticate(username=phoneNumber, password=password)

        if user:
            if not user.is_active:
                raise serializers.ValidationError("حساب کاربری غیرفعال است")
        else:
            raise serializers.ValidationError("گواهی نامعتبر. لطفا دوباره تلاش کنید.")

        data['user'] = user
        return data


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email =serializers.EmailField(min_length=2)

    class Meta:
        model=User
        fields =['email']


class SetNewPasswordSerializer(serializers.Serializer):
    password=serializers.CharField(min_length=1,max_length=68,write_only=True)
    token=serializers.CharField(min_length=1,write_only=True)
    uidb64=serializers.CharField(min_length=1,write_only=True)


    class Meta:
        fields=['password','token','uidb64']


    def validate(self, attrs):
        try:
            password=attrs.get('password')
            token=attrs.get('token')
            uidb64=attrs.get('uidb64')

            id =force_str(urlsafe_base64_decode(uidb64))
            user=(User.objects.get(id=id))

            if not PasswordResetTokenGenerator().check_token(user,token):
                raise AuthenticationFailed('لینک درست نیست',401)
            user.set_password(password)
            user.save()
        except Exception as e:
            raise AuthenticationFailed('لینک درست hhh',401)

        return super().validate(attrs)