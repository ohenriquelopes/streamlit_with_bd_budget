import datetime

import pandas as pd
import streamlit as st


from controller import select
import plotly.express as px
import plotly.figure_factory as ff


st.title('Inserir Dados')

############# CREATE FILTERS ######################



col1, col2 = st.columns(2)

# getting the min and max date
startDate = pd.to_datetime(select.select_all_receitas()['data_recebimento'].min())
endDate = pd.to_datetime(select.select_all_receitas()['data_recebimento'].max())
# startDate = data1.strftime('%Y-%m-%d')
# endDate = data2.strftime('%Y-%m-%d')

df = select.select_all_receitas()


with col1:
    date1 = st.date_input("Start Date", startDate)
with col2:
    date2 = st.date_input("End Date", endDate)
df = df[(df["data_recebimento"] >= date1) & (df["data_recebimento"] <= date2)].copy()

cat_receita = df['categoria'].unique()



st.sidebar.header('Choose your filter: ')

# create for revenue
revenue = st.sidebar.multiselect('Pick your revenue', cat_receita)

if not revenue:
    filtered_df = df
else:
    filtered_df = df[df['categoria'].isin(revenue)]




with col1:
    st.subheader('Receitas')
    fig = px.pie(filtered_df, values='valor', names='categoria', title='Receitas')
    fig.update_traces(text=filtered_df['valor'], textposition='outside')
    st.plotly_chart(fig, user_container_width=True)