from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf.urls import url, include
from rest_framework import routers
from articulos.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'articulos.views.index_view', name='index_view'),
    url(r'^', include('front_end.urls')),
    url(r'^admin/', include('articulos.urls')),
    url(r'^caronte/', include(admin.site.urls)),
    url(r'^froala_editor/', include('froala_editor.urls')),
    url(r'^post/', PostView.as_view(), name='post'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
