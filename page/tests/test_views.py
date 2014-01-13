# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse

from ..models import Page


class PageViewsCase(TestCase):

    def setUp(self):
        self.root_page = Page.objects.create(name='root-page', slug='home')

    def test_homepage_response(self):
        response = self.client.get(reverse('homepage'))

        self.assertEqual(response.status_code, 200)
