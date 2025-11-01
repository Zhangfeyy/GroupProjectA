import requests

import xlwt
from bs4 import BeautifulSoup
import time

book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('republica', cell_overwrite_ok=True)
sheet.write(0, 0, 'title')
sheet.write(0, 1, 'summary')
sheet.write(0, 2, 'published_time')
sheet.write(0, 3, 'text')

headers = {
    "User-Agent": "Mozilla/5.0"
}


def fetch_with_catch(url, headers, timeout=30):
    try:
        resp = requests.get(url, headers=headers, timeout=timeout)
        return resp
    except Exception as e:
        print(f"[get error] {e} {url}")
        return None


def save_to_excel(soup):
    global n
    try:
        title = soup.find(class_='rep-headline--large my-2 lg:my-4').get_text()
        summary = soup.find(
            class_='rep-body--large text-neutral-dark-gray mb-6 lg:mb-8').get_text()
        published_time = soup.find(id='pub-date').get_text()
        texts = soup.find(id='content').find_all('p')
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

    page = 1
    n = 1
    max_try = 3

    while True:
        url = f'https://myrepublica.nagariknetwork.com/news/search?date=Any%20Time&categories=23%2C23&sort=asc&from_date=2024-01-01&to_date=2025-01-01&page={page}'

        for i in range(max_try):
            resp = fetch_with_catch(url, headers=headers)
            if not resp:
                print(f"tried getting the page url {i+1} time(s)")
                time.sleep(2)
            else:
                break
        if not resp:
            break

        soup = BeautifulSoup(resp.text, 'lxml')
        try:
            items = soup.find(
                id='results-container').find_all(class_='lg:flex gap-6 justify-between')
        except Exception as e:
            print(f"[element error] {e}")
            break
        if not items:
            break

        # get the list on the single page
        links = []
        for item in items:
            link = item['href']
            links.append(link)

        # visit the links one by one
        for index, link in enumerate(links):
            for i in range(max_try):
                resp_item = fetch_with_catch(link, headers=headers)
                if not resp_item:
                    print(f"tried getting the item url {i+1} time(s)")
                    time.sleep(2)
                else:
                    break
            if resp_item:
                soup_item = BeautifulSoup(resp_item.text, "lxml")
                save_to_excel(soup_item)
            else:
                print(f"[page {page} no. {index} got error]")

        print(f'--------collected page{page}--------')
        page += 1
        time.sleep(2)

    book.save('../data/np_ms.xls')
    print("bingo!")
