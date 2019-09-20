import pandas as pd

df1= pd.read_excel('d:/龙华区听书2000集.xlsx') 
df_pick1 = df1.sample(frac=0.43,replace=False,random_state=None)
print(df_pick1["书香实际集数"].sum())

writer1 = pd.ExcelWriter('d:/已选音频目录.xlsx')
df_pick1.to_excel(writer1, sheet_name='已选音频', index=False)
writer1.save()

'''
df2= pd.read_excel('d:/3.高校公图（数图）视频资源目录10755集.xlsx',sheet_name = 1) 
df_pick2 = df2.sample(n=100,replace=False,random_state=1)
writer2 = pd.ExcelWriter('d:/已选视频目录.xlsx')
df_pick2.to_excel(writer2, sheet_name='已选视频', index=False)
writer2.save()
'''