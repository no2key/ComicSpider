#!/usr/bin/python
#coding=utf-8
#****************************************************
# Author: XYJ - xyj.asmy@gmail.com
# Last modified: 2012-07-21 16:41
# Filename: downloader/downloader.py
# Description:
#****************************************************
import requests

from  parser import parse_bengou

def open_url(url):
    res = requests.get(url)
    if 200<= res.status_code <= 300:
        return res.text
    return None

def download_section(section):
    if section.domain.startswith("http://www.bengou.com"):
        res = open_url(section.url)
        if not res:
            raise Exception("open section %s failure" % section.title)
        pictree = parse_bengou(res, section.num)
