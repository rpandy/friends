# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Friend, User


# Create your views here.
def index(request):
    print "FRIENDS INDEX ROUTE"
    print "*****************"

    context = {
        'users': User.objects.all(),
        'friends': Friend.objects.all()
    }
    print "DATA IN CONTEXT ------>>", context

    return render(request,'friends_app/index.html', context)

def user(request, id):
    print "show specific user"
    print "**************"
    specific_user = User.objects.get(id=id)
    print specific_user
    context = {
        'user':specific_user
    }

    return render(request, "friends_app/user.html", context)

def delete(request, id):
    print "Delete user"
    print "**************"
    delete_user = User.objects.get(id=id)
    print delete_user
    context = {
        'delete_user':delete_user
    }

    return redirect('friends:index')


def new(request):
    print "New friend"
    print "**************"

    # data = Friend.objects.new(request.POST)

    print "request.POST:", request.POST

    return redirect('friends:index')
