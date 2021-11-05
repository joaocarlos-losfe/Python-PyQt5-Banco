import os
import mysql.connector as mysql
from querys import Query

conexao = mysql.connect(host = 'localhost',db = 'BancoReal',user = 'root', passwd = 'targout00')
cursor = conexao.cursor()

cursor.execute(Query.create_table_client())
for i in range(5):
     cursor.execute(Query.query_save_date_cliente())

cursor.execute(query_get_cliente())

for c in cursor:
    print(c)

conexao.commit()
conexao.close()
