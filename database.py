from logging import Logger
import os
import mysql.connector as mysql
from querys import Query
from Modelos.conta import Conta


class Database:

    def __init__(self):

        self.conexao = mysql.connect(host = 'localhost', db = 'BancoReal',user = 'root', passwd = 'sousafej2021')
        self.cursor = self.conexao.cursor()
        self.inicializar_db()


    def inicializar_db(self):
        self.cursor.execute(Query.create_table_client())
        self.cursor.execute(Query.create_table_conta())
        self.cursor.execute(Query.create_table_historico())

    def adicionar_conta(self, conta:Conta):

        try:
            self.cursor.execute(Query.query_save_cliente(), (conta.titular.cpf, conta.titular.nome, conta.titular.sobre_node))
            self.cursor.execute(Query.query_save_date_conta(), (conta.numero, conta.titular.cpf, conta.saldo, conta.senha, conta.limite))
            self.conexao.commit()
            return "True"
            
        except BaseException as e:
            Logger.error('Failed to do something: ' + str(e))
            return "False"