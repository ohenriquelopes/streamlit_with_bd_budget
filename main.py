import streamlit as st
import pymysql
# import pages.select as select
import controller.cliente as cliente
import pages.inserir as inserir

import streamlit as st
import pymysql
# função para selecionar todos os registros no banco de dados

pymysql.install_as_MySQLdb()
conn = st.experimental_connection('mysql', type='sql')


conn.query("INSERT INTO test.pessoas (id, nome, idade, job) VALUES (NULL, 'a', 1, 'a');")
conn.commit()




# st.write(cliente.select_all())
# rows = []
# for row in df.itertuples():
#     rows.append(row)
# st.write(rows)

# Initialize connection.
# conn = st.experimental_connection('mysql', type='sql')
# Perform query.
# df = conn.query('SELECT * from test.table;', ttl=600)

# select.consultar()

# select()

# Print results.
# for row in df.itertuples():
#     # st.write(f"{row.name} has a :{row.pet}:")
#     st.write(f"{row.coluna}")

# select.consultar()