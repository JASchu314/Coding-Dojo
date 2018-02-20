# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from time import gmtime, localtime, strftime

import random

def index(request):
    if 'goldcount' not in request.session:
        request.session['goldcount'] = 0
    if 'log' not in request.session:
        request.session['log'] =''
    return render(request, 'ninjagold/index.html')

def process_money(request):
    now = strftime('%Y/%b/%d %I: %M %p' , localtime())
    if 'farm' in request.POST:
        request.session['gold'] = random.randrange(10 , 21)
        request.session['goldcount'] += request.session['gold']
        request.session['log'] += 'You earned {} Gold from working the farm! '.format(request.session['gold'])+now+'\n'
    elif 'cave' in request.POST:
        request.session['gold'] = random.randrange(5 , 11)
        request.session['goldcount'] += request.session['gold']
        request.session['log'] += 'You entered the Dark Spooky Cave and received {} Gold! '.format(request.session['gold'])+now+'\n'
    elif 'house' in request.POST:
        request.session['gold'] = random.randrange(2 , 6)
        request.session['goldcount'] += request.session['gold']
        request.session['log'] += 'You earned {} Gold cleaning the house, Good Work! '.format(request.session['gold'])+now+'\n'
    elif 'casino'in request.POST:
        request.session['gold'] = random.randrange(-50 , 51)
        request.session['goldcount'] += request.session['gold']
        if request.session['goldcount'] < 0:
            request.session['goldcount'] = 0
            request.session['log'] += 'You went completely broke at the casino, better luck next time! '+now+'\n'
        else:
            if request.session['gold'] <0:
                request.session['log'] += 'You lost {} Gold at the Casino, Dang! '.format(request.session['gold'])+now+'\n'
            elif request.session['gold'] == 0:
                request.session['log'] += 'You broke even at the Casino, Try Again!' +now+'\n'
            elif request.session['gold'] >0:
                request.session['log'] += 'You won {} Gold at the Casino, Congrats, Ya lucky Duck!'.format(request.session['gold'])+now+'\n'
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
# Create your views here.
