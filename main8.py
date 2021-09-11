from logging import lastResort
from typing import List
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from streamlit.proto.Button_pb2 import Button
import time

st.title('レイアウト')

st.write('プログレスバーの表示')
'スタート'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)


'終了'

left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ１')
expander1.write('問い合わせ１の回答')
expander2 = st.expander('問い合わせ２')
expander2.write('問い合わせ２の回答')

# if st.checkbox('表示する場合はチェックを入れる'):
#     img = Image.open('hana.jpg')
#     st.image(img, caption='古代ハス' , use_column_width=True)

# st.write('セレクトボックス')
# optin = st.selectbox(
#     'あなたの好きな数字を選んでください',
#     list(range(1,11))
# )
# 'あなたの好きな数字は' , optin , 'です'


# st.write('テキスト入力')
# text = st.text_input(
#     'あなたの趣味を教えてください',
# )
# 'あなたの趣味は：　' , text , 'です'

# st.write('スライダー')
# condition = st.slider(
#     'あなたの今のコンディションは？', 0 , 100 , 50
# )
# 'あなたのコンディションは：　' , condition , 'です'