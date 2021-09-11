from typing import List
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('画像の表示')

st.sidebar.write('チェックボックス')

if st.sidebar.checkbox('表示する場合はチェックを入れる'):
    img = Image.open('hana.jpg')
    st.image(img, caption='古代ハス' , use_column_width=True)

st.sidebar.write('セレクトボックス')
optin = st.sidebar.selectbox(
    'あなたの好きな数字を選んでください',
    list(range(1,11))
)
'あなたの好きな数字は' , optin , 'です'


st.sidebar.write('テキスト入力')
text = st.sidebar.text_input(
    'あなたの趣味を教えてください',
)
'あなたの趣味は：　' , text , 'です'

st.sidebar.write('スライダー')
condition = st.sidebar.slider(
    'あなたの今のコンディションは？', 0 , 100 , 50
)
'あなたのコンディションは：　' , condition , 'です'