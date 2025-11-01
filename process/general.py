import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import re


def combine(*args):
    data = pd.concat([arg for arg in args],
                     ignore_index=True)  # rearrange the index
    return data


def check(data):
    # basic info: shape/dtypes
    print("basic info")
    print(data.info())

    # the first rows
    print("check the first row")
    print(data.head(1))

    # all the cols
    print("check the columns")
    print(data.columns)


def clean_html(text):
    if pd.isna(text):  # handle NaN values
        return text
    soup = BeautifulSoup(str(text), "html.parser")
    clean_text = soup.get_text()
    return " ".join(clean_text.split())


def clean(data):
    data = data.drop_duplicates()
    data = data.applymap(clean_html)


def extract_and_parse_date(text, year):
    # 1.replace "Sept" with "Sep"
    text = str(text).replace("Sept", "Sep")

    # 2. extract according to the most common format: Jan 01
    # alphabet(s) + space(s) + digit(s)
    match = re.search(r'([A-Za-z]+ \d{1,2})', text)
    if match:
        date_part = match.group(1)
        date_str = f"{year} {date_part}"
        # abbreviation or full-spelling
        for fmt in ("%Y %b %d", "%Y %B %d"):
            try:
                return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
            except ValueError:
                continue
    return None

# directly operate on the original df


def generate_date(data, col):
    data['date'] = data[col].apply(lambda x: extract_and_parse_date(x, 2024))


if __name__ == "__main__":
    data = pd.read_excel('./data/ireland_ms.xls')

    check(data)

    clean(data)

    check(data)

    generate_date(data, "published_time")
    check(data)

    data.to_csv('ireland_ms.csv', encoding="utf-8-sig", index=False)
