from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

def index(request):
    articles = Article.objects.all()
    return render(request, 'encyclopedia/index.html', {'articles': articles})

def article_detail(request, title):
    article = Article.objects.get(title=title)
    return render(request, 'encyclopedia/article_detail.html', {'article': article})

def create_article(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Article.objects.create(title=title, content=content)
        return redirect('index')
    return render(request, 'encyclopedia/create_article.html')

def edit_article(request, title):
    article = get_object_or_404(Article, title=title)
    if request.method == 'POST':
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()
        return redirect('article_detail', title=article.title)
    return render(request, 'encyclopedia/edit_article.html', {'article': article})

def delete_article(request, title):
    article = get_object_or_404(Article, title=title)
    if request.method == 'POST':
        article.delete()
        return redirect('index')
    return render(request, 'encyclopedia/delete_article.html', {'article': article})