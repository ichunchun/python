import pandas as pd

# 读取原始Excel表格
# df = pd.read_excel("2022-2023-1期末综合评教情况.xlsx", sheet_name="具体评教内容")


def creat_result(excel_path):
    def get_people():
        new_df_people = pd.DataFrame(columns=["教师", "课程名称", "应参评人数"])
        grouped = df_people.groupby(["课程名称", "教师"])
        for (course, teacher), group in grouped:
            attitude_avg = pd.to_numeric(group["应参评人数"]).sum()
            new_row = pd.DataFrame(
                [
                    [
                        teacher,
                        course,
                        attitude_avg,
                    ]
                ],
                columns=["教师", "课程名称", "应参评人数"],
            )
            new_df_people = pd.concat([new_df_people, new_row], ignore_index=True)
            
        return new_df_people
    
    df_people = pd.read_excel(excel_path, sheet_name="课程评分")[['课程名称','教师','应参评人数']]
    df = pd.read_excel(excel_path, sheet_name="具体评教内容")
    # 计算平均分并创建新的DataFrame
    new_df = pd.DataFrame(columns=["教师", "课程名称", "教学态度", "教学内容", "课堂管理", "师德师风", "相同行数"])
    grouped = df.groupby(["课程名称", "教师"])
    for (course, teacher), group in grouped:
        attitude_avg = pd.to_numeric(
            group["教学态度"].str.replace("分", ""), errors="coerce"
        ).mean()
        content_avg = pd.to_numeric(
            group["教学内容"].str.replace("分", ""), errors="coerce"
        ).mean()

        try:
            management_avg = pd.to_numeric(
                group["课堂管理"].str.replace("分", ""), errors="coerce"
            ).mean()
        except ValueError:
            management_avg = None

        ethics_avg = pd.to_numeric(
            group["师德师风"].str.replace("分", ""), errors="coerce"
        ).mean()
        row_count = len(group)

        new_row = pd.DataFrame(
            [
                [
                    teacher,
                    course,
                    attitude_avg,
                    content_avg,
                    management_avg,
                    ethics_avg,
                    row_count,
                ]
            ],
            columns=["教师", "课程名称", "教学态度", "教学内容", "课堂管理", "师德师风", "相同行数"],
        )
        new_df = pd.concat([new_df, new_row], ignore_index=True)

    # 将结果写入新的Excel文件
    new_df["教学态度"] = new_df["教学态度"].apply(
        lambda x: f"{round(x, 2)}分" if pd.notnull(x) else ""
    )
    new_df["教学内容"] = new_df["教学内容"].apply(
        lambda x: f"{round(x, 2)}分" if pd.notnull(x) else ""
    )
    new_df["课堂管理"] = new_df["课堂管理"].apply(
        lambda x: f"{round(x, 2)}分" if pd.notnull(x) else ""
    )
    new_df["师德师风"] = new_df["师德师风"].apply(
        lambda x: f"{round(x, 2)}分" if pd.notnull(x) else ""
    )


    new_df_p=get_people()
    merged_df = new_df.merge(new_df_p, on=['教师', '课程名称'])
    merged_df.to_excel("教师结果评测.xlsx", index=False)
    # new_df.to_excel("教师结果评测_1.xlsx", index=False)

# def check_code(excel_path):
#     df = pd.read_excel(excel_path)
#     temp_list = [
#         "0分",
#         "5分",
#         "10分",
#         "15分",
#         "20分",
#         "25分",
#         "30分",
#         "35分",
#         "40分",
#         "45分",
#         "50分",
#         "55分",
#         "60分",
#         "65分",
#         "70分",
#         "75分",
#         "80分",
#         "85分",
#         "90分",
#         "95分",
#         "100分",
#     ]
#
#     for i, row in df.loc[:, ["教学态度", "教学内容", "课堂管理", "师德师风"]].iterrows():
#         for j, value in enumerate(row):
#             # 如果单元格的值不是字符串类型，则跳过
#             if not isinstance(value, str):
#                 print(f"第{i + 1}行，第{j + 1}列单元格的值不是字符串类型")
#                 continue
#             # 检查单元格的值是否包含乱码
#             if value not in temp_list:
#                 # 如果包含乱码，则输出单元格的行和列
#                 print(f"乱码出现在第{i + 1}行，第{j + 1}列，单元格的值为：{value}")

# if __name__ == "__main__":
#     creat_result("1.xlsx")