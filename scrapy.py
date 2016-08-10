#!/usr/bin/python
# coding=utf-8

import sys
import requests
from pyquery import PyQuery as pq
import time
import asyncio
import aiohttp


TIME_FORMAT = '%Y-%m-%d %H:%M'


s = requests.session()
s.trust_env = False     # faster

cookie = None

def login(username, password):
    params = {'actionFlag': 'loginAuthenticate',
              'lang': 'en',
              'loginMethod': 'login',
              'loginPageType': 'mix',
              'redirect': 'http://xxxx.hhh.com/cn/index.php?app',
              'redirect_local': '',
              'redirect_modify': '',
              'scanedFinPrint': '',
              'uid': username,
              'password': password,
              'verifyCode': '2345',
              }

    login_url = 'https://login.hhh.com/login/login.do'
    print('login...')

    res = s.post(login_url, params=params)  # 核心代码
    global cookie
    cookie = res.cookies          # 记下cookie，后面会用

    if res.status_code == 200:    # 返回200代表页面成功
        print('successful connected!')

        if cookie is None or cookie['login_failLoginCount'] is None or cookie['login_failLoginCount'] != '0':  	#这才判断login成功
            print('WRONG w3id/password!')
            sys.exit(0)
        else:
            print('successful login')
            
  
  def get_list_page(start, end):
    list_url = 'http://xxx.hhh.com/cn/index.php?app='
    return [list_url.format(i) for i in range(start, end)]


async def get_link(page):
    post_links = []
    async with aiohttp.get(page) as r:
        html = await r.text()
        d = pq(html)
        ul = d('body > div.html_body > div.bbs_left > div.bbs_list_box > div.bbs_list > ul > li > div > div.title > p > a')
    return [li.attrib['href'] for li in ul]


def get_blog_link(page_addr):
    coroutines = []
    all_links =[]
    for page in page_addr:
        coroutine = get_link(page)
        coroutines.append(coroutine)
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    res = loop.run_until_complete(asyncio.gather(*coroutines))
    [all_links.extend(page_links) for page_links in res]
    print(all_links)
    print(len(all_links))
    return all_links
    
    
  def post_page(page_cookie, referer_url, xsname, xsid):
    base_url = 'http://xxx.hhh.com/cn/index.php?app=forum&mod=Do&act=reply'
    post_id = referer_url.rsplit('=', 1)[1]
    headers = {
              'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'zh-CN,zh;q=0.8',
              'Cache-Control': 'max-age=0',
              'Connection': 'keep-alive',
              'Content-Length': '843',
              'Content-Type': 'application/x-www-form-urlencoded',
              'Host': 'xxx.hhh.com',
              'Origin': 'http://xxx.hhh.com',
              'Upgrade-Insecure-Requests': '1',
              }

    payload = {
        "quickreply": 0,
        "tid": post_id,
        "content": 'hhh',
        'mask_id_select': xsid,
        "mask_name": xsname,
        "mask_id": xsid,
        'jump': 1,
    }

    post_response = s.post(base_url, data=payload, cookies=page_cookie, headers=headers)
    print(referer_url)
    return post_response
    
def main():
    startt = time.time()
    login(username, password)
    tlogin = time.time()
    print("tlogin---{}".format(tlogin-startt))
    page_addr = get_list_page(10, 12)
    tpage_addr = time.time()
    print("tpage_addr---{}".format(tpage_addr-tlogin))
    post_links = get_blog_link(page_addr)
    tpost_link = time.time()
    print("tpost_link---{}".format(tpost_link-tpage_addr))

    for link in post_links[0:10]:
        post_page(cookie, link, account, uid)
        time.sleep(5)

    tpost_page = time.time()
    print("tpost_page---{}".format(tpost_page-tpost_page))


if __name__ == '__main__':
    main()
