from django.urls import path

from django_blog.article.views import IndexView, ArticleView, ArticleFormView, \
    ArticleFormEditView, ArticleFormDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='articles'),
    path('<int:id>/edit/', ArticleFormEditView.as_view(), name='articles_update'),
    path('<int:id>/delete/', ArticleFormDeleteView.as_view(), name='articles_delete'),
    path('<int:id>/', ArticleView.as_view(), name='article'),
    path('create/', ArticleFormView.as_view(), name='articles_create'),
]