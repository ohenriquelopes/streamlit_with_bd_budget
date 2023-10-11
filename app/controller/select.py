import streamlit as st
import pymysql
from sqlalchemy import text

pymysql.install_as_MySQLdb()
conn = st.experimental_connection('mysql', type='sql')

def select_all_cash_flow():
    df = conn.query('SELECT * from test.cash_flow;', ttl=600)
    return df

def select_all_categoria_despesas():
    df = conn.query('SELECT * from test.categoria_despesas;', ttl=600)
    return df

def select_all_categoria_receitas():
    df = conn.query('SELECT * from test.categoria_despesas;', ttl=600)
    return df

def select_all_conta_cartao():
    df = conn.query('SELECT * from test.conta_cartao;', ttl=600)
    return df

def select_all_saldo_limite():
    df = conn.query('SELECT * from test.saldo_limite;', ttl=600)
    return df

def select_all_tipo_pagamento():
    df = conn.query('SELECT * from test.tipo_pagamento;', ttl=600)
    return df