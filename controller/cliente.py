# carregando as funções em outros arquivos .py
# import services.database as db
import streamlit as st
import pymysql
# função para selecionar todos os registros no banco de dados

pymysql.install_as_MySQLdb()
conn = st.experimental_connection('mysql', type='sql')


def select_all():
    df = conn.query('SELECT * from test.table;', ttl=600)
    return df


# def insert(input_name, input_age, input_job):
#     # Inicia uma sessão dentro da conexão
#     with conn.session as s:
#         # Use placeholders para inserir os valores de forma segura na consulta SQL
#         query = 'INSERT INTO test.pessoas VALUES (NULL, :input_name, :input_age, :input_job);'
#         s.execute(query, params={'nome': input_name, 'idade': input_age, 'job': input_job})
#         s.commit()
#         # Retorna uma mensagem de sucesso
#     return st.write("Inserido com sucesso")


# def insert(input_name, input_age, input_job):
#     with conn.session as s:
#         # query = 'INSERT INTO test.pessoas VALUES (NULL, :input_name, :input_age, :input_job);'
#         # s.execute(query, params={'input_name': input_name, 'input_age': input_age, 'input_job': input_job})
#         s.execute("INSERT INTO test.pessoas (id, nome, idade, job) VALUES (NULL, 'a', 1, 'a');")
#         s.commit()
#     return st.write("Inserido com sucesso")

