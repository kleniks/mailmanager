# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def home_page(requests):
    return render(requests, 'mail/home.html')
