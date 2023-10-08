import streamlit as st
import pymysql


pymysql.install_as_MySQLdb()

# Initialize connection.
conn = st.experimental_connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from test.table;', ttl=600)

# Print results.
for row in df.itertuples():
    # st.write(f"{row.name} has a :{row.pet}:")
    st.write(f"{row.coluna}")