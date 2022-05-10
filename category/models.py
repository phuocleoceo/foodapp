from django.template.defaultfilters import slugify
from django.urls import reverse
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # allow_unicode để hỗ trợ UTF8
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)
    description = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to="photos/categories", blank=True)

    # Hiển thị trong admin site, số ít và số nhiều
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def save(self, *args, **kwargs):
        """
        Slug có dấu thì URL sẽ bị lỗi không truy cập được 
        Hàm slugify giúp ta chuyển â, ă -> a ,...
        """
        self.slug = slugify(self.slug)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_product(self):
        """
        Hàm sử dụng ở header_menu_links
        Sử dụng hàm reverse để ánh xạ sang views có name = product_by_category ở product app
        với tham số là slug của Category hiện tại
        """
        return reverse("product_by_category", args=[self.slug])
