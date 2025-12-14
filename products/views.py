from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'index.html')

def add_product(request):
    if request.method == 'POST':
        Product.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            price=request.POST.get('price'),
            category=request.POST.get('category'),
            brand=request.POST.get('brand'),
            is_available=request.POST.get('is_available', True),
            stock_quantity=request.POST.get('stock_quantity', 0)
        )
    return render(request, 'product_page/add_product.html')

def all_products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product_page/all_products.html', context)