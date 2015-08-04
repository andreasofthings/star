#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
urly.py to allow tests in travis-ci
"""

from django.conf.urls import patterns, url, include

urlpatterns = patterns(
    '',
    url(
        r'^stars/',
        include(
            'star.urls',
            namespace="star",
            app_name="star"
        )
    )
)
