# views.py
from rest_framework import viewsets
from .models import KingCategory, Categorytwo, Categorythree, Product,Order
from .serializers import KingCategorySerializer, CategorytwoSerializer, CategorythreeSerializer,OrderSerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny 

from rest_framework import  generics


#class ProductViewSet(viewsets.ModelViewSet):
#    permission_classes = [AllowAny]
#    queryset = Product.objects.all()
#    serializer_class = ProductSerializer



class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)