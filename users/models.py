# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import user

from django.contrib.auth.models import User, AbstractUser

# Create your models here.
from django.db import models


class User(AbstractUser):
    nickname = models.CharField(max_length=30, blank=True, null=True,
                                verbose_name='昵称')
    avatar = models.ImageField(upload_to='avatar',
                               verbose_name='头像')

    # class Meta(AbstractUser.Meta):
    #     pass

    def __str__(self):
        return self.nickname

    def save(self, *args, **kwargs):
        # 当用户更改头像的时候，avatar.name = '文件名'
        # 其他情况下avatar.name = 'upload_to/文件名'

        # if len(self.avatar.name.split('/')) == 1:
        #
        #     print 'before:%s' % self.avatar.name
        #     # 用户上传图片时，将avatar.name改为用户名/文件名
        #     self.avatar.name = self.username + '/' + self.avatar.name

        if self.socialaccount_set.exists():
            self.avatar.name = self.socialaccount_set.first().get_avatar_url()
            print self.socialaccount_set.first().get_avatar_url()
        else:
            print 'is not exists'
        super(User, self).save()
