#from django.contrib import admin

from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from front_end.views import *

urlpatterns = patterns("front_end.views",
    url(r'^$', 'index_view', name='index_view'),
    url(r'^portfolio/$', portfolio_view, name='portfolio_view'),
    url(r'^hire-me/$', hire_me_view, name='blog_view'),
    url(r'^hire-me-do/$', send_mail_view, name='send_mail_view'),
    url(r'^blog/$', blog_view, name='blog_view'),
    #url(r'^blog/(?P<slug>[-\w]+)/$(?P<pk>\d+)/$', article_view, name='article_view'),
    url(r'^blog/(?P<slug>[-\w!home]+)/$', article_view, name='article_view'),
    url(r'^blog/home/', RedirectView.as_view(url='/',), name='index')

    #url(r'^hire-me/$', hire_me_view, name='hire_me_view'),
)