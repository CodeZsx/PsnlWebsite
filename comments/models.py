# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
from PsnlWebsite import settings


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20]
