from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.main, name='main'),
    path('gallery/', views.gallery, name='gallery'),
    path('calculate/', views.calculate, name='calculate'),
    path('reviews/', views.reviews, name='reviews'), # страница с отображением отзывов
    path('write-review/', views.write_reviews, name='write-review'),
    path('contact/', views.contact, name='contact'),
    path('enter/', views.enter, name='enter'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login'),
    path('delete/', views.delete_user, name='delete'),
    path('calculate_table/', views.calculate_table, name='calculate_table'),
    path('delete_pricing/', views.delete_pricing, name='delete_pricing'),
    # path('send_telegram/', views.send_telegram, name='send_telegram'),
    path('personal_account/<str:pk>/', views.personal_account, name='personal_account'),
    path('captcha/', include('captcha.urls')),

]

# путь url для медиафайлов в режиме разработки сайта
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
