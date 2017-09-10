# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')

def app(request):
    return render(request, 'app.html')


def about(request):
    return render(request, 'about.html')
