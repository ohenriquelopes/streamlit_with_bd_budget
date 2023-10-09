# carregando as funções em outros arquivos .py
# import services.database as db
import streamlit as st
import pymysql
from sqlalchemy import text
# função para selecionar todos os registros no banco de dados

pymysql.install_as_MySQLdb()
conn = st.experimental_connection('mysql', type='sql')


def select_all():
    df = conn.query('SELECT * from test.table;', ttl=600)
    return df


def insert(input_name1, input_age, input_job):
    # Inicia uma sessão dentro da conexão
    with conn.session as s:
        # Use placeholders para inserir os valores de forma segura na consulta SQL
        s.execute(text('INSERT INTO test.pessoas (nome, idade, job) VALUES (:input_name2, :input_age, :input_job);'), params={'input_name2': input_name1, 'input_age': input_age, 'input_job': input_job})
        s.commit()
        # Retorna uma mensagem de sucesso
    return st.write("Inserido com sucesso")

