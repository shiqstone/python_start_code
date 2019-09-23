from bs4 import BeautifulSoup
from lxml import html
import requests
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "Keep-Alive",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Origin": "wenku.baidu.com",
    "Upgrade-Insecure-Requests": "1",
}

def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

url = "https://wenku.baidu.com/view/6664f84bf7ec4afe04a1dfad?pcf=2"

browser = webdriver.Chrome()
browser.get(url)
# print(browser.page_source)

browser.implicitly_wait(3)

js = "$('.moreBtn').click()"
browser.execute_script(js)

items = browser.find_elements_by_css_selector('.ppt-image-wrap img')

# print(items)
for item in items:
    # print(item)
    image_url = item.get_attribute('src')
    if image_url == None:
        image_url = item.get_attribute('data-src')

    print(image_url)

browser.close()
