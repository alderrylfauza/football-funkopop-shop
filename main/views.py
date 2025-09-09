from django.shortcuts import render
from .models import Product

def show_main(request):
    products = Product.objects.all()  # ambil semua produk dari database
    context = {
        "app_name": "Football FunkoPop Shop",
        "class_name": "PBP A",
        "products": products,
    }
    return render(request, "main.html", context)
