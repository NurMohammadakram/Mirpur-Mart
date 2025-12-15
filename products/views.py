from django.shortcuts import render, redirect
from .models import Product
from decimal import Decimal, InvalidOperation


def home(request):
    return render(request, 'index.html')


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        price_raw = request.POST.get('price', '0')
        try:
            price = Decimal(price_raw)
        except (InvalidOperation, TypeError):
            price = Decimal('0.00')

        category = request.POST.get('category')
        brand = request.POST.get('brand')

        is_av_raw = request.POST.get('is_available', 'True')
        is_available = str(is_av_raw).lower() in ('true', '1', 'yes')

        stock_raw = request.POST.get('stock_quantity', '0')
        try:
            stock_quantity = int(stock_raw)
        except (ValueError, TypeError):
            stock_quantity = 0

        image = request.FILES.get('image')

        Product.objects.create(
            name=name,
            description=description,
            price=price,
            category=category,
            brand=brand,
            is_available=is_available,
            stock_quantity=stock_quantity,
            image=image,
        )

        return redirect('all_products')

    return render(request, 'product_page/add_product.html')


def all_products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'product_page/all_products.html', context)
