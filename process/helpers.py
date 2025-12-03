import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import re
import numpy as np
import pandas as pd


# PROCESSING DATASETS **************************************************************

# 1. combine multiple datasets
def combine(*args):
    data = pd.concat([arg for arg in args],
                     ignore_index=True) 
    return data

# 2. check the data info 
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

# 3. clean the html text
def clean_html(text):
    if pd.isna(text):  # handle NaN values
        return text
    soup = BeautifulSoup(str(text), "html.parser")
    clean_text = soup.get_text()
    return " ".join(clean_text.split())

def clean(data):
    data = data.drop_duplicates()
    data = data.dropna()
    # strip can only work on the str type
    data.columns = data.columns.str.strip()
    data = data.map(lambda x: x.strip() if isinstance(x, str) else x)
    # data = data.applymap(clean_html)
    return data

# 4. extract the date
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

def concatenate_cols(df, *cols, new_col, sep):
    df[new_col] = df[list(cols)].astype(str).agg(sep.join,axis=1) # aggregate function
    return df
def generate_date(data, col):
    data['date'] = data[col].apply(lambda x: extract_and_parse_date(x, 2024))
    
# 5. tag genders
def mark_names(news_df, name_df, text_col, name_col, gender_col,female_col='female', male_col='male'):
        '''
        news_df: the dataset storing the corpus
                text_col: the col name of the text
                female_col: the col name of are females included?
                male_col: the col name of are males included?

        name_df: the dataset storing the MP information
                name_col: the col name of the name information
                gender_col the col name of the gender information
  
        '''
        news_df[female_col] = 0
        news_df[male_col] = 0
        for idx, row in news_df.iterrows():
                text = row[text_col]
                found = name_df[name_df[name_col].apply(lambda n: n in str(text))]
                # a subframe of name_df by boolean indexing
                news_df.at[idx, female_col] = int((found[gender_col]=='F').any())
                news_df.at[idx, male_col] = int((found[gender_col]=='M').any())
        
        return news_df

# 6. calculate the accuracy
def accuracy(df_man,label_col, pred_col,df_sample= None):
        # cannot use bool to determine
        if df_sample is None:
                df_sample = df_man
        accuracy = ((df_man[label_col]).astype(str) == (df_sample[pred_col]).astype(str)).mean()
        return accuracy

    
# PROCESS TEXTS **************************************************************

# 1. cut texts
def text_embedding(text, tokenizer,embedding_model,max_tokens):
    
    # decoded text can still be over 512 tokens, so its necessary to double check
    def split_text(text, tokenizer,max_tokens):
        tokens = tokenizer.encode(text,add_special_tokens=False) # only based on the original text
        chunks = [tokens[i:i+max_tokens] for i in range(0, len(tokens),max_tokens)] # if tokens are less than 512, it automatically ends at the last meaningful token.
        texts = []
        for chunk in chunks:
            chunk_text = tokenizer.decode(chunk)
            chunk_tokens = tokenizer.encode(chunk_text,add_special_tokens=False)
            if len(chunk_tokens) <= max_tokens:
                texts.append(chunk_text)
            else:
                sub_chunks = [chunk_tokens[i:i+max_tokens] for i in range(0, len(chunk_tokens),max_tokens)]
                for sub_chunk in sub_chunks:
                    texts.append(tokenizer.decode(sub_chunk))
        return texts
    
    chunks = split_text(text, tokenizer,max_tokens)
    embs = embedding_model.encode(chunks, show_progress_bar = True) 
    return np.mean(embs,axis=0)


if __name__ == "__main__":
    data = pd.read_excel('./data/ireland_ms.xls')

    check(data)

    clean(data)

    check(data)

    generate_date(data, "published_time")
    check(data)

    data.to_csv('ireland_ms.csv', encoding="utf-8-sig", index=False)
