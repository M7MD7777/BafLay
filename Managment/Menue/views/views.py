from django.shortcuts import render
from django.shortcuts import render,get_object_or_404, redirect
from ..models import Branche, Category, Product,ParentCategory

def home(request):
    branches=Branche.objects.all()
    categories = Category.objects.all()

    return render(request, 'home.html',{'branches': branches,'categories': categories})

def dashboard(request):
    return render(request, 'dashboard.html')


def branche_categories(request, branche_id):
    branche = get_object_or_404(Branche, pk=branche_id)
    parent_categories = ParentCategory.objects.filter(branche=branche)
    
    return render(request, 'branche/branche_categories.html', {'branche': branche, 'parent_categories': parent_categories})

def parent_category_items(request, parent_category_id):
    parent_category = get_object_or_404(ParentCategory, pk=parent_category_id)
    categories = Category.objects.filter(parent_category=parent_category)

    return render(request, 'parent_category/parent_category_categories.html', {'parent_category': parent_category, 'categories': categories})


def  category_items(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category=category)
    
    return render(request, 'product/category_items.html', {'category': category, 'products': products})

def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product/product_details.html', {'product': product})