# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_and_registration_app.models import User

# Create your models here.
class FriendManager(models.Manager):
    def new(self,data):
        print "creating new friendship"
        print "*************"
        print data, "<<---- data from database"

        add_friend = Friend.objects.create(
            friends = "True",
            id = data['user_id']
        )
        return(add_friend)

    def delete(self,data):
        pass

#Initially set friends to False. When frienship is established toggle boolean field to true.

class Friend(models.Model):
    friends = models.BooleanField(default=False)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = FriendManager()
