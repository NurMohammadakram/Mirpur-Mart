from django.shortcuts import get_object_or_404, render, redirect
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

        is_available = request.POST.get('is_available', 'True')
        
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
    productsData = Product.objects.all()
    context = {
        'products': productsData,
    }
    return render(request, 'product_page/all_products.html', context)

def product_details(request, product_id):
    productData = get_object_or_404(Product, id=product_id)
    context = {
        'product': productData,
    }
     
    return render(request, 'product_page/product_details.html', context)

def update_product(request, product_id):
    productData = get_object_or_404(Product, id=product_id)
    
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

        is_available = request.POST.get('is_available', 'True')

        stock_raw = request.POST.get('stock_quantity', '0')
        try:
            stock_quantity = int(stock_raw)
        except (ValueError, TypeError):
            stock_quantity = 0

        image = request.FILES.get('image')

        productData.name = name
        productData.description = description
        productData.price = price
        productData.category = category
        productData.brand = brand
        productData.is_available = is_available
        productData.stock_quantity = stock_quantity
        if image:
            productData.image = image

        productData.save()
        return redirect('product_details', productData.id)
    
    context = {
        'product': productData,
    }
    
    return render(request, 'product_page/update_product.html', context)