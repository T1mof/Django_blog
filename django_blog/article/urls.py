from django.urls import path

from django_blog.article.views import IndexView, ArticleView, ArticleCommentsView, ArticleFormView, ArticleFormEditView

urlpatterns = [
    path('', IndexView.as_view(), name='articles'),
    path('<int:id>/edit/', ArticleFormEditView.as_view(), name='articles_update'),
    path('<int:id>/', ArticleView.as_view(), name='article'),
    path('<int:article_id>/comments/<int:id>/', ArticleCommentsView.as_view()),
    path('create/', ArticleFormView.as_view(), name='articles_create'),
]