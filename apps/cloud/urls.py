# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import RegionView,ZoneView
urlpatterns = [
    #ping
    url(r'^region/$',RegionView.as_view(),name='region'),
    url(r'^zone/$',ZoneView.as_view(),name='zone'),

]
