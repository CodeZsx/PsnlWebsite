# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import Post, Category, Tag
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
