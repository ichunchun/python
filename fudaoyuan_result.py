import pandas as pd

def fudaoyuan_result():
    
    excel1 = pd.read_excel("excel/excel1.xlsx")
    excel2 = pd.read_excel("excel/excel2.xlsx")
    excel3 = pd.read_excel("excel/excel3.xlsx")
    excel4 = pd.read_excel("excel/excel4.xlsx")
    excel5 = pd.read_excel("excel/excel5.xlsx")
    excel6 = pd.read_excel("excel/excel6.xlsx")
    excel7 = pd.read_excel("excel/excel7.xlsx")
    excel8 = pd.read_excel("excel/excel8.xlsx")


    # 合并三个Excel
    df = pd.concat([excel1, excel2, excel3, excel4, excel5, excel6, excel7, excel8])

    # 取出Q1列,并去重,得到所有辅导员名字
    names = df["Q1.我的辅导员是"].unique()

    result = []
    for name in names:
        # 过滤出名字为name的记录
        df_name = df[df["Q1.我的辅导员是"] == name]

        # 取出Q2,Q3,Q4,Q5列,并去掉"分"字
        q2 = df_name["Q2.政治素养"].str.replace("分", "").astype(int)
        q3 = df_name["Q3.道德品质"].str.replace("分", "").astype(int)
        q4 = df_name["Q4.管理能力"].str.replace("分", "").astype(int)
        q5 = df_name["Q5.解决问题"].str.replace("分", "").astype(int)

        q2_mean = round(q2.mean(), 2)
        q3_mean = round(q3.mean(), 2)
        q4_mean = round(q4.mean(), 2)
        q5_mean = round(q5.mean(), 2)
        q6 = len(df_name["Q2.政治素养"])
        means = [q2_mean, q3_mean, q4_mean, q5_mean, q6]
        # 存入结果list
        result.append({"name": name, "means": means})

    result_df = pd.DataFrame(result)
    result_df.columns = ["name", "means"]

    result_df["q2_mean"] = result_df["means"].apply(lambda x: x[0])
    result_df["q3_mean"] = result_df["means"].apply(lambda x: x[1])
    result_df["q4_mean"] = result_df["means"].apply(lambda x: x[2])
    result_df["q5_mean"] = result_df["means"].apply(lambda x: x[3])
    result_df["q6"] = result_df["means"].apply(lambda x: x[4])

    result_df.drop("means", axis=1, inplace=True)

    result_df.columns = ["姓名", "政治素养", "道德品质", "管理能力", "解决问题", "测评人数"]
    result_df["平均数"] = round(result_df[["政治素养", "道德品质", "管理能力", "解决问题"]].mean(axis=1), 2)

    result_df.to_excel("result.xlsx")

