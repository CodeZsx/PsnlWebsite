"""PsnlWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from blog.feeds import AllPostsRssFeed
from website.views import home, about, new_home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^home/', new_home, name='new_home'),
    url(r'^about/', about, name='about'),
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'', include('comments.urls', namespace='comments', app_name='comments')),
    url(r'^search/', include('haystack.urls')),
    url(r'^all/css/$',AllPostsRssFeed(), name='rss'),
]
