#!/usr/bin/python
#coding=utf-8
#****************************************************
# Author: XYJ - xyj.asmy@gmail.com
# Last modified: 2012-07-21 16:11
# Filename: models.py
# Description:
#****************************************************

class Section(object):

    def __init__(self, domain, url, title):
        self.domain = domain + '/' if not domain.endswith('/') else domain
        self._url = url.strip('/')
        self.title = title

    def _get_full_url(self):
        return self.domain + self._url

    @property
    def url(self):
        return self. _get_full_url()

    @property
    def num(self):
        return self._url.split('/')[0]
