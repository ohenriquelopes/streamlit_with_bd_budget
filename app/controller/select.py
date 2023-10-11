import streamlit as st
import pymysql
from sqlalchemy import text

pymysql.install_as_MySQLdb()
conn = st.experimental_connection('mysql', type='sql')

def select_all_():
    df = conn.query('SELECT * from test.table;', ttl=600)
    return df

