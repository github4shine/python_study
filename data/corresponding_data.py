import pandas as pd

df_code= pd.read_excel("2_资产国标码.xlsx")
df_code = df_code.drop_duplicates(["国标码"],keep="first")
df_data = pd.read_excel("社康-HRP.xls")
df_new = pd.merge(df_data,df_code,how="left",left_on="新编码",right_on="国标码")
s_code = df_new.资产类型
s_name = df_new.类型名称
s_gcode = df_new.国标码
s_gname = df_new.国标码名称
df_new = df_new.drop('资产类型',axis=1)
df_new = df_new.drop('类型名称',axis=1)
df_new = df_new.drop('国标码',axis=1)
df_new = df_new.drop('国标码名称',axis=1)
s_code = '0' + s_code.astype(str)
s_code = s_code.str.rstrip('.0')

df_new.insert(1,"类型名称",s_name)
df_new.insert(1,"资产类型",s_code)
df_new.insert(1,"国标码名称",s_gname)
df_new.insert(1,"国标码",s_gcode)
writer = pd.ExcelWriter("社康-HRP-merge.xlsx")
df_new.to_excel(writer,sheet_name = "data",index=None) #导出成excel
writer.save()
