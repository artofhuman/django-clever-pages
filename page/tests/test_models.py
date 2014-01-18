# coding: utf-8
from django.test import TestCase
from ..models import Page


class PageModelsCase(TestCase):

    def setUp(self):
        self.root_page = Page.objects.create(name='root', slug='home')
        self.second_page = Page.objects.create(name='second page', slug='second-page', parent=self.root_page)

    def test_generate_path_for_root_page(self):
        """
        Set tree we must get urls with parents
        """

        self.assertEqual('/', self.root_page.get_absolute_url())
        self.assertEqual('/second-page/', self.second_page.get_absolute_url())

    def test_regenerate_path_in_subpages(self):
        """
        if update parent page sub pages must recalculate his paths
        """
        test_page = Page.objects.create(name='test-page', slug='test-page', parent=self.second_page)
        test_page_2 = Page.objects.create(name='test-page-2', slug='test-page-2', parent=test_page)
        self.second_page.slug='new-second-page'
        self.second_page.save()

        self.assertEqual(Page.objects.get(pk=test_page.pk).path, '/new-second-page/test-page/')
        self.assertEqual(Page.objects.get(pk=test_page_2.pk).path, '/new-second-page/test-page/test-page-2/')

