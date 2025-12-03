import pandas as pd
from process.helpers import check

np_al = pd.read_csv("./data/marked/classified_np_al.csv")
np_ms = pd.read_csv("./data/marked/classified_np_ms.csv")
ir_al = pd.read_csv("./data/marked/classified_ir_al.csv")
ir_ms = pd.read_csv("./data/marked/classified_ir_ms.csv")

# or cannot be used in pandas indexing
gender_np_al = np_al[(np_al["female"] == 1) | (np_al["male"] == 1)]
gender_np_ms = np_ms[(np_ms["female"] == 1) | (np_ms["male"] == 1)]
gender_ir_al = ir_al[(ir_al["female"] == 1) | (ir_al["male"] == 1)]
gender_ir_ms = ir_ms[(ir_ms["female"] == 1) | (ir_ms["male"] == 1)]


print("filtered np_al************************************************************")
check(gender_np_al)
print("**************************************************************************\n")

print("filtered np_ms************************************************************")
check(gender_np_ms)
print("**************************************************************************\n")

print("filtered ir_al************************************************************")
check(gender_ir_al)
print("**************************************************************************\n")

print("filtered ir_ms************************************************************")
check(gender_ir_ms)
print("**************************************************************************\n")

gender_ir_al.to_csv("./data/filtered/gender_ir_al.csv",index=False)
gender_ir_ms.to_csv("./data/filtered/gender_ir_ms.csv",index=False)
gender_np_al.to_csv("./data/filtered/gender_np_al.csv",index=False)
gender_np_ms.to_csv("./data/filtered/gender_np_ms.csv",index=False)

'''
filtered np_al************************************************************
basic info
<class 'pandas.core.frame.DataFrame'>
Index: 22 entries, 0 to 306
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   date     22 non-null     object
 1   content  22 non-null     object
 2   female   22 non-null     int64 
 3   male     22 non-null     int64 
dtypes: int64(2), object(2)
memory usage: 880.0+ bytes
None
check the first row
       date                                            content  female  male
0  2024/1/1  House panel ask govt to investigate Minister o...       0     1
check the columns
Index(['date', 'content', 'female', 'male'], dtype='object')
**************************************************************************

filtered np_ms************************************************************
basic info
<class 'pandas.core.frame.DataFrame'>
Index: 198 entries, 3 to 2877
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   date     198 non-null    object
 1   content  198 non-null    object
 2   female   198 non-null    int64
 3   male     198 non-null    int64
dtypes: int64(2), object(2)
memory usage: 7.7+ KB
None
check the first row
       date                                            content  female  male
3  2024/1/1  Home ministry acknowledges weakness in Balkuma...       0     1
check the columns
Index(['date', 'content', 'female', 'male'], dtype='object')
**************************************************************************

filtered ir_al************************************************************
basic info
<class 'pandas.core.frame.DataFrame'>
Index: 294 entries, 1 to 394
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   date     294 non-null    object
 1   content  294 non-null    object
 2   female   294 non-null    int64
 3   male     294 non-null    int64
dtypes: int64(2), object(2)
memory usage: 11.5+ KB
None
check the first row
        date                                            content  female  male
1  2024/1/10  Irish LGBTQI+ groups steadfastly support surro...       0     1
check the columns
Index(['date', 'content', 'female', 'male'], dtype='object')
**************************************************************************

filtered ir_ms************************************************************
basic info
<class 'pandas.core.frame.DataFrame'>
Index: 1320 entries, 0 to 1754
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   date     1320 non-null   object
 1   content  1320 non-null   object
 2   female   1320 non-null   int64
 3   male     1320 non-null   int64
dtypes: int64(2), object(2)
memory usage: 51.6+ KB
None
check the first row
       date                                            content  female  male
0  2024/1/1  Leo Varadkar says he is not changing his life ...       0     1
check the columns
Index(['date', 'content', 'female', 'male'], dtype='object')
**************************************************************************
'''