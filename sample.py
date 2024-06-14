import streamlit as st
import numpy as np
import pandas as pd
from io import BytesIO
#from pyxlsb import open_workbook as open_xlsb
 
st.write("""
# My first app
Hello *world!*
""")
 
df = pd.read_csv("my_data.csv")
st.line_chart(df)




dataframe = pd.DataFrame(np.random.randn(10, 5),
  columns = ('col %d' % i
    for i in range(5)))
dataframe
st.write('This is a line_chart.')
st.line_chart(dataframe)

uploaded_file = st.file_uploader("Choose a file", type=['xlsx', 'csv'])



st.radio("好きなマイケルは？", ('ジャクソン', 'ジョーダン', 'ホフマン'))
