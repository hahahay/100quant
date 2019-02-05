# -*- coding: utf-8 -*-
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


from concurrent.futures import ThreadPoolExecutor
from functools import partial

# headless version
'''
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
'''

# drive = webdriver.Chrome(chrome_options=chrome_options)


def play_video(proxy, av):
    # print(i)
    print(proxy)
    # av = "av41724649"
    chrome_options = Options()
    chrome_options.add_argument("--proxy-server=http://{0}".format(proxy))

    drive = webdriver.Chrome(options=chrome_options)
    # drive = webdriver.Chrome()
    av_url = "https://www.bilibili.com/video/{0}/".format(av)
    print(av_url)

    # drive.get("https://www.bilibili.com/video/av41724649/")
    drive.get(av_url)
    video = WebDriverWait(drive, 10, 0.5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='bilibiliPlayer']/div[1]/div[1]/div[8]/video")))  # 找到视频
    url = drive.execute_script("return arguments[0].currentSrc;", video)  # 打印视频地址
    print(url)

    print("start")
    drive.execute_script("return arguments[0].play()", video)  # 开始播放
    time.sleep(10)

    print("stop")
    drive.execute_script("return arguments[0].pause()", video)  # 暂停

    drive.close()
    return 0

def play_video_1(proxy, av):
    # print(i)
    print(proxy)
    # av = "av41724649"
    chrome_options = Options()
    chrome_options.add_argument("--proxy-server=http://{0}".format(proxy))

    drive = webdriver.Chrome(options=chrome_options)
    # drive = webdriver.Chrome()
    av_url = "https://www.bilibili.com/video/{0}/".format(av)
    print(av_url)

    # drive.get("https://www.bilibili.com/video/av41724649/")
    try:
        drive.get(av_url)
        video = WebDriverWait(drive, 20, 0.5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='bilibiliPlayer']/div[1]/div[1]/div[8]/video")))  # 找到视频
        url = drive.execute_script("return arguments[0].currentSrc;", video)  # 打印视频地址
        print(url)

        print("start")
        drive.execute_script("return arguments[0].play()", video)  # 开始播放
        time.sleep(10)

        print("stop")
        drive.execute_script("return arguments[0].pause()", video)  # 暂停
    except Exception as e:
        print('except: {0}'.format(e))
    finally:
        drive.close()


def get_proxy(n):
    s = requests.session()
    r = s.get('http://api3.xiguadaili.com/ip/?tid=559676048748861&num={0}&delay=3&protocol=https'.format(n))
    r1 = r.text
    proxy_list = r1.split("\r\n")
    return proxy_list

# play_video("av41724649")


def play(av, n):
    proxy_list = get_proxy(n)
    executor = ThreadPoolExecutor(max_workers=2)
    play_video_av = partial(play_video_1, av=av)

    for data in executor.map(play_video_av, proxy_list):
        print("in main: 1 success".format(data))


av = "av41723598"
n = 10
play(av, n)
print("end of all")
