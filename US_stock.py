import pandas as pd
import yfinance as yf
import altair as alt
import streamlit as st

st.title('株価可視化アプリ            by t.tsuka')

st.sidebar.write("""
# US株価
株価可視化ツールです。以下のオプションから表示日数を指定できます。
""")

st.sidebar.write("""
## 表示日数選択
""")

days = st.sidebar.slider('日数', 1, 300, 60)

st.write(f"""
### 過去 **{days}日間** のUS株価
""")

@st.cache
def get_data(days, tickers):
    df = pd.DataFrame()
    for company in tickers.keys():
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period=f'{days}d')
        hist.index = hist.index.strftime('%d %B %Y')
        hist = hist[['Close']]
        hist.columns = [company]
        hist = hist.T
        hist.index.name = 'Name'
        df = pd.concat([df, hist])
    return df

try: 
    st.sidebar.write("""
    ## 株価の範囲指定
    """)
    ymin, ymax = st.sidebar.slider(
        '範囲を指定してください。',
        0.0, 500.0, (30.0, 300.0)
    )

#追加個所
    st.sidebar.write("""
    ## ratioの範囲指定
    """)
    ymin_ratio, ymax_ratio = st.sidebar.slider(
        '範囲を指定してください。',
        0.0, 2.5, (0.8, 1.3)
    )


#追加個所おわり

    tickers = {
        'nvdia': 'NVDA',
        'facebook': 'FB',
        'arkk': 'ARKK',
        'microsoft': 'MSFT',
        'square': 'SQ',
        'micron': 'MU',
        'uber' : 'UBER'
    }
    df = get_data(days, tickers)
    companies = st.multiselect(
        '会社名を選択してください。',
        list(df.index),
        ['arkk', 'square', 'uber']
    )

    if not companies:
        st.error('少なくとも一社は選んでください。')
    else:
        data = df.loc[companies]
        st.write("### 株価 (USD)", data.sort_index())
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=['Date']).rename(
            columns={'value': 'Stock Prices(USD)'}
        )

#追加個所
        data2 = data.copy()
        j = 0
        for k in range(0,len(companies)): 
            for i in range(0,days):
                n = i + j
                data2.loc[n,'ratio']  = data.loc[n,'Stock Prices(USD)'] / data.loc[j,'Stock Prices(USD)']
            j = j + days

        chart = (
            alt.Chart(data2)
            .mark_line(opacity=0.8, clip=True)
            .encode(
                x="Date:T",
                y=alt.Y("ratio:Q", stack=None, scale=alt.Scale(domain=[ymin_ratio, ymax_ratio])),
                color='Name:N'
            )
        )
        st.altair_chart(chart, use_container_width=True)


#追加個所おわり


        chart = (
            alt.Chart(data)
            .mark_line(opacity=0.8, clip=True)
            .encode(
                x="Date:T",
                y=alt.Y("Stock Prices(USD):Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
                color='Name:N'
            )
        )
        st.altair_chart(chart, use_container_width=True)
except:
    st.error(
        "おっと！なにかエラーが起きているようです。"
    )