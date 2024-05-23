from django.shortcuts import render
from django.views import View

from django_blog.article.models import Article

class Index(View):

    def get(self, request, *args, **kwargs):
        return redirect(reverse("article", args={"tags": "python", 'article_id': 42}))

def index(request, tags, article_id):
    return render(request, 'articles/custom_article.html', context={'tags': tags, 'article_id': article_id})

class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })