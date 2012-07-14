#!/usr/bin/python
#coding=utf-8
#****************************************************
# Author: XYJ - xyj.asmy@gmail.com
# Last modified: 2012-07-14 17:23
# Filename: config.py
# Description:
#****************************************************
import os.path


home_dir = os.path.expanduser("~")
comic_dir_name = "commics"

SAVE_TO_DIR  = os.path.join(home_dir, comic_dir_name)

SUPPORT_SITES = ["www.bengou.com"]

COMIC_LIST = [{u"海贼王":
                {"url":"http://www.bengou.com/080819/hzw0008081910/index.html",
                 "download_all": False}},
            ]
