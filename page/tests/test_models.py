# coding: utf-8
from django.test import TestCase
from ..models import Page


class PageModelsCase(TestCase):

    def test_generate_path_for_root_page(self):
        """
        Set tree we must get urls with parents
        """
        root_page = Page.objects.create(name='root', slug='home')
        second_page = Page.objects.create(name='second page', slug='second-page', parent=root_page)

        self.assertEqual('/', root_page.get_absolute_url())
        self.assertEqual('/second-page/', second_page.get_absolute_url())

