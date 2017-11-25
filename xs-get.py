#!/usr/bin/python
# coding=utf-8

import sys
import requests
from pyquery import PyQuery as pq


s = requests.session()
s.trust_env = False     # faster


def get_list_page(start, end):
    list_url = 'http://xinsheng.huawei.com/cn/index.php?app=forum&mod=List&act=index&class=461&p={}'
    return [list_url.format(i) for i in range(start, end)]


def get_blog_link(page_addr):
    post_links = []

    for page in page_addr:
        r = s.get(page)
        if r.status_code == 200:
            d = pq(page)
            ul = d('body > div.html_body > div.bbs_left > div.bbs_list_box > div.bbs_list > ul')
            lists = ul.children()
            for li in lists:
                lio = pq(li)
                a = lio('div > div.title > p > font > a').attr('title')
                post_links.append(a)
    return post_links




def main():

    #login()
    page_addr = get_list_page(20, 30)
    post_links = get_blog_link(page_addr)



    for link in post_links[0:10]:
        print(link)



if __name__ == '__main__':
    main()
