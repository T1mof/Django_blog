from django.urls import path

from django_blog.article import views
from django_blog.article.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
    path('<str:tags>/<int:article_id>/', views.Index.as_view(), name='article'),
]