#!/usr/bin/python
# coding=utf-8

import sys
import requests
import time
import asyncio
import aiohttp


s = requests.session()
s.trust_env = False     # faster

cookie = None

p1s = 'H'
p2s = '0'
p3s = 'B'
p4s = '5'
p5s = '8'


def gen_num1():
    #36864
    p1s = 'ABCDEFGHKLMNPQRSTUVWXYZ'
    p2s = '0689'
    p3s = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
    p4s = '0689'
    p5s = '0689'
    nums = []
    for p1 in p1s:
        for p2 in p2s:
            for p3 in p3s:
                for p4 in p4s:
                    for p5 in p5s:
                        num = p1+p2+p3+p4+p5
                        nums.append(num)
    return nums

def gen_num2():
    #1472
    # A6A08
    p1s = 'ABCDEFGHKLMNPQRSTUVWXYZ'
    p2s = '0689'
    p4s = '0689'
    p5s = '0689'
    nums = []
    for p1 in p1s:
        for p2 in p2s:
            for p4 in p4s:
                for p5 in p5s:
                    num = p1+p2+p1+p4+p5
                    nums.append(num)
    return nums

def gen_num3():
    #2208
    # A6B66
    p1s = 'ABCDEFGHKLMNPQRSTUVWXYZ'
    p2s = '0689'
    p3s = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
    p5s = '0689'
    nums = []
    for p1 in p1s:
        for p2 in p2s:
            for p3 in p3s:
                num = p1+p2+p3+p2+p2
                nums.append(num)
    return nums

def gen_num4():
    #2208
    # all 4
    p1s = 'ABCDEFGHKLMNPQRSTUVWXYZ'
    p2s = '4'
    p3s = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
    p4s = '4'
    p5s = '0689'
    nums = []
    for p1 in p1s:
        for p2 in p2s:
            for p3 in p3s:
                for p4 in p4s:
                    for p5 in p5s:
                        num = p1+p2+p3+p4+p5
                        nums.append(num)
    return nums

def gen_num5():
    #5520
    #A1B11
    p1s = 'ABCDEFGHKLMNPQRSTUVWXYZ'
    p2s = '0123456789'
    p3s = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
    nums = []
    for p1 in p1s:
        for p2 in p2s:
            for p3 in p3s:
                        num = p1+p2+p3+p2+p2
                        nums.append(num)
    return nums

def gen_num6():
    #1863
    #A2A11
    p1s = 'ABCDEFGHKLMNPQRSTUVWXYZ'
    p2s = '012356789'
    p5s = '012356789'
    nums = []
    for p1 in p1s:
        for p2 in p2s:
            for p5 in p5s:
                num = p1+p2+p1+p5+p5
                nums.append(num)
    return nums

def gen_num7():
    #33856
    #A2B11
    p1s = 'ABCDEFGHKLMNPQRSTUVWXYZ'
    p2s = '01235689'
    p3s = 'ABCDEFGHKLMNPQRSTUVWXYZ'
    p5s = '01235689'
    nums = []
    for p1 in p1s:
        for p2 in p2s:
            for p3 in p3s:
                for p5 in p5s:
                    num = p1+p2+p3+p5+p5
                    nums.append(num)
    return nums

def gen_num8():
    #33856
    #H0B68
    p2s = '01235689'
    p4s = '01235689'
    p5s = '01235689'
    nums = []
    for p2 in p2s:
        for p4 in p4s:
            for p5 in p5s:
                num = 'H'+p2+'B'+p4+p5
                nums.append(num)
    return nums

def gen_num12():
    #1472
    # A6A08
    p1s = 'AB'
    p2s = '04'
    nums = []
    for p1 in p1s:
        for p2 in p2s:
            num = p1+p2+p1+'7'+'4'
            nums.append(num)
    return nums

async def req_one(num):
    p1, p2, p3, p4, p5 = num[0], num[1], num[2], num[3], num[4]
    base_url = 'http://117.36.53.122:9085/zzxh/business/BusinessAction.do?actiontype=xhgzvalidate&timeStamp=1483971549238&clsbdh=1HGCD5656VA008978&hpzl=02&hphm1=A&hphm2={0}&hphm3={1}&hphm4={2}&hphm5={3}&hphm6={4}&cxyzm=true'.format(
        p1, p2, p3, p4, p5)
    headers = {
        'Cookie': 'JSESSIONID=0000WLAEwwhQVRgJ0zmZ7zuTM5K:-1',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': '117.36.53.122:9085',
        'Origin': 'http://117.36.53.122:9085',
        'Referer': 'http://117.36.53.122:9085/zzxh/business/BusinessAction.do?actiontype=third',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }

    payload = {
        "quickreply": 0,
        "tid": 0,
        "content": 'hhh',
        'mask_id_select': 0,
        "mask_name": 0,
        "mask_id": 0,
        'jump': 1,
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(base_url, data=payload, headers=headers) as resp:
            #print(resp.status)
            res = await resp.text()
            #print(res)
            code = res[0:2]
            if code == "00":
                #print("num="+num)
                return str(num)

def req_list(nums):
    coroutines = []
    all_links = []
    for num in nums:
        coroutine = req_one(num)
        coroutines.append(coroutine)
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    res = loop.run_until_complete(asyncio.gather(*coroutines))
    return [i for i in res if i is not None]


def sub_list(nums, max_len):
    d2list = []
    list_div = len(nums) // max_len
    list_mod = len(nums) % max_len
    d2list = [nums[i*max_len:(i+1)*max_len] for i in range(list_div)]
    if list_mod != 0:
        d2list.append(nums[-list_mod:])
    return d2list


def main():
    startt = time.time()
    nums = gen_num7()
    d2list = sub_list(nums, 20)
    result = ['0']
    for d1list in d2list:
        result.extend(req_list(d1list))

    print(result)
    print(len(result))
    with open('nums-async.txt', 'w') as f:
        for i in result:
            f.writelines(i)
    print(time.time()-startt)
    print("over")
if __name__ == '__main__':
    main()
