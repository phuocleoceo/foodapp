from product.models import Product
from user.models import User
from django.db import models


# Create your models here.
class Order(models.Model):
    # Thuộc về user nào
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # Thông tin user từ trang checkout
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    order_note = models.CharField(max_length=100, blank=True)
    order_total = models.IntegerField()
    # Đơn hàng đã hoàn thành (đã giao) hay chưa
    is_done = models.BooleanField(default=False)
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    # Lưu lại giá sản phẩm tại thời điẻm mua, tránh sau này giá sp thay đổi
    product_price = models.FloatField()
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def order_detail_total(self):
        """
        Hàm trả về Thành tiền của order detail hiện tại
        """
        return self.product_price * self.quantity
