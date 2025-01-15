import pandas as pd

# 读取Excel文件并将每行数据作为字典返回
def get_all_rows(file_path):
    df = pd.read_excel(file_path,dtype=str)
    
    # 如果表格中有 '年龄' 列，将其日期格式化为 'dd/mm/yyyy'
    # if 'date' in df.columns:
    #     df['date'] = df['date'].apply(lambda x: x.strftime('%m/%d') if pd.notnull(x) else x)
    
    # 将数据转换为字典列表
    data = df.to_dict(orient='records')
    return data,len(df)

# 使用示例
# file_path = './200.xlsx'  # 替换为你的文件路径
# all_rows = get_all_rows(file_path)

# # 打印所有行
# for row in all_rows:
#     print(row)
