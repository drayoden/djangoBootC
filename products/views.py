from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import Product  # in same app, only .models is required otherwise 'products.models' is required.

# Create your views here.

# function based views:

def home_view(request, *args, **kwargs): # args, 'key word' args = kwargs
    return HttpResponse("<h3>Hello world</h3>")  # static response

# this version for static id
# def product_detail_view(request, *args, **kwargs):
#     obj = Product.objects.get(id=1)
#     return HttpResponse(f"Product id {obj.id}")

# this version for passing id on url
def product_detail_view(request, pk, **kwargs):  # changed from id to 'pk'
    try:
        obj = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        raise Http404 # render 404 page
    return HttpResponse(f"Product id {obj.id}")

def product_api_detail_view(request, id, **kwargs):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found"}) # return JSON with message
    return JsonResponse({"id": obj.id})



# class based views:

# class HomeView():
#     pass
