from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index/index.html')


def products(request):
    return render(request, 'products/all_product.html')


def customers(request):
    return render(request, 'review/customer_review.html')


def vendors(request):
    return render(request, 'review/vendor_review.html')


def contact(request):
    return render(request, 'others/contact.html')
