import pandas as pd
from IPython.display import display
# ファイルやディレクトリを操作するための標準ライブラリ
import os

# スクリプトと同じフォルダにあるファイル名を指定
file_name = "/Users/fuchikota/Lecture/dspro2/sql課題/winequality-red.csv"


# pandasを使ってデータを読み込む
df = pd.read_csv(file_name)

# ファイルの5行目から10行目のみを表示する
print(df[5:11])

# より見やすくするために表形式で表示
df = pd.DataFrame(df)
display(df[5:11])




