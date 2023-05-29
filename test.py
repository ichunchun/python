import pandas as pd

# 读取文件1
df1 = pd.read_excel('文件1.xlsx')

# 读取文件2
df2 = pd.read_excel('文件2.xlsx')

# 使用"姓名"列来对齐两个DataFrame的数据
merged_df = df2.merge(df1, left_on='姓名', right_on='姓名')

# 保存合并后的结果到新的Excel文件
merged_df.to_excel('合并结果.xlsx', index=False)
