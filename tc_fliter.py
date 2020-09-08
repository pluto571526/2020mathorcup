import pandas as pd

sale_df = pd.read_csv('sale_info.csv')
target_tc_code_df = pd.read_csv('top10.csv')
prod_df = pd.read_csv('prod_info.csv')
prod_df.set_index('tiny_class_code', inplace=True)
sale_skc = []
for line in sale_df.itertuples():
    sale_skc.append(line[1])
sale_df['date_rcd'] = pd.to_datetime((sale_df['date_rcd']))
sale_df.set_index('skc', inplace=True)
sale_skc = set(sale_skc)
target_tc_code = []
result = []
for i in range(240):
    result.append({})
for code in target_tc_code_df.itertuples():
    target_tc_code.append(code[1])


def time_filter(df, date1, date2):
    a = 0
    if type(df) == type(sale_df):
        for line in df.itertuples():
            if (line[1] >= pd.to_datetime(date1)) & (line[1] <= pd.to_datetime(date2)):
                a += line[2]
    else:
        if (df[0] >= pd.to_datetime(date1)) & (df[0] <= pd.to_datetime(date2)):
            a += df[1]
    return a


tc_flag = 0
for tc_code in target_tc_code:
    prod_df_section = prod_df.loc[tc_code]
    s_sum = []
    for i in range(24):
        s_sum.append(0)
    for line in prod_df_section.itertuples():
        if line[1] in sale_skc:
            sale_df_section = sale_df.loc[line[1]]
            s_sum[0] += time_filter(sale_df_section, '2018-1-1 00:00:00', '2018-1-31 00:00:00')
            s_sum[1] += time_filter(sale_df_section, '2018-2-1 00:00:00', '2018-2-27 00:00:00')
            s_sum[2] += time_filter(sale_df_section, '2018-3-1 00:00:00', '2018-3-31 00:00:00')
            s_sum[3] += time_filter(sale_df_section, '2018-4-1 00:00:00', '2018-4-30 00:00:00')
            s_sum[4] += time_filter(sale_df_section, '2018-5-1 00:00:00', '2018-5-31 00:00:00')
            s_sum[5] += time_filter(sale_df_section, '2018-6-1 00:00:00', '2018-6-30 00:00:00')
            s_sum[6] += time_filter(sale_df_section, '2018-7-1 00:00:00', '2018-7-31 00:00:00')
            s_sum[7] += time_filter(sale_df_section, '2018-8-1 00:00:00', '2018-8-31 00:00:00')
            s_sum[8] += time_filter(sale_df_section, '2018-9-1 00:00:00', '2018-9-30 00:00:00')
            s_sum[9] += time_filter(sale_df_section, '2018-10-1 00:00:00', '2018-10-31 00:00:00')
            s_sum[10] += time_filter(sale_df_section, '2018-11-1 00:00:00', '2018-11-30 00:00:00')
            s_sum[11] += time_filter(sale_df_section, '2018-12-1 00:00:00', '2018-12-31 00:00:00')
            s_sum[12] += time_filter(sale_df_section, '2019-1-1 00:00:00', '2019-1-31 00:00:00')
            s_sum[13] += time_filter(sale_df_section, '2019-2-1 00:00:00', '2019-2-27 00:00:00')
            s_sum[14] += time_filter(sale_df_section, '2019-3-1 00:00:00', '2019-3-31 00:00:00')
            s_sum[15] += time_filter(sale_df_section, '2019-4-1 00:00:00', '2019-4-30 00:00:00')
            s_sum[16] += time_filter(sale_df_section, '2019-5-1 00:00:00', '2019-5-31 00:00:00')
            s_sum[17] += time_filter(sale_df_section, '2019-6-1 00:00:00', '2019-6-30 00:00:00')
            s_sum[18] += time_filter(sale_df_section, '2019-7-1 00:00:00', '2019-7-31 00:00:00')
            s_sum[19] += time_filter(sale_df_section, '2019-8-1 00:00:00', '2019-8-31 00:00:00')
            s_sum[20] += time_filter(sale_df_section, '2019-9-1 00:00:00', '2019-9-30 00:00:00')
            s_sum[21] += time_filter(sale_df_section, '2019-10-1 00:00:00', '2019-10-31 00:00:00')
            s_sum[22] += time_filter(sale_df_section, '2019-11-1 00:00:00', '2019-11-30 00:00:00')
            s_sum[23] += time_filter(sale_df_section, '2019-12-1 00:00:00', '2019-12-31 00:00:00')
    for i in range(24):
        result[tc_flag * 24 + i]['s'] = s_sum[i]
        result[tc_flag * 24 + i]['month'] = i
        result[tc_flag * 24 + i]['tc_code'] = tc_code
    tc_flag += 1
pd.DataFrame(result).to_csv('result2.csv',index=None)
