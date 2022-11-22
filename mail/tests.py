# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

class HomePageTest(TestCase):

    def test_exit_root_route(self):
        '''Проверка наличия пути'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'mail/home.html')
