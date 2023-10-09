
import streamlit as st


import pymysql
from sqlalchemy import text
# função para selecionar todos os registros no banco de dados

pymysql.install_as_MySQLdb()
conn = st.experimental_connection('mysql', type='sql')

with conn.session as s:
    # s.execute('INSERT INTO test.pessoas (nome, idade, job) VALUES ("aasdas", 12, "a");')
    s.execute(text('INSERT INTO test.pessoas (nome, idade, job) VALUES ("11111111111111", 12, "a");'))
    s.commit()


