import streamlit as st
import pandas as pd
import altair as alt
@st.cache
def get_un_data():
    df=pd.read_csv("agri.csv")
    return df.set_index("Region")
df=get_un_data()
countries=st.multiselect("Choose countries",list(df.index),default=["United States of America","India"])
data=df.loc[countries]
data/=1000000.0
st.write("### gross agriculture production ($B)",data.sort_index())
data=data.T.reset_index()
data=pd.melt(data,id_vars=["index"]).rename(
    columns={"index":"year","value":"gross agriculture product ($B)"}
)
chart=alt.Chart(data).mark_area(opacity=0.3).encode(x="year:T",y=alt.Y("gross agriculture product ($B):Q", stack=None),color="Region:N")
st.altair_chart(chart,use_container_width=True)
