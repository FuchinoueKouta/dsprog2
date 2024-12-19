import pandas as pd

# ファイルを読み込む
items = pd.read_csv("/Users/fuchikota/Lecture/dspro2/sql課題/items.csv")

# item_id=101の商品情報を取得
base_item = items[items['item_id'] == 101].iloc[0]

# 他の商品情報を取得（item_id=101を除外し、コピーを作成）
other_items = items[items['item_id'] != 101].copy()

# おすすめ度を計算する関数
def calculate_score(row):
    score = 0
    # ルール1: カテゴリが近いものを優先
    if row['small_category'] == base_item['small_category']:
        score += 100  # 小カテゴリが一致
    if row['big_category'] == base_item['big_category']:
        score += 10   # 大カテゴリが一致
    
    # ルール2: 価格が近いものを優先
    price_diff = abs(row['item_price'] - base_item['item_price'])
    score -= price_diff  # 価格差が小さいほどスコアが高い

    # ルール3: ページ数が近いものを優先
    page_diff = abs(row['pages'] - base_item['pages'])
    score -= page_diff / 10  # ページ数差が小さいほどスコアが高い（重み調整）

    return score

# おすすめ度を計算して追加（警告が出た場合は解消する）
other_items.loc[:, 'score'] = other_items.apply(calculate_score, axis=1)

# 推薦候補の上位3件を取得
top_recommendations = other_items.sort_values(by='score', ascending=False).head(3)

# 推薦候補を指定された形式で出力
print(top_recommendations['item_id'].tolist())