# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from time import localtime, strftime

from django.shortcuts import HttpResponse, redirect, render


def index(request):
    if 'words' not in request.session:
        request.session['words'] = []
    return render(request, 'sessionwords/index.html')

def input(request):
    if 'big' in request.POST:
        font = 36
    else:
        font = 18
    if 'color' not in request.POST:
        color = 'black'
    else:
        color = request.POST['color']

    word = {
        'word': request.POST['word'],
        'color': color,
        'font': font,
        'time': strftime('%I:%M %p, %B %d, %Y' , localtime())
    }    
    request.session['words'].append(word)
    request.session.modified = True
    return redirect('/', word)

def clear(request):
    request.session.clear()
    return redirect('/')
