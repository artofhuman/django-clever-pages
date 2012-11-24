# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from .models import Page


class HomePageView(DetailView):

    model = Page
    context_object_name = 'page'
    template_name = 'page/homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context


class PageDetailView(DetailView):

    model = Page
    context_object_name = 'page'
    template_name = 'page/default.html'

    def get_object(self):

        page = get_object_or_404(Page, path=self.request.path, active=1)
        self.page = page
        return page

    def get_template_names(self):
        return ["page/%s.html" % self.page.template]
