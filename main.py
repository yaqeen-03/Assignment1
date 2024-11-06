import numpy as np
import pandas as pd
import streamlit as st

st.title("This is First Assignment")
st.write("This assignment is for Cloud Computing!!")

data = pd.DataFrame(
    {"coluomn1":["P","Q","R","S","T"],
     "coluomn2":[1000,1001,1002,1003,1004]}
)

st.write("This is just a sample data!!")
st.write(data)

chart_data=pd.DataFrame(
    np.random.randn(20,4),
    columns=["P","Q","R","T"]

)

st.line_chart(chart_data)