# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

from time import gmtime, strftime, localtime
def index(request):
  context = {
  "date": strftime("%b %d, %Y", localtime()),
  "time": strftime("%I: %M %p", localtime())
  }
  return render(request,'index.html', context)