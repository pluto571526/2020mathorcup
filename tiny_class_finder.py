import pandas as pd

prod_df = pd.read_csv('prod_info.csv')
sale_df = pd.read_csv('filtered_sale_info_2.csv')
prod_df.set_index('tiny_class_code', inplace=True)
sale_df.set_index('skc', inplace=True)
tiny_class_code = set(prod_df.index)
sale_skc = set(sale_df.index)
data_sum = {}
target_tc_code = []
for tc_code in tiny_class_code:
    prod_df_section = prod_df.loc[tc_code]
    cost_sum = 0
    if tc_code != 27248400:
        for line in prod_df_section.itertuples():
            skc = line[1]
            if skc in sale_skc:
                cost_sum += sale_df.loc[skc, 'real_cost'].sum()
    else:
        skc = prod_df_section[0]
        cost_sum = sale_df.loc[skc, 'real_cost'].sum()
    data_sum[tc_code] = cost_sum
data_sorted = sorted(data_sum.items(), key=lambda kv: (kv[1], kv[0],), reverse=True)
for i in range(10):
    target_tc_code.append(data_sorted[i][0])
top10_df = pd.DataFrame(data=target_tc_code)
top10_df.to_csv('top10.csv',index=False)
