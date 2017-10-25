# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import User
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
    ########You need this so a user who is not registered cannot access certain pages when not logged on. DO NOT FORGET THIS
def logout(request):
    request.session.flush()
    return redirect('/')

def index(request):
    return render(request, 'login_app/index.html')


#Make your database in models with class User
def register(request):
    results = User.objects.registerVal(request.POST)
    if results['status'] == False:
        User.objects.createUser(request.POST)
        messages.success(request, 'Your user has been created. Please log in')
    else:
        for error in results['errors']:
            messages.error(request, error)

    return redirect('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status'] == True:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['first_name'] = results['user'].first_name
        request.session['id'] = results['user'].id
        request.session['email'] = results['user'].email
        return redirect('/dashboard')

def account(request):
    return render(request, 'bookface_app/account.html')
