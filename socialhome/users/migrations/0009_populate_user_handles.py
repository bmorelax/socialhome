# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 19:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
from django.db.migrations import RunPython


def forward(apps, schema_editor):
    User = apps.get_model("users", "User")
    for user in User.objects.all():
        user.handle = "%s@%s" % (
            user.username, settings.SOCIALHOME_DOMAIN
        )
        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_handle'),
    ]

    operations = [
        RunPython(forward, RunPython.noop),
    ]
