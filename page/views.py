# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from .models import Page

from meta.views import MetadataMixin


class MetaTagsMexin(MetadataMixin):
    """ Mixin for show meta tegs from django-meta """

    def get_meta_description(self, context):
        return self.page.meta_description

    def get_meta_keywords(self, context):
        keywords_str = self.page.meta_keywords
        if keywords_str:
            return [c.strip() for c in keywords_str.split(',')]

    def get_meta_title(self, context):
        return self.page.meta_title or self.page.name


class HomePageView(MetaTagsMexin, DetailView):

    model = Page
    context_object_name = 'page'
    template_name = 'page/homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context

    def get_object(self):
        page = get_object_or_404(self.model, slug='home')
        self.page = page
        return page


class PageDetailView(MetaTagsMexin, DetailView):

    model = Page
    context_object_name = 'page'
    template_name = 'page/default.html'

    def get_object(self):
        page = get_object_or_404(self.model, path=self.request.path, active=1)
        self.page = page
        return page

    def get_template_names(self):
        return ["page/%s.html" % self.page.template]
