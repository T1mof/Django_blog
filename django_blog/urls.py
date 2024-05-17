from django.contrib import admin
from django.urls import path, include
from django_blog import views

urlpatterns = [
    path('', views.index),
    path('articles/', include('django_blog.article.urls')),
    path('about/', views.about),
    path('admin/', admin.site.urls),
]
