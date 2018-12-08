# -*- coding: utf-8 -*-
import os
from channels.layers import get_channel_layer
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "omsbackend.settings")
channel_layer = get_channel_layer()
