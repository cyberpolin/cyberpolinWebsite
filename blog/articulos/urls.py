from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from django.conf.urls import url, include
from rest_framework import routers
from articulos.views import *

urlpatterns = patterns('articulos.views',
    #url(r'/$', 'proxy_view', name='proxy_view'),
    # url(r'$', 'articulos_view', name='articulos_view'),
    url(r'articulos/$', 'articulos_view', name='articulos_view' ),
    url(r'^articulos/borrados/$', 'articulos_borrados_view', name='articulos_borrados_view' ),
    url(r'articulos/borrar/(?P<articulo_id>\d+)/$', 'borrar_view', name='borrar_view'),
    url(r'articulos/desborrar/(?P<articulo_id>\d+)/$', 'des_borrar_view', name='des_borrar_view'),
    url(r'articulos/editar/(?P<articulo_id>\d+)/$', 'editar_view', name='editar_view'),
    url(r'^articulos/agregar/$', 'add_article_view', name='add_article_view' ),
    url(r'^articulos/agregar/media/$', 'add_media_view', name='add_media_view'),

    # url(r'^portfolio/$', 'list_portfolio_view', name='list_portfolio_view'),
    # url(r'^portfolio/add$', 'add_portfolio_view', name='add_portfolio_view'),
    # url(r'^portfolio/deleted/', 'portfolio_deleted_view', name = 'portfolio_deleted_view'),
    # url(r'^portfolio/delete/(?P<pk>\d+)/$', portfolio_delete_view, name = 'portfolio_delete_view'),
    # url(r'^portfolio/undelete/(?P<pk>\d+)/$', porfolio_udelete_view, name= 'portfolio_undelete_view'),

    #url(r'^login/', 'login_view', name='login_view'),
    url(r'^login/$', login, {'template_name': 'login.html', }, name="login"),
    url(r'^logout/$', logout, {'template_name': 'index.html', }, name="logout"),
)

