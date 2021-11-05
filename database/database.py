import os
import pathlib as p
import mysql.connector as mysql
from querys import Query

from singleton import Singleton

class Database(Query,metaclass = Singleton):
    def __init__():
        self._path_db = p.Path(__file__).parent.absolute()
        self._path_db = os.path.join(self.path_db,"DB")

        if not os.path.isfile(self.get_path_db):
            conexao = mysql.connect(host = 'localhost',db = 'BancoReal',user = 'root', passwd = 'targout00')
            cursor = conexao.cursor()
            cursor.execute(super().create_table_client())
            cursor.execute(super().create_table_conta())
            cursor.execute(super().create_table_historico())

    @property
    def get_path_db():
        return self._path_db + "local.db"

    def get_cliente(self,cpf):
        conexao = mysql.connect(host = 'localhost',db = 'BancoReal',user = 'root', passwd = 'targout00')
        cursor = conexao.cursor()
        cursor.execute(super().query_get_cliente(),cpf)
        data = exec.fetchall()






        '''
q = Query()

cursor.execute(q.create_table_client())
for i in range(5):
     cursor.execute(q.query_save_date_cliente())

cursor.execute(q.query_get_cliente())

for c in cursor:
    print(c)
conexao.commit()
conexao.close()
'''
