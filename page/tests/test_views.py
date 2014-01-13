# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse

from ..models import Page


class PageViewsCase(TestCase):

    def setUp(self):
        self.root_page = Page(name='root-page', slug='home')
        self.root_page.save()

    def test_homepage_response(self):
        response = self.client.get(reverse('homepage'))

        self.assertEqual(response.status_code, 200)
