from rest_framework import serializers
from .models import *
class CartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartItem1
        fields = ['id','product_id','quantity']

class CartSerializers(serializers.ModelSerializer):
    items = CartItemSerializers(many=True, read_only=True)
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Cart1
        fields = ['id','user_id','items']