import streamlit as st
import numpy as np
import pandas as pd

st.title('マップの表示')


df = pd.DataFrame(
   np.random.rand(100, 2)/[50,50]  + [35.69 , 139.70],
   columns= ['lat' ,'lon' ]
)
#st.table(df.style.highlight_max(axis=0))
st.map(df)
