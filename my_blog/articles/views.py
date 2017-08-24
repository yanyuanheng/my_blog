from django.shortcuts import render

# Create your views here.
from articles.models import Article, Author
from django.shortcuts import render, render_to_response, redirect, Http404
from django.template import loader, Template


def main(req):
    blog_main = Article.objects.all()
    abc = Article.objects.all()

    return render_to_response('indexs.html', locals())

def detail(req, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render_to_response('single.html', locals())