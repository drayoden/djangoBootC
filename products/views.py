from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import Product  # in same app, only .models is required otherwise 'products.models' is required.

# Create your views here.

# function based views:

def home_view(request, *args, **kwargs):            # args, 'key word' args = kwargs
    print(f'args, kwargs: {args,kwargs}')
    # return HttpResponse("<h3>Hello world</h3>")   # static response
    context = {"name": "stormy fun pants!"}
    return render(request, 'home.html', context)   # use the context in the rendered page (see index.html)

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

    print(dir(request))
    #return HttpResponse(f"Product id {obj.id}")
    return render(request, 'products/detail.html', {"object": obj})

def product_list_view(request, *args, **kwargs): 
    qs = Product.objects.all() # query set from db
    context = {"object_list": qs}
    return render(request, 'products/list.html', context)


def product_api_detail_view(request, id, **kwargs):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found"}) # return JSON with message
    return JsonResponse({"id": obj.id})



# class based views:

# class HomeView():
#     pass
