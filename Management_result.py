import pandas as pd


def management_result(excel_path):
    # 一定要删除最后的无用列，列一定是5的倍数，因为每人5列
    df = pd.read_excel(excel_path)

    def get_avg(df):
        result = []
        temp = []

        for col in df.columns:
            df[col] = df[col].str.replace("分", "").astype(float)
            avg = round(df[col].mean(), 2)  # 保留2位小数
            temp.append(avg)

            if len(temp) == 4:
                result.append(temp)
                temp = []

        if len(temp) > 0:
            result.append(temp)
        return result

    avg_list = get_avg(df)

    # print(avg_list)

    def get_names(df):
        name_list = []
        for i in range(0, len(df.columns), 4):
            name = df.columns[i]
            name_list.append(name)
        return name_list

    names = get_names(df)
    # print(names)
    result = {}
    for i in range(len(names)):
        result[names[i]] = avg_list[i]

    # print(result)

    df1 = pd.DataFrame.from_dict(result, orient="index")
    df1.columns = ["办事水平", "部门协同", "服务能力", "纪律意识"]

    df1["平均数"] = round(df1[["办事水平", "部门协同", "服务能力", "纪律意识"]].mean(axis=1), 2)
    df1["测评人数"] = len(df)
    df1.to_excel("管理部门结果评测.xlsx")
