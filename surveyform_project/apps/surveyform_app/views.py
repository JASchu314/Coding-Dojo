# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
        request.session['name'] = ''
        request.session['location'] = ''
        request.session['language'] = ''
        request.session['comment']  = ''  
    return render(request, 'surveyform/index.html')

def info(request):
    request.session['count'] += 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')

def result(request):
    return render(request, 'surveyform/results.html')
# Create your views here.
