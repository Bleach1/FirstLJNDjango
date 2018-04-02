from django.shortcuts import render
from django.template import Context

from . import models


# Create your views here.
# 1.创建
# 2.在Url中配置
# def index(request):
#     return HttpResponse('Hello World')

def index(request):
    return render(request, 'page/index.html', {'Key': 'Value'})


def article_ljn(request):
    article = models.Article.objects.get(pk=1)
    return render(request, 'page/index.html', {'article': article})


def article_all(request):
    # 返回集合
    articles = models.Article.objects.all()
    return render(request, 'page/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'page/article_page.html', {'article': article})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'page/edit_page.html')
    else:
        article = models.Article.objects.get(pk=article_id)
        # 这有大坑  草
        context = Context().update({'article': article})
        return render(request, 'page/edit_page.html', context)


def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')
    if str(article_id) == '0':
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'page/index.html', {'articles': articles})
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'page/article_page.html', {'article': article})
