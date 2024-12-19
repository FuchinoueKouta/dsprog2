import pandas as pd
from IPython.display import display
# ファイルやディレクトリを操作するための標準ライブラリ
import os

# スクリプトと同じフォルダにあるファイル名を指定
file_name = "/Users/fuchikota/Lecture/dspro2/sql課題/winequality-red.csv"

# ファイルを読み込む
df = pd.read_csv(file_name)

# "quality" ごとの平均を計算
quality_means = df.groupby('quality').mean()

# 表形式で結果を表示
display(quality_means)
