from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.main, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('calculate/', views.calculate, name='send_mail'),
    path('reviews/', views.reviews, name='reviews'),
    path('contact/', views.contact, name='contact'),
    path('enter/', views.enter, name='enter'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login', views.loginuser, name='loginuser'),

]