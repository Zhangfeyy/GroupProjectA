from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import xlwt
from bs4 import BeautifulSoup
import time
import json
import os

book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('republica', cell_overwrite_ok=True)
sheet.write(0, 0, 'title')
sheet.write(0, 1, 'summary')
sheet.write(0, 2, 'published_time')
sheet.write(0, 3, 'text')


def save_to_excel(soup):
    global n
    try:
        title = soup.find(class_='rep-headline--large my-2 lg:my-4').get_text()
        summary = soup.find(
            class_='rep-body--large text-neutral-dark-gray mb-6 lg:mb-8').get_text()
        published_time = soup.find(id='pub-date').get_text()
        texts = soup.find(id='content').find_all(style='text-align:justify')
        print(f'obtain: {title}  published time: {published_time}')
        sheet.write(n, 0, title)
        sheet.write(n, 1, summary)
        sheet.write(n, 2, published_time)
        sheet.write(n, 3, ' '.join([text.get_text() for text in texts]))
        n += 1
        return True
    except Exception as e:
        print(f"[save_to_excel error] {e}")
        return False


if __name__ == '__main__':

    # default settings
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    # based on the setting of chromedriver
    service = Service('D:\Python2025\chromedriver.exe')
    browser = webdriver.Chrome(service=service, options=options)
    browser.set_window_size(1920, 1080)

    # get cookies (need a json file)
    browser.get('https://myrepublica.nagariknetwork.com/news/search?date=Any%20Time&categories=23%2C23&sort=asc&from_date=2024-01-01&to_date=2025-01-01/')
    browser.delete_all_cookies()
    with open('./jsons/republika.json', 'r') as f:
        ListCookies = json.loads(f.read())
    for cookie in ListCookies:
        browser.add_cookie({
            'domain': '.nagariknetwork.com',
            'name': cookie['name'],
            'value': cookie['value'],
            'path': '/',
            'expires': None,
            'httponly': False,
        })

    # get articles
    page = 1
    n = 1
    max_try = 3

    while True:
        url = f'https://myrepublica.nagariknetwork.com/news/search?date=Any%20Time&categories=23%2C23&sort=asc&from_date=2024-01-01&to_date=2025-01-01&page={page}'
        browser.get(url)
        time.sleep(2)

        # get sources by Soup
        html = browser.page_source
        soup = BeautifulSoup(html, 'lxml')
        for i in range(max_try):
            items = soup.find(id='results-container')
            if items:
                items = items.find_all(class_='lg:flex gap-6 justify-between')
                break
            else:
                print(f"tried {i+1} time(s)")
                time.sleep(2)
        if not items:
            break

        # get the list on the single page
        links = []
        for item in items:
            link = item['href']
            links.append(link)

        # visit the links one by one
        for link in links:
            for i in range(max_try):
                try:
                    browser.get(link)
                    time.sleep(1)
                    html = browser.page_source
                    soup = BeautifulSoup(html, 'lxml')
                    if save_to_excel(soup):
                        break
                    else:
                        print(f"tried {i+1} time(s)")
                        time.sleep(2)
                except Exception as e:
                    print(f"save_to_excel: {e}")

        print(f'--------collected page{page}--------')
        page += 1

    # there is only one window, so no need to switch handles
    # all_h = browser.window_handles
    # browser.switch_to.window(all_h[1])

    browser.quit()
    book.save('../data/np_ms.xls')
    print("bingo!")
