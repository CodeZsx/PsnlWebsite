# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from comments.models import Comment
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
admin.site.register(Comment)
