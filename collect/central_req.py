import requests

import xlwt
from bs4 import BeautifulSoup
import time

book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('onlinekahbar', cell_overwrite_ok=True)
sheet.write(0, 0, 'title')
sheet.write(0, 1, 'summary')
sheet.write(0, 2, 'published_time')
sheet.write(0, 3, 'text')


def fetch_with_catch(url, headers, timeout=30):
    try:
        resp = requests.get(url, headers=headers, timeout=30)
        return resp
    except Exception as e:
        print(f"[get error] {e} {url}")
        return None


def save_to_excel(soup):
    global n
    try:
        title = soup.find(class_='article-header-title').get_text()
        summary = soup.find(class_='article-header-abstract').get_text()
        published_time = soup.find(class_='date-only').get_text()
        texts = soup.find(class_='article-content').find_all('p')
        print(f'obtain: {title}  published time: {published_time}')
        sheet.write(n, 0, title)
        sheet.write(n, 1, summary)
        sheet.write(n, 2, published_time)
        sheet.write(n, 3, ' '.join([text.get_text() for text in texts]))
        n += 1
    except Exception as e:
        print(f"[save_to_excel error] {e}")


headers = {
    "User-Agent": "Mozilla/5.0"
}

if __name__ == '__main__':

    page = 42  # collected on Oct 30, 2025
    n = 1
    max_try = 3

    while page <= 82:
        url = f'https://www.irishcentral.com/topic/irish-politics?page={page}'

        # visit the link
        for i in range(max_try):
            resp = fetch_with_catch(url, headers=headers)
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
                class_='section-partial-list').find_all(class_='article-partial')
        except Exception as e:
            print(f"[element error] {e}")
            break
        if not items:
            break

        # traverse each link
        links = []
        for item in items:
            link = 'https://www.irishcentral.com' + item.find('a')['href']
            links.append(link)

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

    book.save('../data/ir_al.xls')
    print("bingo!")
