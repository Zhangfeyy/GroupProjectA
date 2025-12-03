import pandas as pd
from process.helpers import check

np_al = pd.read_csv("./data/marked/classified_np_al.csv")
np_ms = pd.read_csv("./data/marked/classified_np_ms.csv")
ir_al = pd.read_csv("./data/marked/classified_ir_al.csv")
ir_ms = pd.read_csv("./data/marked/classified_ir_ms.csv")

# or cannot be used in pandas indexing
f_np_al = np_al[(np_al["female"] == 1) & (np_al["male"] == 0)]
m_np_al = np_al[(np_al["female"] == 0) & (np_al["male"] == 1)]
f_np_ms = np_ms[(np_ms["female"] == 1) & (np_ms["male"] == 0)]
m_np_ms = np_ms[(np_ms["female"] == 0) & (np_ms["male"] == 1)]
f_ir_ms = ir_ms[(ir_ms["female"] == 1) & (ir_ms["male"] == 0)]
m_ir_ms = ir_ms[(ir_ms["female"] == 0) & (ir_ms["male"] == 1)]
f_ir_al = ir_al[(ir_al["female"] == 1) & (ir_al["male"] == 0)]
m_ir_al = ir_al[(ir_al["female"] == 0) & (ir_al["male"] == 1)]

print("female np_al************************************************************")
check(f_np_al)
print("**************************************************************************\n")

print("male np_al************************************************************")
check(m_np_al)
print("**************************************************************************\n")

print("female np_ms************************************************************")
check(f_np_ms)
print("**************************************************************************\n")

print("male np_ms************************************************************")
check(m_np_ms)
print("**************************************************************************\n")

print("female ir_al************************************************************")
check(f_ir_al)
print("**************************************************************************\n")

print("male ir_al************************************************************")
check(m_ir_al)
print("**************************************************************************\n")

print("female ir_ms************************************************************")
check(f_ir_ms)
print("**************************************************************************\n")

print("male ir_ms************************************************************")
check(m_ir_ms)
print("**************************************************************************\n")

f_ir_al.to_csv("./data/splited/f_ir_al.csv",index=False)
m_ir_al.to_csv("./data/splited/m_ir_al.csv",index=False)
f_np_al.to_csv("./data/splited/f_np_al.csv",index=False)
m_np_al.to_csv("./data/splited/m_np_al.csv",index=False)
f_np_ms.to_csv("./data/splited/f_np_ms.csv",index=False)
m_np_ms.to_csv("./data/splited/m_np_ms.csv",index=False)
f_ir_ms.to_csv("./data/splited/f_ir_ms.csv",index=False)
m_ir_ms.to_csv("./data/splited/m_ir_ms.csv",index=False)

'''
female np_al************************************************************
basic info
<class 'pandas.core.frame.DataFrame'>
Index: 3 entries, 150 to 179
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   date     3 non-null      object
 1   content  3 non-null      object
 2   female   3 non-null      int64
 3   male     3 non-null      int64
dtypes: int64(2), object(2)
memory usage: 120.0+ bytes
None
check the first row
          date                                            content  female  male
150  2024/3/12  Narayan Dahal elected chairperson of the Natio...       1     0
check the columns
Index(['date', 'content', 'female', 'male'], dtype='object')
**************************************************************************

male np_al************************************************************
basic info
<class 'pandas.core.frame.DataFrame'>
Index: 16 entries, 0 to 306
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   date     16 non-null     object
 1   content  16 non-null     object
 2   female   16 non-null     int64
 3   male     16 non-null     int64
dtypes: int64(2), object(2)
memory usage: 640.0+ bytes
None
check the first row
       date                                            content  female  male
0  2024/1/1  House panel ask govt to investigate Minister o...       0     1
check the columns
Index(['date', 'content', 'female', 'male'], dtype='object')
**************************************************************************

female np_ms************************************************************
basic info
<class 'pandas.core.frame.DataFrame'>
Index: 27 entries, 164 to 2567
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   date     27 non-null     object
 1   content  27 non-null     object
 2   female   27 non-null     int64
 3   male     27 non-null     int64
dtypes: int64(2), object(2)
memory usage: 1.1+ KB
None
check the first row
          date                                            content  female  male
164  2024/1/25  UML candidate Koirala elected as National Asse...       1     0
check the columns
Index(['date', 'content', 'female', 'male'], dtype='object')
**************************************************************************

male np_ms************************************************************
basic info
<class 'pandas.core.frame.DataFrame'>
Index: 146 entries, 3 to 2877
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   date     146 non-null    object
 1   content  146 non-null    object
 2   female   146 non-null    int64
 3   male     146 non-null    int64
dtypes: int64(2), object(2)
memory usage: 5.7+ KB
None
check the first row
       date                                            content  female  male
3  2024/1/1  Home ministry acknowledges weakness in Balkuma...       0     1
check the columns
Index(['date', 'content', 'female', 'male'], dtype='object')
**************************************************************************

female ir_al************************************************************
basic info
<class 'pandas.core.frame.DataFrame'>
Index: 27 entries, 4 to 391
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   date     27 non-null     object
 1   content  27 non-null     object
 2   female   27 non-null     int64
 3   male     27 non-null     int64
dtypes: int64(2), object(2)
memory usage: 1.1+ KB
None
check the first row
        date                                            content  female  male
4  2024/1/14  Thousands gather in Dublin for "biggest Irish ...       1     0
check the columns
Index(['date', 'content', 'female', 'male'], dtype='object')
**************************************************************************

male ir_al************************************************************
basic info
<class 'pandas.core.frame.DataFrame'>
Index: 210 entries, 1 to 394
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   date     210 non-null    object
 1   content  210 non-null    object
 2   female   210 non-null    int64
 3   male     210 non-null    int64
dtypes: int64(2), object(2)
memory usage: 8.2+ KB
None
check the first row
        date                                            content  female  male
1  2024/1/10  Irish LGBTQI+ groups steadfastly support surro...       0     1
check the columns
Index(['date', 'content', 'female', 'male'], dtype='object')
**************************************************************************

female ir_ms************************************************************
basic info
<class 'pandas.core.frame.DataFrame'>
Index: 124 entries, 4 to 1750
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   date     124 non-null    object
 1   content  124 non-null    object
 2   female   124 non-null    int64
 3   male     124 non-null    int64
dtypes: int64(2), object(2)
memory usage: 4.8+ KB
None
check the first row
        date                                            content  female  male
4  2024/1/10  Proportion of single men among asylum seekers ...       1     0
check the columns
Index(['date', 'content', 'female', 'male'], dtype='object')
**************************************************************************

male ir_ms************************************************************
basic info
<class 'pandas.core.frame.DataFrame'>
Index: 717 entries, 0 to 1754
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   date     717 non-null    object
 1   content  717 non-null    object
 2   female   717 non-null    int64
 3   male     717 non-null    int64
dtypes: int64(2), object(2)
memory usage: 28.0+ KB
None
check the first row
       date                                            content  female  male
0  2024/1/1  Leo Varadkar says he is not changing his life ...       0     1
check the columns
Index(['date', 'content', 'female', 'male'], dtype='object')
**************************************************************************
'''