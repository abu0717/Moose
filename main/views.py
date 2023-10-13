from django.shortcuts import render
from .models import PostModel, UserModel


# Create your views here.
def home(request):
    obj = PostModel.objects.all()
    obj2 = UserModel.objects.all()
    return render(request, template_name='index-2.html', context={
        'obj': obj,
        'obj2': obj2,
    })


def detail(request, pk):
    obj = PostModel.objects.filter(pk=pk)
    print(obj)
    return render(request, template_name='blog-single.html', context={
        'obj': obj,
    })

