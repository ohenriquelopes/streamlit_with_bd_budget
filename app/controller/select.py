import streamlit as st
import pymysql
from sqlalchemy import text
import pandas as pd


pymysql.install_as_MySQLdb()
conn = st.experimental_connection('mysql', type='sql')


def select_all_receitas():
    df = conn.query('''
    select
    r.id,
    r.valor,
    r.pago,
    r.data_recebimento,
    cr.nome as categoria
from
    receitas r
inner join categoria_receitas cr
    on cr.id = r.categoria_receita_id;
    ''', ttl=600)
    return df


def select_all_despesas():
    df = conn.query("""
    SELECT
    d.id,
    d.valor,
    d.pago,
    d.data_pagamento,
    cd.nome as 'categoria_despesa',
    tp.nome as 'tipo_pagamento'
FROM
    despesas d
LEFT JOIN categoria_despesas cd
    ON d.categoria_despesa_id = cd.id
LEFT JOIN tipo_pagamento tp
    ON tp.id = d.tipo_pagamento_id
    """, ttl=600)
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