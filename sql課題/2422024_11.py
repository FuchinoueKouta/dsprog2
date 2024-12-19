import pandas as pd
import numpy as np

# 使用するデータをそれぞれに分けて読み込む
users = pd.read_csv("/Users/fuchikota/Lecture/dspro2/sql課題/users.csv")
orders = pd.read_csv("/Users/fuchikota/Lecture/dspro2/sql課題/orders.csv")
items = pd.read_csv("/Users/fuchikota/Lecture/dspro2/sql課題/items.csv")

# 購入金額を算出するために、ordersとitemsを結合する
orders_items = pd.merge(orders, items, on='item_id')
orders_items['total_price'] = orders_items['item_price'] * orders_items['order_num']

# 各ユーザーの平均購入金額を算出
user_means = orders_items.groupby('user_id')['total_price'].mean()

# 最も高い平均購入金額を持つユーザーを取得
max_user = user_means.idxmax()
max_avg_price = user_means.max()

# 結果を出力（user_id と 平均購入金額）
print([max_user, max_avg_price])