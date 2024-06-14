import streamlit as st
import numpy as np
import pandas as pd
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb
 
st.write("""
# My first app
Hello *world!*
""")
 
# df = pd.read_csv("my_data.csv")
# st.line_chart(df)

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    #writer.save()
    writer.close()
    processed_data = output.getvalue()
    return processed_data

def df_to_xlsx(df):
    byte_xlsx = BytesIO()
    writer_xlsx = pd.ExcelWriter(byte_xlsx, engine="xlsxwriter")
    df.to_excel(writer_xlsx, index=False, sheet_name="Sheet1")
    ##-----必要に応じてexcelのフォーマット等を設定-----##
    workbook = writer_xlsx.book
    worksheet = writer_xlsx.sheets["Sheet1"]
    format1 = workbook.add_format({"num_format": "0.00"})
    worksheet.set_column("A:A", None, format1)
    #writer_xlsx.save()
    writer_xlsx.close()
    ##---------------------------------------------##
    workbook = writer_xlsx.book
    out_xlsx = byte_xlsx.getvalue()
    return out_xlsx



dataframe = pd.DataFrame(np.random.randn(10, 5),
  columns = ('col %d' % i
    for i in range(5)))
dataframe
st.write('This is a line_chart.')
st.line_chart(dataframe)

uploaded_file = st.file_uploader("Choose a file", type=['xlsx', 'csv'])
if uploaded_file is not None:
    #df1 = pd.read_excel(uploaded_file, sheet_name='Ergebnisse', decimal =',')
# Automatically display the uploaded file
    try:
        # Check the file extension and read accordingly
        if uploaded_file.name.endswith('.xlsx'):
            df1 = pd.read_excel(uploaded_file, decimal=',')
        elif uploaded_file.name.endswith('.csv'):
            df1 = pd.read_csv(uploaded_file, decimal=',')
        else:
            st.write("Unsupported file type")

        # Displaying the uploaded file
        st.write("Displaying the uploaded file:")
        st.write(df1)

        # Check if df1 is empty
        if df1.empty:
            st.write("The uploaded file is empty or could not be read.")
        else:
            st.line_chart(df1)
    except pd.errors.EmptyDataError:
        st.write("The uploaded file is empty.")
    except pd.errors.ParserError:
        st.write("Error parsing the uploaded file.")
    except ValueError as ve:
        st.write(f"ValueError: {ve}")
    except Exception as e:
        st.write(f"An unexpected error occurred: {e}")
        
# xlsx_test = df_to_xlsx(dataframe)

# st.download_button(label="Download", data=xlsx_test, file_name="_test.xlsx")

df_xlsx = to_excel(dataframe)
st.download_button(label='📥 Download Current Result',
                                data=df_xlsx ,
                                file_name= 'df_test.xlsx')

st.radio("好きなマイケルは？", ('ジャクソン', 'ジョーダン', 'ホフマン'))
