import pandas as pd

inv_df = pd.read_csv('top50_inv_info.csv')
sale_df = pd.read_csv('top50_sale_info.csv')
holiday_df = pd.read_csv('holiday_info.csv')


def convert_date(df):
    df['date_rcd'] = pd.to_datetime((df['date_rcd']))
    df.set_index('date_rcd', inplace=True)


convert_date(inv_df)
convert_date(sale_df)

holiday_df.set_index('fest_name', inplace=True)
target_date = holiday_df.loc[('国庆节', '元旦', '双十一', '双十二'), ('date_fest_start', 'date_fest_end')]


def filter_date(df):
    target_list = []  # 创建一个空数组
    for line in target_date.itertuples():
        target_list.append(df[line[1]:line[2]])
    return pd.concat(target_list)


filter_date(inv_df).to_csv('target_inv_info.csv')
filter_date(sale_df).to_csv('target_sale_info.csv')
