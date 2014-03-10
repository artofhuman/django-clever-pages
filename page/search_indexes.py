# coding: utf-8

from haystack.indexes import SearchIndex, Indexable
from models import Page


class PageIndex(SearchIndex, Indexable):
    """ Haystack seach index """
    name = CharField(model_attr='name')
    text = CharField(document=True, use_template=True)
    updated_at = DateTimeField(model_attr='updated_at')

    def get_model(self):
        return Page

    def index_queryset(self):
        """
        Используется, когда весь индекс для модели обновляется.
        TODO: Check this
        """
        return Page.objects.select_related().all()
