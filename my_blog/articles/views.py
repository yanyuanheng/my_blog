from django.shortcuts import render

# Create your views here.
from articles.models import Article, Author
from django.shortcuts import render, render_to_response, redirect
from django.template import loader, Template

def home(req):
    blog_article = Article.objects.all()

    return render_to_response('single.html', locals())

def main(req):
    return render_to_response('index.html', locals())
