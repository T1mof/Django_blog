from django.shortcuts import render

def index(request):
    app_name = 'article'
    return render(request, 'articles/article.html', context={'app_name' : app_name})