# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


from concurrent.futures import ThreadPoolExecutor
from functools import  partial

# headless version
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# drive = webdriver.Chrome(chrome_options=chrome_options)


def play_video(i, av, proxy):
    print(i)
    print(proxy)
    # av = "av41724649"
    drive = webdriver.Chrome()
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
    return i


# play_video("av41724649")


executor = ThreadPoolExecutor(max_workers=2)

av = "av42021723"
proxy = "127.0.0.1"
play_video_av = partial(play_video, av=av, proxy=proxy)

for data in executor.map(play_video_av, range(4)):
    print("in main: {} success".format(data))

print("end of all")

