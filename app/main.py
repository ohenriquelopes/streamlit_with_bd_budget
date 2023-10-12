import pandas as pd
import streamlit as st
from controller import select
import plotly.express as px
import plotly.figure_factory as ff


st.title('Inserir Dados')


# getting the min and max date
startDate = pd.to_datetime(select.select_all_receitas()['data_recebimento'].min())
endDate = pd.to_datetime(select.select_all_receitas()['data_recebimento'].max())

col1, col2 = st.columns(2)
df = pd.to_datetime(select.select_all_receitas()['data_recebimento'])

with col1:
    start_date = st.date_input('Start date', startDate)
with col2:
    end_date = st.date_input('End date', endDate)


st.write(df)
