from django.template.defaultfilters import slugify
from category.models import Category
from django.urls import reverse
from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # allow_unicode để hỗ trợ UTF8
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)
    # Giá
    price = models.IntegerField()
    # Mô tả
    description = models.TextField(max_length=500, blank=True)
    # Hình ảnh
    image = models.ImageField(upload_to='photos/products')
    # Sản phẩm còn khả dụng (còn để bán) hay không ?
    is_available = models.BooleanField(default=True)
    # auto_now_add : Khi tạo mới thì trường này tự động lấy ngày giờ hiện tại
    created_date = models.DateTimeField(auto_now_add=True)
    # auto_now : Khi chỉnh sửa, trường này tự động lấy ngày giờ hiện tại
    modified_date = models.DateTimeField(auto_now=True)
    # Khóa ngoại, khi xóa category thì mọi sản phẩm thuộc category đó cũng tự mất
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # Hiển thị trong admin site, số ít và số nhiều
    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"

    def save(self, *args, **kwargs):
        """
        Slug có dấu thì URL sẽ bị lỗi không truy cập được 
        Hàm slugify giúp ta chuyển â, ă -> a ,...
        """
        self.slug = slugify(self.slug)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_detail(self):
        """
        Hàm trả về vị trí trang Detail sản phẩm
        """
        return reverse("product_detail", args=[self.slug])
