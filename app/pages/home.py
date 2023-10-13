import pandas as pd
import streamlit as st
from controller import select
import plotly.express as px
from datetime import datetime
import calendar

######## Pegando ultimo dia do mes ########


data_atual = datetime.now()
ultimo_dia_do_mes = calendar.monthrange(data_atual.year, data_atual.month)[1]



st.title('Home')
rf = select.select_all_receitas()
df = select.select_all_despesas()


def value_card(title, value):
    st.markdown(f"## {title}")
    st.markdown(f"#### {value}")


rf['data_recebimento'] = pd.to_datetime(rf['data_recebimento'])

rf['mes'] = rf['data_recebimento'].dt.month
rf_grouped = rf.groupby(['mes'])
rf_grouped = rf_grouped.agg({
    'valor': 'sum'
})
# st.write(rf_grouped)

df['data_pagamento'] = pd.to_datetime(df['data_pagamento'])
df['mes'] = df['data_pagamento'].dt.month
df_grouped = df.groupby(['mes'])
df_grouped = df_grouped.agg({
    'valor': 'sum'
})
# st.write(df_grouped)



month = [0]
for i in range(1, 13):
    month.append(i)


mes_selecionado = st.selectbox("Selecione o Mês", month)

if mes_selecionado == 0:
    mes_selecionado = data_atual.month
else:
    mes_selecionado = mes_selecionado


receita_mes_selecionado = rf_grouped.loc[mes_selecionado, 'valor']
despesa_mes_selecionado = df_grouped.loc[mes_selecionado, 'valor']


col1, col2 = st.columns(2)

with col1:
    value_card("Receita", f"R$ {receita_mes_selecionado}")
with col2:
    value_card("Despesas", f"R$ {despesa_mes_selecionado}")





