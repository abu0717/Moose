from django.urls import path
from .views import home, detail, blog

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:pk>', detail, name='detail'),
    path('Artices/', blog, name='blog')

]