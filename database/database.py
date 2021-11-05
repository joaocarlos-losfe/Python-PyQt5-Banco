import os
import mysql.connector as mysql
from query import Query
import hashlib

class Database:

    def __init__(self):

        self.conexao = mysql.connect(host = 'localhost', db = 'BancoReal',user = 'root', passwd = 'sousafej2021')
        self.cursor = self.conexao.cursor()
        self.inicializar_db()


    def inicializar_db(self):
        self.cursor.execute(Query.create_table_client())
        self.cursor.execute(Query.create_table_conta())
        self.cursor.execute(Query.create_table_historico())

    def adicionar_conta(self, cpf:str, nome:str, sobre_nome:str, numero:str, saldo:float, senha:str, limite: float):

        #self.cursor.execute(Query.query_save_cliente(), (cpf, nome, sobre_nome))
        self.cursor.execute(Query.query_save_date_conta(), (numero, cpf, saldo, senha, limite))
        self.conexao.commit()


db = Database()

db.adicionar_conta("111", "Joao Carlos", "de Sousa", "111 111 111", 200.50, "arrozComFeijao", 1000)
