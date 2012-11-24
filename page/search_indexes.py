# -*- coding: utf-8 -*-

#import datetime
from haystack.indexes import *
from haystack import site
from models import Page


class PageIndex(RealTimeSearchIndex, SearchIndex):
    """Поисковой индекс по страницам"""
    text = CharField(document=True, use_template=True)
    name = CharField(model_attr='name')
    updated_at = DateTimeField(model_attr='updated_at')

    def index_queryset(self):
        """Используется, когда весь индекс для модели обновляется."""
        return Page.objects.select_related().all()

site.register(Page, PageIndex)
