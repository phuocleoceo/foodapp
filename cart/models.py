from product.models import Product
from django.db import models


# Create your models here.
class Cart(models.Model):
    """
    Giỏ hàng
    """
    cart_id = models.CharField(max_length=100, blank=True)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    """
    Sản phẩm trong giỏ hàng
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product
