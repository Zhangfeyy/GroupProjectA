import pandas as pd

np_al = pd.read_csv('./data/marked/classified_np_al.csv')
np_ms = pd.read_csv('./data/marked/classified_np_ms.csv')
ir_al = pd.read_csv('./data/marked/classified_ir_al.csv')
ir_ms = pd.read_csv('./data/marked/classified_ir_ms.csv')
np_mp = pd.read_csv('./data/mp_list/cleaned_np_mp.csv')
ir_mp = pd.read_csv('./data/mp_list/cleaned_ir_mp.csv')

print("np_al statistic")
print(np_al[['female', 'male']].describe())
print("**********************************************************")

print("np_ms statistic")
print(np_ms[['female', 'male']].describe())
print("**********************************************************")

print("ir_al statistic")
print(ir_al[['female', 'male']].describe())
print("**********************************************************")

print("ir_ms statistic")
print(ir_ms[['female', 'male']].describe())
print("**********************************************************")

print("np_mp statistic")
print(np_mp['gender'].describe())
print(np_mp['gender'].value_counts(normalize=True))
print("**********************************************************")

print("ir_mp statistic")
print(ir_mp['gender'].describe())
print(ir_mp['gender'].value_counts(normalize=True))
print("**********************************************************")

'''
np_al statistic
           female        male
count  311.000000  311.000000
mean     0.019293    0.061093
std      0.137773    0.239887
min      0.000000    0.000000
25%      0.000000    0.000000
50%      0.000000    0.000000
75%      0.000000    0.000000
max      1.000000    1.000000
**********************************************************
np_ms statistic
            female         male
count  2895.000000  2895.000000
mean      0.017962     0.059067
std       0.132836     0.235791
min       0.000000     0.000000
25%       0.000000     0.000000
50%       0.000000     0.000000
75%       0.000000     0.000000
max       1.000000     1.000000
**********************************************************
ir_al statistic
           female        male
count  396.000000  396.000000
mean     0.212121    0.674242
std      0.409327    0.469250
min      0.000000    0.000000
25%      0.000000    0.000000
50%      0.000000    1.000000
75%      0.000000    1.000000
max      1.000000    1.000000
**********************************************************
ir_ms statistic
            female         male
count  1755.000000  1755.000000
mean      0.343590     0.681481
std       0.475041     0.466035
min       0.000000     0.000000
25%       0.000000     0.000000
50%       0.000000     1.000000
75%       1.000000     1.000000
max       1.000000     1.000000
**********************************************************
np_mp statistic
count     59
unique     2
top        M
freq      37
Name: gender, dtype: object
gender
M    0.627119
F    0.372881
Name: proportion, dtype: float64
**********************************************************
ir_mp statistic
count     160
unique      2
top         M
freq      124
Name: gender, dtype: object
gender
M    0.775
F    0.225
Name: proportion, dtype: float64
**********************************************************
'''