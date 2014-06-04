# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.utils.translation import ugettext as _
from django.utils.encoding import python_2_unicode_compatible


from mptt.models import MPTTModel, TreeForeignKey


@python_2_unicode_compatible
class Page(MPTTModel):

    page_templates = (
        ('default', _('Static page')),
    )

    if hasattr(settings, 'PAGE_TEMPLATES'):
        page_templates += settings.PAGE_TEMPLATES

    parent = TreeForeignKey('self', blank=True, null=True,
                            related_name='children', verbose_name=_('Parent page'),
                            help_text=_('All pages must linked to root page.'))
    active = models.BooleanField(default=True, verbose_name=_('Active'))
    name = models.CharField(max_length=300, verbose_name=_('Name'))
    slug = models.SlugField(max_length=200, unique=True, help_text=_('For root page valuse must be home'))
    path = models.CharField(max_length=300, verbose_name=_('Full path'), null=True, blank=True, help_text=_('Build automatic'))
    template = models.CharField(max_length=50, verbose_name=_('Template'), null=True, blank=True)
    text = models.TextField(blank=True, verbose_name=_('Text'))

    meta_title = models.CharField(max_length=300, verbose_name=_('Meta title'), blank=True)
    meta_keywords = models.CharField(max_length=300, verbose_name=_('Meta keywords'), blank=True)
    meta_description = models.TextField(blank=True, verbose_name=_('Meta description'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Create date'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Update date'))

    class Meta:
        db_table = 'page'
        verbose_name = _('Static page')
        ordering = ['tree_id', 'lft']

    def __str__(self):
        return self.name

    def generate_path(self):
        """
        Build full path for page includes all parents

        Example:
            page.generate_path() => '/root-page/this-page-slug/'
        """
        ontology = []
        for item in self.parent.get_ancestors():
            if item.level != 0:
                ontology.append(item.slug)

        if self.parent.level != 0:
            ontology.append(self.parent.slug)

        ontology.append(self.slug)

        return '/' + '/'.join(ontology) + '/'

    def get_absolute_url(self):
        return self.path


@receiver(pre_save, sender=Page)
def generate_path(sender, instance, **kwargs):
    instance.path = '/' if not instance.parent else instance.generate_path()

@receiver(post_save, sender=Page)
def regenerate_subpages_paths(sender, instance, **kwargs):
    for sub_page in instance.get_descendants():
        sub_page.path = sub_page.generate_path()
        sub_page.save()

