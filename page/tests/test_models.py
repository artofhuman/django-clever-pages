# coding: utf-8
from django.test import TestCase
from ..models import Page


class PageModelsCase(TestCase):

    def test_generate_path_for_root_page(self):
        """
        Set tree we must get urls with parents
        """
        root_page = Page(name='root', slug='home')
        root_page.save()

        second_page = Page(name='second page', slug='second-page', parent=root_page)
        second_page.save()

        self.assertEqual('/', root_page.get_absolute_url())
        self.assertEqual('/second-page/', second_page.get_absolute_url())
