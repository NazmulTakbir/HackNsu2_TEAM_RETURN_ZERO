from django.shortcuts import render
from login_signup import models as ls
from products import models as p
import datetime
# Create your views here.

def index(request):
    return render(request, 'index/index.html')


def products(request):
    dict = {}
    dict['products'] = list(p.company_product.objects.all())
    print(list(p.company_product.objects.all()))
    return render(request, 'products/all_product.html',dict)

def place_order(product_obj , amount , customer_obj ):
    time = datetime.datetime.now().time()
    order = p.order.objects.create(time = time , order_amount = amount , customer_fk = customer_obj , product_fk = product_obj )
    order.save();

def customers(request):
    dict = {}
    dict['customers'] = list(ls.Customer.objects.all())
    return render(request, 'review/customer_review.html' , dict)

def vendors(request):
    return render(request, 'review/vendor_review.html')

def contact(request):
    return render(request, 'others/contact.html')

