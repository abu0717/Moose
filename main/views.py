from django.shortcuts import render
from .models import PostModel, UserModel, CommentModels


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
    comments = CommentModels.objects.filter(post_c_id=pk)
    return render(request, template_name='blog-single.html', context={
        'obj': obj,
        'comments': comments
    })


def blog(request):
    obj = PostModel.objects.all()
    return render(request, template_name='blog.html', context={
        'obj' : obj,
    })
