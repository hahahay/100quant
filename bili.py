# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# headless version

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# drive = webdriver.Chrome(chrome_options=chrome_options)


drive = webdriver.Chrome()

# drive.get("https://www.bilibili.com/video/av41724649/")
drive.get("https://www.bilibili.com/video/av41725006/")
video = WebDriverWait(drive, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='bilibiliPlayer']/div[1]/div[1]/div[8]/video")))  # 找到视频
url = drive.execute_script("return arguments[0].currentSrc;", video)  # 打印视频地址
print(url)

print("start")
drive.execute_script("return arguments[0].play()", video)  # 开始播放
time.sleep(20)

print("stop")
drive.execute_script("return arguments[0].pause()", video)  # 暂停

drive.close()

# driver.quit()

