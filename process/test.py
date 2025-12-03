import pandas as pd
from process import mark_names,accuracy
from process.helpers import clean, check, concatenate_cols


df_man = pd.read_csv('./data/sample_man.csv')
df_sample = pd.read_csv('./data/sample_test.csv')

if __name__ == '__main__':
        # check(news_df)
        # check(name_df)
        
        # news_df= clean(news_df)
        # name_df = clean(name_df)
        
        # check(news_df)
        # check(name_df)
        
        # news_df['female'] = 0
        # news_df['male'] = 0
        
        # news_df = mark_names(news_df,name_df,'text','female','male','name','gender')
        
        # name_df = concatenate_cols(name_df, 'First Name', 'Surname', 'name', ' ')
        # name_df = name_df.drop(columns=['First Name', 'Surname'], errors='ignore')
        
        # name_df.to_csv('./data/ir_mp_cleaned.csv',index=False)
        # name_df.to_csv('./data/np_mp_cleaned.csv',index=False)
        # news_df.to_csv('./data/sample_test.csv',index=False)
        
        print(f"female accuracy: {accuracy(df_man,'f_mp_incl','female',df_sample)}") # 100%
        print(f"male accuracy: {accuracy(df_man,'m_mp_incl','male',df_sample)}") # 87.5%
        
