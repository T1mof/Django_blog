from django.contrib import admin
from django.urls import path, include
from django_blog import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('articles/', include('django_blog.article.urls')),
    path('about/', views.about),
    path('admin/', admin.site.urls),
]
