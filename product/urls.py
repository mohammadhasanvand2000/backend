
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  OrderListCreateView

#router = DefaultRouter()

#router.register('', ProductViewSet)

urlpatterns = [
   path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
]
