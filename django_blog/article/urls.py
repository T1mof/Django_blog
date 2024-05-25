from django.urls import path

from django_blog.article import views
from django_blog.article.views import IndexView, ArticleView, ArticleCommentsView, ArticleFormCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='articles'),
    path('<int:id>/', ArticleView.as_view(), name='article'),
    path('<int:article_id>/comments/<int:id>/', ArticleCommentsView.as_view()),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
]