from django.shortcuts import render
from my_pharmacy.models import Category, Products

def pharmacy(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    return render(request, 'pharmacy.html', {'products': products, 'categories': categories})

def category_sort(request,category_slug):
    category = Category.objects.get(category_slug=category_slug)
    sorted_products = Products.objects.filter(category=category)
    return render(request,'pharmacy.html',{'products':sorted_products})

def product_details(request,product_slug):
    products=Products.objects.get(product_slug=product_slug)
    return render(request,'product_details.html',{'products':products})