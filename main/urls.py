from django.urls import path
from .views import home, detail, blog, sign_up, login_view, logout_view, profile_view, add_post, change

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:pk>', detail, name='detail'),
    path('Artices/', blog, name='blog'),
    path('sign_up/', sign_up, name='sign_up'),
    path('Log_in/', login_view, name='log_in'),
    path('log_out/', logout_view, name='log_out'),
    path('profile', profile_view, name='profile'),
    path('add_post/', add_post, name='add_post'),
    path('change/', change, name='change')
]
