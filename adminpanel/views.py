from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from product.models import OrderItem,Order,Product,Bestselling,Customer_comment,Categorythree,Categorytwo,KingCategory,Additional_field
from product.serializers import OrderSerializer,OrderItemSerializer, AdditionalFieldSerializer,Customer_commentSerializer,CategorythreeSerializer,CategorytwoSerializer,KingCategorySerializer,ProductSerializer,BestsellingSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework import generics
from accounts.models import User
from accounts.serializers import  UserRegistrationSerializer,SetNewPasswordSerializer,ResetPasswordEmailRequestSerializer, UserLoginSerializer,UserSerializer
from .serializers import TicketSerializer,ArticleSerializer,DailyVisitSerializer
from .models import Ticket,Article
from django.utils.timezone import now
from rest_framework_api_key.models import APIKey
from django.db.models.functions import TruncMonth
from rest_framework_api_key.permissions import HasAPIKey
from django.db.models import Count
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import timedelta
from .models import Visit
from rest_framework_api_key.permissions import *
from rest_framework import status
from rest_framework.response import Response
#from rest_framework_api_key.authentication import ApiKeyAuthentication

from .custom_permissions import ApiKeyPermission 

class BestsellingViewSet(viewsets.ModelViewSet):
    #authentication_classes = [ApiKeyAuthentication]
    permission_classes = [IsAdminUser,ApiKeyPermission]
    queryset = Bestselling.objects.all()
    serializer_class = BestsellingSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer




class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer



class KingCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = KingCategory.objects.all()
    serializer_class = KingCategorySerializer



class Customer_commentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Customer_comment.objects.all()
    serializer_class = Customer_commentSerializer


class Additional_fieldViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Additional_field.objects.all()
    serializer_class = AdditionalFieldSerializer



class OrderItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Additional_field.objects.all()
    serializer_class = OrderItemSerializer



class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer




class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer







class TicketListCreateView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




class TicketRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAdminUser]










class DailyAnalyticsAPI(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, format=None):
        today = timezone.now().date()
        visits_today = Visit.objects.filter(timestamp__date=today).count()
        data = {
            "date": today,
            "visits": visits_today
        }
        return Response(data)

class WeeklyAnalyticsAPI(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, format=None):
        today = timezone.now().date()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        visits_this_week = Visit.objects.filter(timestamp__date__range=(start_of_week, end_of_week)).count()
        data = {
            "start_date": start_of_week,
            "end_date": end_of_week,
            "visits": visits_this_week
        }
        return Response(data)

class MonthlyAnalyticsAPI(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, format=None):
        today = timezone.now().date()
        start_of_month = today.replace(day=1)
        end_of_month = (start_of_month + timedelta(days=32)).replace(day=1) - timedelta(days=1)
        visits_this_month = Visit.objects.filter(timestamp__date__range=(start_of_month, end_of_month)).count()
        data = {
            "start_date": start_of_month,
            "end_date": end_of_month,
            "visits": visits_this_month
        }
        return Response(data)
    








class MonthlyVisitAnalytics(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        end_date = now()
        start_date = end_date - timedelta(days=30)

        monthly_data = Visit.objects.filter(timestamp__gte=start_date, timestamp__lte=end_date)\
            .extra({"day": "date(timestamp)"})\
            .values("day")\
            .annotate(total_visits=Count("id"))\
            .order_by("day")

        response_data = []
        for entry in monthly_data:
            response_data.append({
                "date": entry["day"].strftime("%Y-%m-%d"),
                "total_visits": entry["total_visits"]
            })

        return Response(response_data)
