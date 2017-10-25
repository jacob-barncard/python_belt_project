# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import User
from django.shortcuts import render, redirect

# Create your views here.
def dashboard(request):
    if 'first_name' not in request.session:
        return redirect('/')
    context = {
        'other_users': User.objects.exclude(id=request.session['id'])
    }
    context = {
        'friend_users': User.objects.exclude(id=request.session['id'])
    }
    ########You need this so a user who is not registered cannot access certain pages when not logged on. DO NOT FORGET THIS
    return render(request, 'bookface_app/dashboard.html', context)

def showUser(request, id):
    context = {
        'shown_user': User.objects.exclude(id = id)
    }
    context = {
        'other_users': User.objects.filter(id=id)
    }
    context = {
        'friend_users': User.objects.filter(id=id)
    }
    return render(request, 'bookface_app/account.html', context)
