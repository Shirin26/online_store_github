from django.shortcuts import render, redirect
from webapp.models import Product, CATEGORIES
from django.shortcuts import get_object_or_404


def index_view(request):
    products = Product.objects.order_by('category', 'name').filter(balance__gt=0)
    context = {'products': products}
    return render(request, 'index.html', context)


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product_view.html', context)


def product_create_view(request):
    if request.method == 'GET':
        return render(request, 'product_create.html', {'categories': CATEGORIES})
    elif request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        balance = request.POST.get('balance')
        price = request.POST.get('price')
        new_product = Product.objects.create(name=name, description=description, category=category, balance=balance, price=price)
        return render(request, 'product_view.html', {'product': new_product})

