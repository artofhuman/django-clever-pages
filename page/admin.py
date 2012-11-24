# -*- coding: utf-8 -*-

from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Page
from django import forms
from ckeditor.widgets import CKEditorWidget
#from feincms.admin import tree_editor
from modeltranslation.admin import TranslationAdmin


class PageAdminForm(forms.ModelForm):
    template = forms.ChoiceField(choices=Page.page_templates, widget=forms.Select)

    def __init__(self, *args, **kwargs):
        super(PageAdminForm, self).__init__(*args, **kwargs)
        self.fields['text_ru'].widget = self.fields['text_en'].widget = self.fields['text_de'].widget = CKEditorWidget(config_name='default')


class PageAdmin(TranslationAdmin, MPTTModelAdmin):
    form = PageAdminForm
    list_display = ('name', 'slug', 'path', 'active', 'created_at', 'updated_at', )
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Page, PageAdmin)
