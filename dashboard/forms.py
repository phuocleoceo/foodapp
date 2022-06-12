from category.models import Category
from product.models import Product
from django import forms


class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = "Tên danh mục"
        self.fields["slug"].label = "Định danh"
        self.fields["description"].label = "Mô tả"

    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tên danh mục...'
        })
    )

    slug = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Slug...'
        })
    )

    description = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mô tả...'
        })
    )

    class Meta:
        model = Category
        fields = '__all__'


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = "Tên danh mục"
        self.fields["slug"].label = "Định danh"
        self.fields["price"].label = "Đơn giá"
        self.fields["description"].label = "Mô tả"
        self.fields["image"].label = "Hình ảnh"
        self.fields["is_available"].label = "Còn khả dụng ?"
        self.fields["category"].label = "Danh mục"

    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tên danh mục...'
        })
    )

    slug = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Slug...'
        })
    )

    price = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Giá...'
        })
    )

    description = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mô tả...'
        })
    )

    is_available = forms.CheckboxInput()

    image = forms.ImageField()

    class Meta:
        model = Product
        fields = '__all__'
