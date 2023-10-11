import streamlit as st
from controller import select

st.title('Inserir Dados')

st.info(select.select_all_receitas())
st.info(select.select_all_categoria_despesas())
st.info(select.select_all_categoria_receitas())
st.info(select.select_all_conta_cartao())
st.info(select.select_all_saldo_limite())
st.info(select.select_all_tipo_pagamento())

st.info(select.select_all_despesas())
