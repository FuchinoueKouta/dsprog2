import pandas as pd
import numpy as np

# 使用するデータをそれぞれに分けて読み込む
users = pd.read_csv("/Users/fuchikota/Lecture/dspro2/sql課題/users.csv")
orders = pd.read_csv("/Users/fuchikota/Lecture/dspro2/sql課題/orders.csv")
items = pd.read_csv("/Users/fuchikota/Lecture/dspro2/sql課題/items.csv")

# 購入金額を算出するために、ordersとitemsを結合する
orders_items = pd.merge(orders, items, on='item_id')
orders_items['total_price'] = orders_items['item_price'] * orders_items['order_num']

# 最も大きい購入金額の行を取得
max_order = orders_items.loc[orders_items['total_price'].idxmax()]

# 結果を出力（order_id と 購入金額）
print([max_order['order_id'], max_order['total_price']])