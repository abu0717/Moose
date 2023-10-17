from django.urls import path
from .views import home, detail, blog, sign_up, login_view

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:pk>', detail, name='detail'),
    path('Artices/', blog, name='blog'),
    path('Sign_up/', sign_up, name='sign_up'),
    path('Log_in', login_view, name='log_in')
]