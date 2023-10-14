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

st.write(mes_selecionado)
st.write(df_grouped)
st.write(rf_grouped)


# if mes_selecionado nao for localizado no df try except
try:
    despesa_mes_selecionado = df_grouped.loc[mes_selecionado, 'valor']
except:
    despesa_mes_selecionado = 0

try:
    receita_mes_selecionado = rf_grouped.loc[mes_selecionado, 'valor']
except:
    receita_mes_selecionado = 0



col1, col2 = st.columns(2)

with col1:
    value_card("Receita", f"R$ {receita_mes_selecionado}")
with col2:
    value_card("Despesas", f"R$ {despesa_mes_selecionado}")



col1, col2 = st.columns(2)

saldo_geral = 10
saldo_mes = receita_mes_selecionado - despesa_mes_selecionado
with col1:
    st.write("## Saldo Mes")
    st.write(f"R$ {saldo_mes}")

with col2:
    st.write("## Saldo Geral")
    st.write(f"R$ {saldo_geral}")

### Grafico de receitas no ano

rf['mes'] = rf['data_recebimento'].dt.month
rf_grouped = rf.groupby(['mes'])
rf_grouped = rf_grouped.agg({
    'valor': 'sum'
})
rf_grouped = rf_grouped.reset_index()
rf_grouped['mes'] = rf_grouped['mes'].apply(lambda x: calendar.month_abbr[x])
rf_grouped['valor'] = rf_grouped['valor'].apply(lambda x: round(x, 2))
rf_grouped['valor'] = rf_grouped['valor'].apply(lambda x: f"{x}")

### Gerando grafico de receitas no ano
st.subheader("Receitas por ano")
fig = px.bar(rf_grouped, x="mes", y="valor", text=['R$ {}'.format(x) for x in rf_grouped["valor"]],
             template="seaborn")
st.plotly_chart(fig, use_container_width=True, height=200)

############################
############################
############################


### Grafico de despesas no ano

df['mes'] = df['data_pagamento'].dt.month
df_grouped = df.groupby(['mes'])
df_grouped = df_grouped.agg({
    'valor': 'sum'
})
df_grouped = df_grouped.reset_index()
df_grouped['mes'] = df_grouped['mes'].apply(lambda x: calendar.month_abbr[x])
df_grouped['valor'] = df_grouped['valor'].apply(lambda x: round(x, 2))
df_grouped['valor'] = df_grouped['valor'].apply(lambda x: f"{x}")

### Gerando grafico de despesas no ano
st.subheader("Despesas no ano")
fig = px.bar(df_grouped, x="mes", y="valor", text=['R$ {}'.format(x) for x in df_grouped["valor"]],
             template="seaborn")
st.plotly_chart(fig, use_container_width=True, height=200)
