from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
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
    query = request.GET.get('query', '').strip()
    order = request.GET.get('order', '')

    products_qs = Product.objects.filter(is_deleted=False)
    print(products_qs)
    if query:
        products_qs = products_qs.filter(
            Q(name__icontains=query) | Q(brand__icontains=query) | Q(category__icontains=query)
        )

    if order == 'asc':
        products_qs = products_qs.order_by('name')
    elif order == 'desc':
        products_qs = products_qs.order_by('-name')

    context = {
        'products': products_qs,
    }
    return render(request, 'product_page/all_products.html', context)

def product_details(request, product_id):
    productData = get_object_or_404(Product, id=product_id)
    if productData.is_deleted:
        return redirect('all_products')
    
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

def delete_product(request, product_id):
    productData = get_object_or_404(Product, id=product_id, is_deleted=False)
    if request.method == 'POST':
        productData.is_deleted = True
        productData.save()
        return redirect('all_products')

    return redirect('product_details', product_id)