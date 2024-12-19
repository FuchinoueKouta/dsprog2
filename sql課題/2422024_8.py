import pandas as pd
from IPython.display import display
# ファイルやディレクトリを操作するための標準ライブラリ
import os

# スクリプトと同じフォルダにあるファイル名を指定
file_name = "/Users/fuchikota/Lecture/dspro2/sql課題/winequality-red.csv"

# ファイルを読み込む
df = pd.read_csv(file_name)

# "quality" が 6 以上のデータを抽出して、高い順に並べる
df = df[df['quality'] >= 6].sort_values(by='quality', ascending=False)

# 表形式で表示
display(df)
