import pandas as pd

target_tc_code_df = pd.read_csv('top10.csv')
sale_df_2018 = pd.read_csv('2018_sale_info.csv')
sale_df_2019 = pd.read_csv('2019_sale_info.csv')
prod_df = pd.read_csv('prod_info.csv')
prod_df.set_index('tiny_class_code', inplace=True)
sale_skc_2018 = []
sale_skc_2019 = []
target_skc_code = []
result = []
for line in sale_df_2018.itertuples():
    sale_skc_2018.append(line[1])
sale_df_2018['date_rcd'] = pd.to_datetime((sale_df_2018['date_rcd']))
sale_df_2018.set_index('skc', inplace=True, drop=False)
for line in sale_df_2019.itertuples():
    sale_skc_2019.append(line[1])
sale_df_2019['date_rcd'] = pd.to_datetime((sale_df_2019['date_rcd']))
sale_df_2019.set_index('skc', inplace=True, drop=False)
target_tc_code = []
for code in target_tc_code_df.itertuples():
    target_tc_code.append(code[1])
for tc_code in target_tc_code:
    for line in prod_df.loc[tc_code].itertuples():
        target_skc_code.append(line[1])
target_skc_code_2018 = set(target_skc_code) & set(sale_skc_2018)
target_skc_code_2019 = set(target_skc_code) & set(sale_skc_2019)
for skc in target_skc_code_2018:
    sale_df_section = sale_df_2018.loc[skc]
    sale_df_section.reindex()
    if type(sale_df_section) == type(sale_df_2018):
        weeks = []
        week_flag = 0
        sale_df_section.set_index('date_rcd', inplace=True)
        for week in sale_df_section.index.week:
            weeks.append(week)
        weeks = sorted(list(set(weeks)))
        for s_sum in sale_df_section.groupby(sale_df_section.index.week).s.sum():
            result.append({'skc':skc,'s':s_sum,'weed_flag':weeks[week_flag],'year_flag':2018})
            week_flag += 1
    else:
        print(sale_df_section)
        # result.append({'skc':skc,'s':sale_df_section})
# for skc in target_skc_code_2019:
#     sale_df_section = sale_df_2019.loc[skc]
#     sale_df_section.reindex()
#     if type(sale_df_section) == type(sale_df_2019):
#         weeks = []
#         week_flag = 0
#         sale_df_section.set_index('date_rcd', inplace=True)
#         for week in sale_df_section.index.week:
#             weeks.append(week)
#         weeks = sorted(list(set(weeks)))
#         for s_sum in sale_df_section.groupby(sale_df_section.index.week).s.sum():
#             result.append({'skc':skc,'s':s_sum,'week_flag':weeks[week_flag],'year_flag':2019})
#             week_flag += 1
# pd.DataFrame(result).to_csv('result3.csv',index=False)