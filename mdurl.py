#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
入力されたURLからタイトルを取得し、Markdown形式で出力する
Created on 2023.4.16
Author: K. Agata
"""

import sys
import urllib.error
import urllib.request
from argparse import ArgumentParser

from bs4 import BeautifulSoup


def parse_args():
    argparser = ArgumentParser()
    argparser.add_argument("url", nargs="?", default=False, help="target url")
    argparser.add_argument("-l", "--list", action="store_true", help="bulleted list")
    argparser.add_argument("-n", "--number", action="store_true", help="numbered list")
    return argparser.parse_args()


def get_title(url):
    """
    URLからタイトルを取得する
    """
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    return soup.title.string


def get_md_url(url):
    title = get_title(url)
    return f"[{title}]({url})"


if __name__ == "__main__":
    args = parse_args()
    cnt = 1
    while True:
        try:
            if args.url is not False:
                # 引数から
                url = args.url
            else:
                # 標準入力から
                url = input()

            if not url:
                continue

            # Output
            if args.list is True:
                print("- ", end="")
            elif args.number is True:
                print(f"{cnt}. ", end="")
            print(get_md_url(url))

            cnt += 1
        except KeyboardInterrupt:
            break
        except (urllib.error.URLError, ValueError) as e:
            print(e)
            print("Invalid URL", file=sys.stderr)

        if args.url is not False:
            # 引数からの入力の場合は1回で終了
            break
