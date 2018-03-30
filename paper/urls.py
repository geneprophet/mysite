# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.views.static import serve
from . import search
from mysite import settings

urlpatterns = [
    url(r'^$', search.search_post),
    url(r'^static/(?P<path>.*)$', serve , {'document_root': settings.STATIC_ROOT}),
]
