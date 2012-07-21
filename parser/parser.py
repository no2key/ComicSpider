#!/usr/bin/python
#coding=utf-8
#****************************************************
# Author: XYJ - xyj.asmy@gmail.com
# Last modified: 2012-07-21 14:55
# Filename: parser/parser.py
# Description:
#****************************************************

import re

from pyquery import PyQuery as pq

from models import Section


def parse_index(res, url):
    domain = url.rstrip('index.html')
    jquery = pq(res)
    mhlist =  jquery("#mhlist li")
    section_list = []
    for mh in mhlist:
        jquery = pq(mh)
        a = jquery('a')
        section_list.append(Section(domain, a.attr.href, a.attr.title))
    return section_list

def parse_bengou(html, sec_num):
    """ return pictree """
    m = re.search(r'src="(http://pic\d.+?)"', html)
    pic_url = m.group(1)
    pic_type = "." + pic_url.split('.')[-1]
    pic_domain = "/".join(pic_url[7:].split('/')[:4]) + "/"
    m = re.search(r'var pictree\s*=\s*(\[\S+\])', html)
    if m:
        pictree = m.group(1)[1:-1].strip().split(',')
        pictree = ["http://" + pic_domain+sec_num+'/'+pic.strip().strip('\'').split('.')[0]
                + pic_type for pic in pictree]
        print pictree
