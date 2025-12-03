import pandas as pd
from process.helpers import clean, check, concatenate_cols, mark_names,accuracy

np_al = pd.read_csv('./data/nepal_al.csv')
np_ms = pd.read_csv('./data/nepal_ms.csv')
ir_al = pd.read_csv('./data/ireland_al.csv')
ir_ms = pd.read_csv('./data/ireland_ms.csv')

np_mp = pd.read_csv("./data/np_mp_cleaned.csv")
ir_mp = pd.read_csv("./data/ir_mp_cleaned.csv")

# preprocess
# clean(np_al) Pnlinekhabar doesnt contain summary part
clean(np_ms)
clean(ir_al)
clean(ir_ms)

print("np_al:")
check(np_al)

print("np_ms:")
check(np_ms)

print("ir_al:")
check(ir_al)

print("ir_ms:")
check(ir_ms)

np_al = concatenate_cols(np_al,"title","summary","text", new_col="content", sep=' ')
np_al = np_al.drop(columns=["title","summary","text"],errors="ignore")
np_al = np_al.sort_values(by='date', ascending=True)

np_ms = concatenate_cols(np_ms,"title","summary","text", new_col="content", sep=' ')
np_ms = np_ms.drop(columns=["title","summary","text"],errors="ignore")
np_ms = np_ms.sort_values(by='date', ascending=True)

ir_al = concatenate_cols(ir_al,"title","summary","text", new_col="content", sep=' ')
ir_al = ir_al.drop(columns=["title","summary","text"],errors="ignore")
ir_al = ir_al.sort_values(by='date', ascending=True)

ir_ms = concatenate_cols(ir_ms,"title","summary","text", new_col="content", sep=' ')
ir_ms = ir_ms.drop(columns=["title","summary","text"],errors="ignore")
ir_ms = ir_ms.sort_values(by='date', ascending=True)

np_al = mark_names(np_al,np_mp,"content","name","gender")
np_ms = mark_names(np_ms,np_mp,"content","name","gender")
ir_al = mark_names(ir_al,ir_mp,"content","name","gender")
ir_ms = mark_names(ir_ms,ir_mp,"content","name","gender")

np_al.to_csv("./data/classified_np_al.csv",index=False)
np_ms.to_csv("./data/classified_np_ms.csv",index=False)
ir_al.to_csv("./data/classified_ir_al.csv",index=False)
ir_ms.to_csv("./data/classified_ir_ms.csv",index=False)