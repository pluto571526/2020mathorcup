import pandas as pd

top50_df = pd.read_csv("top50.csv")
inv_df = pd.read_csv("inv_info.csv")
sale_df = pd.read_csv("sale_info.csv")
prod_df = pd.read_csv("prod_info.csv")  # 反正数据量不大先一股脑读进来再说
data = {}  # 新建字典用于保存筛选出来的数据
target_skcs = []
for item in top50_df.loc[:, 'skc']:
    target_skcs.append(item)


# 用一个列表储存目标skc，迭代筛选出的csv数据将skc写入列表中


def filter_inv(df):  # 传入一个DataFrame格式的数据
    data_list = []
    for line in df.itertuples():
        for target_skc in target_skcs:
            if target_skc == line[1]:
                data_list.append({'skc': line[1], 'date_rcd': line[2], 'ie': line[3]})
                break

    return data_list


def filter_prod(df):  # 传入一个DataFrame格式的数据
    data_list = []
    for line in df.itertuples():
        for target_skc in target_skcs:
            if target_skc == line[1]:
                data_list.append({'skc': line[1], 'year_id': line[2], 'season_id': line[3], 'tiny_class_code': line[4]
                                     , 'tag_price': line[5]})
                break

    return data_list


def filter_sale(df):  # 传入一个DataFrame格式的数据
    data_list = []
    for line in df.itertuples():
        for target_skc in target_skcs:
            if target_skc == line[1]:
                data_list.append({'skc': line[1], 'date_rcd': line[2], 's': line[3], 'real_cost': line[4]})
                break

    return data_list


new_inv_df = pd.DataFrame(filter_inv(inv_df))
new_prod_df = pd.DataFrame(filter_prod(prod_df))
new_sale_df = pd.DataFrame(filter_sale(sale_df))
new_inv_df.to_csv('top50_inv_info.csv', index=False)
new_prod_df.to_csv('top50_prod_info.csv', index=False)
new_sale_df.to_csv('top50_sale_info.csv', index=False)
