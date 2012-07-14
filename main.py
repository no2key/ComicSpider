#!/usr/bin/python
#coding=utf-8
#****************************************************
# Author: XYJ - xyj.asmy@gmail.com
# Last modified: 2012-07-14 19:47
# Filename: main.py
# Description:
#****************************************************

import argparse


def show_comic_list():
    import config
    comic_list = config.COMIC_LIST
    for comic in comic_list:
        print comic.keys()[0]


def update_comics():
    pass


def download_comic(url):
    pass


def checkout_url(url):
    import re, config
    support_sites = config.SUPPORT_SITES
    for site in support_sites:
        if re.match(r"(http://)?{}.*".format(site), url):
            return True
    print "site:%s is not support now"
    return False


def set_args():
    parser = argparse.ArgumentParser(description="download comic from xxx")
    parser.add_argument('-d', "--download", help="download comic from a url")
    parser.add_argument('-u', "--update", action="store_true", help="update comics in config.py")
    parser.add_argument('-l', "--list", action="store_true", help="show the comic list in config.py")
    args = parser.parse_args()
    return args


def main():
    args = set_args()
    if args.list:
        show_comic_list()
        return
    if args.update:
        update_comics()
        return
    url = args.download
    if url and checkout_url(url):
        download_comic(url)

if __name__ == '__main__':
    main()
