from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Football FunkoPop Shop!")

def show_main(request):
    products = Product.objects.all()  # ambil semua produk dari database
    context = {
        "app_name": "Football FunkoPop Shop",
        "class_name": "PBP A",
        "products": products,
    }
    return render(request, "main.html", context)
