# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import user

import markdown
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.html import strip_tags

# Create your models here.
from PsnlWebsite import settings


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('标题', max_length=100)
    body = models.TextField('正文')
    created = models.DateTimeField('创建时间', auto_now_add=True)
    modified = models.DateTimeField('修改时间', auto_now=True)
    excerpt = models.CharField('摘要', max_length=54, blank=True,
                               null=True, help_text='可选，如若为空将摘取正文的前54个字符')
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞量', default=0)
    category = models.ForeignKey('Category', verbose_name='分类',
                                 null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created']

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个MarkDown类， 用于渲染body的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将Markdown文本渲染成HTML文本
            # strip_tags去掉HTML文本的全部HTML标签
            # 从文本摘取前54个字符给excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        super(Post, self).save(*args, **kwargs)
