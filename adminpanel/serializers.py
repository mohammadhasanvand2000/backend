from rest_framework import serializers
from .models import Ticket,Article
from .models import Visit

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'




class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'




class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'



class DailyVisitSerializer(serializers.Serializer):
    date = serializers.DateField()
    visits = serializers.IntegerField()