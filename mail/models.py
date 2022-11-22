# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Subscribers(models.Model):

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    birthday = models.DateField()

    class Meta:
        db_table = 'subscribers'
        ordering = ["id"]

