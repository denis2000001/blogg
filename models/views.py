from django.shortcuts import render
from models.models import Model
from brands.models import Brand

# Create your views here.

def ModelView(request):
    posts = Model.objects.all()

    data = {
        'posts': posts
    }
    return render(request, 'brand.html', context=data)



def model_detail(request, id):
    post = Model.objects.get(id=id)
    data = {
        'post': post
    }
    return render(request, 'detail.html', context=data)

