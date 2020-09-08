import pandas as pd

prod_df = pd.read_csv('top50_prod_info.csv')
top50_df = pd.read_csv('top50.csv')
inv_df = pd.read_csv('target_inv_info.csv')
sale_df = pd.read_csv('target_sale_info.csv')
holiday_df = pd.read_csv('holiday_info.csv')
target_skcs = []
prod_skcs = []
for item in top50_df.loc[:, 'skc']:
    target_skcs.append(item)
for item in prod_df.loc[:, 'skc']:
    prod_skcs.append(item)


def convert_date(df):
    df['date_rcd'] = pd.to_datetime((df['date_rcd']))
    df.set_index('skc', inplace=True)


result = []
for i in range(200):
    result.append({})
convert_date(inv_df)
convert_date(sale_df)
prod_df.set_index('skc', inplace=True)
skc_flag = 0


def handle_ie(df, date1, date2, fest):
    ie_sum = 0
    ie_flag = 0
    for line in df.itertuples():
        if (line[1] >= pd.to_datetime(date1)) & (line[1] <= pd.to_datetime(date2)):
            ie_sum += line[2]
            ie_flag += 1
    result[4 * skc_flag + fest]['skc'] = skc
    result[4 * skc_flag + fest]['ie'] = ie_sum / ie_flag


def handle_discount(df, date1, date2, fest):
    real_cost_sum = 0
    discount_flag = 0
    if skc in prod_skcs:
        for line in df.itertuples():
            if (line[1] >= pd.to_datetime(date1)) & (line[1] <= pd.to_datetime(date2)):
                real_cost_sum += line[3]
                discount_flag += line[2]
        if discount_flag != 0:
            result[4 * skc_flag + fest]['discount'] = real_cost_sum / discount_flag / prod_df.loc[skc].tag_price
        else:
            result[4 * skc_flag + fest]['discount'] = 'None'
    else:
        result[4 * skc_flag + fest]['discount'] = 'None'


def handle_fashion_level():
    if skc in prod_skcs:
        for i in range(4):
            result[4 * skc_flag + i]['fashion_level'] = 2018 - prod_df.loc[skc].year_id
    else:
        for i in range(4):
            result[4 * skc_flag + i]['fashion_level'] = 'None'


def handle_sales_volume(df, date1, date2, fest):
    s_sum = 0
    for line in df.itertuples():
        if (line[1] >= pd.to_datetime(date1)) & (line[1] <= pd.to_datetime(date2)):
            s_sum += line[2]
    result[4 * skc_flag + fest]['s'] = s_sum


for skc in target_skcs:
    inv_df_section = inv_df.loc[skc]
    sale_df_section = sale_df.loc[skc]
    handle_ie(inv_df_section, '2018-10-1 00:00:00', '2018-10-7 00:00:00', 0)
    handle_ie(inv_df_section, '2018-12-30 00:00:00', '2019-01-01 23:59:59', 1)
    handle_ie(inv_df_section, '2018-11-11 00:00:00', '2018-11-11 23:59:59', 2)
    handle_ie(inv_df_section, '2018-12-12 00:00:00', '2018-12-12 23:59:59', 3)
    handle_discount(sale_df_section, '2018-10-1 00:00:00', '2018-10-7 00:00:00', 0)
    handle_discount(sale_df_section, '2018-12-30 00:00:00', '2019-01-01 23:59:59', 1)
    handle_discount(sale_df_section, '2018-11-11 00:00:00', '2018-11-11 23:59:59', 2)
    handle_discount(sale_df_section, '2018-12-12 00:00:00', '2018-12-12 23:59:59', 3)
    handle_fashion_level()
    handle_sales_volume(sale_df_section, '2018-10-1 00:00:00', '2018-10-7 00:00:00', 0)
    handle_sales_volume(sale_df_section, '2018-12-30 00:00:00', '2019-01-01 23:59:59', 1)
    handle_sales_volume(sale_df_section, '2018-11-11 00:00:00', '2018-11-11 23:59:59', 2)
    handle_sales_volume(sale_df_section, '2018-12-12 00:00:00', '2018-12-12 23:59:59', 3)
    skc_flag += 1
output_df = pd.DataFrame(result)
output_df.to_csv('result.csv')
