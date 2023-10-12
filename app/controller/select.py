import streamlit as st
import pymysql
from sqlalchemy import text
import pandas as pd


pymysql.install_as_MySQLdb()
conn = st.experimental_connection('mysql', type='sql')


def select_all_receitas():
    df = conn.query('SELECT * from test.receitas;', ttl=600)
    # dic = df.to_dict()
    # df_teste = pd.arrays.SparseArray(df['valor'])
    # df_select = df['valor'].to_dict()
    # df_select1 = df['valor'].to_list()
    # df_select = df.to_dict()
    # return df_select
    # return df_teste
    return df
    # return dic

# df = pd.DataFrame(
#     [
#         {"command": "st.selectbox", "rating": 4, "is_widget": True},
#         {"command": "st.balloons", "rating": 5, "is_widget": False},
#         {"command": "st.time_input", "rating": 3, "is_widget": True},
#     ]
# )
#
# st.dataframe(df, use_container_width=True)


def select_all_despesas():
    df = conn.query('SELECT * from test.despesas;', ttl=600)
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