from django.shortcuts import render, redirect
from .models import PostModel, UserModel, CommentModels, TagModels, ChangeBack
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        obj = PostModel.objects.all()
        redirect('home')
        return render(request, template_name='index-2.html', context={
            'obj': obj,
        })
    return redirect('log_in')


def detail(request, pk):
    obj = PostModel.objects.filter(pk=pk)
    comments = CommentModels.objects.filter(post_c_id=pk)
    if request.method == 'POST' and request.POST['name'].strip() != '':
        name = request.POST['name']
        page = pk
        user1 = UserModel.objects.get(username=request.user)

        comment = CommentModels(name=name, post_c_id=page, auther=user1)
        comment.save()
    return render(request, template_name='blog-single.html', context={
        'obj': obj,
        'comments': comments
    })


def blog(request):
    obj = PostModel.objects.all()
    return render(request, template_name='blog.html', context={
        'obj': obj,
    })


def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        avatar = request.FILES['img']
        bio = request.POST['bio']
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        s_password = request.POST.get('s_password')
        if password == s_password:

            new_user = User.objects.create_user(username, email, password)
            new_user.save()

            user = UserModel(first_name=first_name, last_name=last_name, avatar=avatar, bio=bio, username=username,
                             email=email, password=password)
            user.save()

            return redirect("log_in")
        else:
            return render(request, template_name='signup.html')
    return render(request, template_name='signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if username is not None:
            login(request, user)
            return redirect('home')
        else:
            pass
    return render(request, 'login.html')


def add_post(request):
    teg = TagModels.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        img = request.FILES['img']
        description = request.POST['description']
        author = UserModel.objects.get(username=request.user)

        post = PostModel(title=title, img=img, description=description, auther=author)
        post.save()
        return redirect(profile_view)
    return render(request, template_name='post.html', context={
        'teg': teg
    })


def logout_view(request):
    logout(request)
    return redirect('log_in')


def profile_view(request):
    user = UserModel.objects.get(username=request.user)
    blog = PostModel.objects.filter(auther_id=user.pk)
    obj = ChangeBack.objects.filter(auther=user)
    return render(request, template_name='profile.html', context={
        'user': user,
        'blog': blog,
        'obj': obj
    })


def change(request):
    if request.method == 'POST':
        img = request.FILES['img']
        user = UserModel.objects.get(username=request.user)

        back = ChangeBack(back_img=img, auther=user)
        back.save()
        return redirect(profile_view)
    return render(request, template_name='back.html', context={
    })
