from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).order_by('-created_at')
    paginator = Paginator(products, 24)
    page = request.GET.get('page')
    page_items = paginator.get_page(page)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category).order_by('-created_at')
        paginator = Paginator(products, 24)
        page = request.GET.get('page')
        page_items = paginator.get_page(page)


    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'page_items': page_items
    }
    return render(request, 'shop/product/list-2.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    categories = Category.objects.all()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
        'categories': categories,
    }
    return render(request, 'shop/product/detail.html', context)
