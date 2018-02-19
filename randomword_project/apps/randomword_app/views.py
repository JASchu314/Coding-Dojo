# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
    if 'number' not in request.session:
        request.session['number'] = 0
        if 'randomword' not in request.session:
            request.session['randomword'] = ''
    return render(request, 'randomword/index.html')

def word(request):
    request.session['number'] += 1
    request.session['randomword'] = get_random_string(length=14)
    return redirect('/')
    
def reset(request):
    del request.session['number']
    del request.session['randomword']
    return redirect('/')


