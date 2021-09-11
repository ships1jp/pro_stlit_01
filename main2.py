import streamlit as st
import numpy as np
import pandas as pd

st.title('グラフの表示')


df = pd.DataFrame(
   np.random.rand(20, 3) ,
   columns= ['a' ,'b' ,'c']
)
#st.table(df.style.highlight_max(axis=0))
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)