from typing import List
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('画像の表示')

st.write('チェックボックス')

if st.checkbox('表示する場合はチェックを入れる'):
    img = Image.open('hana.jpg')
    st.image(img, caption='古代ハス' , use_column_width=True)

st.write('セレクトボックス')
optin = st.selectbox(
    'あなたの好きな数字を選んでください',
    list(range(1,11))
)
'あなたの好きな数字は' , optin , 'です'

st.write('テキスト入力')
text = st.text_input(
    'あなたの趣味を教えてください',
)
'あなたの趣味は：　' , text , 'です'

st.write('スライダー')
condition = st.slider(
    'あなたの今のコンディションは？', 0 , 100 , 50
)
'あなたのコンディションは：　' , condition , 'です'