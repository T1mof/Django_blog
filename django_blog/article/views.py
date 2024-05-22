from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse

class Index(View):

    def get(self, request, *args, **kwargs):
        return redirect(reverse("article", args={"tags": "python", 'article_id': 42}))

def index(request, tags, article_id):
    return render(request, 'articles/custom_article.html', context={'tags': tags, 'article_id': article_id})