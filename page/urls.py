from django.conf.urls import patterns, url
from .views import PageDetailView, HomePageView

urlpatterns = patterns('',
    url(r'^(?P<path>.*)/$', PageDetailView.as_view(), name='page'),
    url(r'^$', HomePageView.as_view(), name='homepage', kwargs={'slug': 'home'}),
)

