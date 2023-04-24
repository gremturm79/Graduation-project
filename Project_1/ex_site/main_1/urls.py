from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.main, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('calculate/', views.calculate, name='calculate'),
    path('reviews/', views.reviews, name='reviews'),
    path('write-review/', views.write_reviews, name='write-reviews'),
    # path('write-review/', views.update_profile, name='update-profile'),
    path('contact/', views.contact, name='contact'),
    path('enter/', views.enter, name='enter'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login'),
    path('calculate_table/', views.calculate_table, name='calculate_table'),
    path('personal_account/<str:pk>/', views.personal_account, name='personal_account'),

]