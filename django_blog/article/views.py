from django.shortcuts import render
from django.views import View

class Index(View):

    def get(self, request, *args, **kwargs):
        app_name = 'Аrticle'
        return render(request, 'articles/article.html', context={'app_name': app_name})