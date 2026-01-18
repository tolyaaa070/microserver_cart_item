from django.db import models

class Cart1(models.Model):
    user_id = models.SmallIntegerField()

    def __str__(self):
        return f'{self.user_id}'

class CartItem1(models.Model):
    cart = models.ForeignKey(Cart1, on_delete=models.CASCADE, related_name='items')
    product_id  = models.SmallIntegerField()
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.product_id},{self.quantity}'
