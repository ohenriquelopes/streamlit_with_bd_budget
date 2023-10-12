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

df = select.select_all_receitas()


with col1:
    date1 = st.date_input("Start Date", startDate)
with col2:
    date2 = st.date_input("End Date", endDate)
df = df[(df["data_recebimento"] >= date1) & (df["data_recebimento"] <= date2)].copy()

# list of categories for revenue
cat_receita = df['categoria'].unique()


st.sidebar.header('Choose your filter: ')


# create for revenue filter sidebar
revenue = st.sidebar.multiselect('Pick your revenue', cat_receita)

# todo VER COMO POSSO APLICAR ISSO
# revenue = st.sidebar.selectbox('Pick your revenue', cat_receita)


# if filter is empty, return all data
if not revenue:
    filtered_df = df
else:
    filtered_df = df[df['categoria'].isin(revenue)]


with col1:
    st.subheader('Receitas')
    fig = px.pie(filtered_df, values='valor', names='categoria')
    fig.update_traces(text=filtered_df['valor'], textposition='outside')
    st.plotly_chart(fig, user_container_width=True)