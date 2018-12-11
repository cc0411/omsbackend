# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import PingSaltView,RefreshSalt,SaltKeyView,SaltCmd
urlpatterns = [
    #ping
    url(r'^ping/$',PingSaltView.as_view(),name='ping'),
    #delete
    url(r'^keys/$',SaltKeyView.as_view(),name='keys'),
    #refreshsalt
    url(r'^refreshsalt/$',RefreshSalt.as_view(),name='refreshsalt'),
    #cmd
    url(r'^cmd/$',SaltCmd.as_view(),name='cmd')

]