from rest_framework import serializers
from home_app.models import *

class ComboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combo
        fields = '__all__'

class ResursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resurs
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resurs
        fields = '__all__'

class Fast_food_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Fast_food_branch
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
