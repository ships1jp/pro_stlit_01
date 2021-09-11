import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('画像の表示')

st.write('display image')

img = Image.open('hana.jpg')
st.image(img, caption='古代ハス' , use_column_width=True)