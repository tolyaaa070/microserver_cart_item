from django.shortcuts import render
from rest_framework import generics , viewsets
from rest_framework.response import Response
from .models import Cart1 , CartItem1
from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, created = Cart1.objects.get_or_create(
            user_id=request.user.id
        )
        serializer = CartSerializers(cart)
        return Response(serializer.data)
class CartItemView(viewsets.ModelViewSet):
    serializer_class = CartItemSerializers

    def get_queryset(self):
        return CartItem1.objects.filter(
            cart__user_id=self.request.user.id
        )

    def perform_create(self, serializer):
        cart, created = Cart1.objects.get_or_create(
            user_id=self.request.user.id
        )
        serializer.save(cart=cart)
