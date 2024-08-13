from django.shortcuts import render


def index(request):
    return render(request, "home/index.html")

def contact(request):
    return render(request, "contact/index.html")

def blog(request):
    return render(request, "blog/index.html")

def blog_details(request):
    return render(request, "blog_details/index.html")

def checkout(request):
    return render(request, "checkout/index.html")

def product_details(request):
    return render(request, "product_details/index.html")

def regular_page(request):
    return render(request, "reqular_page/index.html")

def shop(request):
    return render(request, "shop/index.html")