from django.urls import path
from .views import home, detail

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:pk>', detail, name='detail'),

]