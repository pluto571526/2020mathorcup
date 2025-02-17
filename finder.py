import pandas as pd

df = pd.read_csv('filtered_sale_info.csv')  # 把筛选过的数据用pandas库读取到df中
inv_df = pd.read_csv("inv_info.csv")
prod_df = pd.read_csv("prod_info.csv")
pre_skc = df.loc[0, 'skc']  # 初始化，把第一个skc读入缓存
cost_sum = 0  # 初始化销售额缓存
data_sum = {}  # 初始化筛选后字典
top_50 = []
prod_skc_list = []
inv_skc_list = []
for data in df.itertuples():
    if data[1] == pre_skc:  # 判断当前的skc是否与前一项相同，相同则将销售额相加，否则存储上一项的结果并继续运算
        cost_sum += data[4]
    else:
        data_sum[pre_skc] = cost_sum
        cost_sum = data[4]
    pre_skc = data[1]


i = 0  # 设置迭代计数器
data_sorted = sorted(data_sum.items(), key=lambda kv: (kv[1], kv[0],), reverse=True)
# 将字典排序并以列表形式保存
for item in data_sorted[:50]:
    top_50.append({'skc': item[0], 'real_cost': item[1]})  # 新建列表并以列表嵌套字典的方式储存销售额前50的skc的数据
df1 = pd.DataFrame(top_50, columns=['skc', 'real_cost'])
df1.to_csv("top50.csv", index=False)  # 将数据写入本地csv文件
