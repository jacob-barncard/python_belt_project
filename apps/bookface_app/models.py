# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import User
from django.db import models

# Create your models here.

class Friend(models.Model):
    users = models.ManyToManyField(User)
    shown_user = models.ForeignKey(User, related_name = 'owner', null=True)

    def make_friend(cls, shown_user, new_friend):
        friend, created = cls.objects.get_or_create(
            shown_user = shown_user
        )
        friend.users.add(new_friend)

    def remove_friend(cls, shown_user, new_friend):
        friend, created = cls.objects.get_or_create(
            shown_user = shown_user
        )
        friend.users.remove(new_friend)

        return redirect(request, 'bookface_app/dashboard.html')
