from django.shortcuts import render
from brands.models import Brand
# Create your views here.

def BrandView(request):
    posts = Brand.objects.all()
    data = {
        'posts': posts
    }
    return render(request, 'brand.html', context=data)

def brand_detail(request, id):
    post = Brand.objects.get(id=id)
    data = {
        'post': post
    }
    return render(request, 'detail.html', context=data)

