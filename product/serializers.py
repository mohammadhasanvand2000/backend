from rest_framework import serializers
from .models import Additional_field
from .models import Product
from .models import Categorythree,Categorytwo,KingCategory,Customer_comment,Order,OrderItem
from .models import Bestselling











class AdditionalFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Additional_field
        fields = '__all__'


class Customer_commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_comment
        fields = '__all__'


class CategorythreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorythree
        fields = '__all__'  



class CategorytwoSerializer(serializers.ModelSerializer):
    cat3 = CategorythreeSerializer(many=True, read_only=True)
    class Meta:
        model = Categorytwo
        fields = '__all__'





class KingCategorySerializer(serializers.ModelSerializer):
    catg = CategorytwoSerializer(many=True, read_only=True)
    
    class Meta:
        model = KingCategory
        fields = '__all__'






class BestsellingSerializer(serializers.ModelSerializer):


    class Meta:
        model = Bestselling
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    kingcategory = KingCategorySerializer()
    #category2 = Category2Serializer()
    #category3 = Category3Serializer()
    discount_percentage = serializers.FloatField(read_only=True)
    field = AdditionalFieldSerializer(many=True, read_only=True)
    comment = Customer_commentSerializer (many=True, read_only=True)
   
    

    class Meta:
        model = Product
        fields = '__all__'






class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']



        

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(source='orderitem_set', many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'order_items']