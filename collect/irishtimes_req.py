from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import requests
import json

import xlwt
from bs4 import BeautifulSoup
import time

book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('irishtimes', cell_overwrite_ok=True)
sheet.write(0, 0, 'title')
sheet.write(0, 1, 'summary')
sheet.write(0, 2, 'published_time')
sheet.write(0, 3, 'text')


def fetch_with_catch(url, headers, cookies=None, timeout=30):
    try:
        resp = requests.get(url, headers=headers, cookies=cookies, timeout=30)
        return resp
    except Exception as e:
        print(f"[get error] {e} {url}")
        return None


def get_by_selenium(url, cookies_list):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    # based on the setting of chromedriver
    service = Service('D:\Python2025\chromedriver.exe')
    browser = webdriver.Chrome(service=service, options=options)
    browser.set_window_size(1920, 1080)

   # visit the browser first then add the cookie(domin will automatically match)
    browser.get(url)
    time.sleep(1)
    for cookie in cookies_list:
        c = {
            'name': cookie['name'],
            'value': cookie['value'],
            'path': '/',
        }
        browser.add_cookie(c)
    browser.refresh()
    time.sleep(2)

    html = browser.page_source
    if not html:
        return None
    return BeautifulSoup(html, 'lxml')


def save_to_excel(soup, url):
    global n
    try:
        title = soup.find(class_='b-it-headline').get_text()
        summary = soup.find(class_='b-it-subheadline').get_text()
        published_time = soup.find(class_='b-it-byline-block__date').get_text()
        texts = soup.find(
            class_='b-it-article-body article-body-wrapper article-sub-wrapper')
        if not texts:
            texts = get_by_selenium(url, cookies_list).find(
                class_='b-it-article-body article-body-wrapper article-sub-wrapper')
        texts = texts.find_all(class_='c-paragraph paywall')

        print(f'obtain: {title}  published time: {published_time}')
        sheet.write(n, 0, title)
        sheet.write(n, 1, summary)
        sheet.write(n, 2, published_time)
        text_content = ' '.join([text.get_text() for text in texts])
        # xlwt maximum input
        if len(text_content) > 32767:
            text_content = text_content[:32767]
            print(f"[overflow error]")
        sheet.write(n, 3, text_content)
        n += 1
    except Exception as e:
        print(f"[save_to_excel error] {e}")


headers = {
    "User-Agent": "Mozilla/5.0"
}

with open("./jsons/irishtimes.json", "r", encoding="utf-8") as f:
    cookies_list = json.load(f)
cookies = {item["name"]: item["value"] for item in cookies_list}


if __name__ == '__main__':

    n = 1
    max_try = 3

    while True:
        if n == 1:
            url = f'https://www.irishtimes.com/article-index/2024/11/21/'

        # visit the link
        for i in range(max_try):
            resp = fetch_with_catch(url, headers=headers, cookies=cookies)
            if not resp:
                print(f"tried getting the page url {i+1} time(s)")
                time.sleep(2)
            else:
                break
        if not resp:
            break

           # get the list
        soup = BeautifulSoup(resp.text, "lxml")
        try:
            items = soup.find(
                class_='c-stack b-flex-promo-list-block').find_all(class_='c-it-border__bottom c-it-border--mobile c-it-border--tablet c-it-border--desktop')
        except Exception as e:
            print(f"[element error] {e}")
            break
        if not items:
            break

        # traverse each link
        links = []
        for item in items:
            classification = item.find(class_='c-grid b-it-overline-block')
            if classification and classification.get_text() == "Politics":
                link = 'https://www.irishtimes.com' + \
                    item.find(
                        class_='b-flex-promo-card__text-no-overline').find('a')['href']
                links.append(link)

        for index, link in enumerate(links):
            for i in range(max_try):
                resp_item = fetch_with_catch(
                    link, headers=headers, cookies=cookies)
                if not resp_item:
                    print(f"tried getting the item url {i+1} time(s)")
                    time.sleep(2)
                else:
                    break
            if resp_item:
                soup_item = BeautifulSoup(resp_item.text, "lxml")
                save_to_excel(soup_item, link)
            else:
                print(f"[{link} got error]")

        # get the url for the next page
        nxt = soup.find_all(class_='prev-next-item')[1]
        nxt_text = nxt.get_text()
        url = nxt['href']
        if nxt_text == "Jan 01 ":
            break
        else:
            url = 'https://www.irishtimes.com' + url

        time.sleep(2)

    book.save('../data/ir_ms_s5.xls')
    print("bingo!")
