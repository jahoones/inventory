from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import HttpResponse

def index (request):
    return HttpResponse("Inventory webs")

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'inventory/product_detail.html', {'product': product})

