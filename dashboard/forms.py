from category.models import Category
from product.models import Product
from django import forms


class CategoryForm(forms.ModelForm):
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

    image = forms.ImageField()

    class Meta:
        model = Product
        fields = '__all__'
