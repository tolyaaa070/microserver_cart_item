from rest_framework import routers
from .views import CartView , CartItemView
from django.urls import path , include
router =routers.SimpleRouter()

router.register(r'cartitem' , CartItemView , basename='cart_item')
urlpatterns = [
    path('', include(router.urls)),
    path('cart/' , CartView.as_view() , name = 'cart')
]