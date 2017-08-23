# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField('标题', max_length=100)  #博客题目
    category = models.CharField('标签', max_length=50, blank=True)  #博客标签
    date_time = models.DateTimeField('日期', auto_now_add=True)  #博客日期
    content = models.TextField('内容', blank=True, null=True)  #博客文章正文
    author_name = models.CharField('作者', max_length=5)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_time']

class Author(models.Model):
    name = models.CharField(max_length=5)
    author_category = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name