# coding: utf-8
from django.test import TestCase
from ..models import Page


class PageViewsCase(TestCase):

    def setUp(self):
        self.root_page = Page.objects.create(name='root-page', slug='home')

    def test_homepage_response(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'page/homepage.html')

    def test_page_seponse(self):
        page = Page.objects.create(name='About', slug='about', parent=self.root_page, template='default')
        response = self.client.get(page.get_absolute_url())

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'page/default.html')

    def test_404_reponse(self):
        response = self.client.get('/not-existing-page/')
        self.assertEqual(response.status_code, 404)

