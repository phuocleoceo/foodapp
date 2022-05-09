from .models import Category


def header_menu_links(request):
    """
    Tạo danh mục ở thanh Header
    """
    links = Category.objects.all()
    return dict(links=links)
