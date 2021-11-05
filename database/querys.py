class Query:

    # MÉTODOS DE CRIAÇÃO DAS TABELAS


    @staticmethod
    def create_table_client():
        return """
                CREATE TABLE IF NOT EXISTS Clientes
                (
                    CPF VARCHAR(14) NOT NULL PRIMARY KEY,
                    Nome VARCHAR(20) NOT NULL,
                    Sobrenome VARCHAR(50) NOT NULL
                );
                """

    @staticmethod
    def create_table_conta():
        return """
            CREATE TABLE IF NOT EXISTS Contas
            (
                numero VARCHAR(15) NOT NULL PRIMARY KEY,
                cpf_titular VARCHAR(8) NOT NULL,
                saldo FLOAT NOT NULL,
                senha TEXT NOT NULL,
                limite FLOAT NOT NULL,
                FOREIGN KEY (cpf_titular) REFERENCES Clientes(CPF)
            );
        """
    @staticmethod
    def create_table_historico():
        return """
            CREATE TABLE IF NOT EXISTS Historicos
            (
                ID int NOT NULL PRIMARY KEY AUTO_INCREMENT,
                historico TEXT NOT NULL,
                numero_conta VARCHAR(15) NOT NULL,
                FOREIGN KEY (numero_conta) REFERENCES Contas(numero)
            );
        """

    # MÉTODOS DE SALVAMENTO DE DADOS

    @staticmethod
    def query_save_cliente():
        return  """
                INSERT INTO Clientes(CPF,Nome,Sobrenome)
                VALUES (%s,%s,%s)
                """
    @staticmethod
    def query_save_date_conta():
        return  """
                INSERT INTO Contas(numero, cpf_titular, saldo, senha, limite)
                VALUES (%s,%s,%s,MD5(%s),%s)
                """
    @staticmethod
    def query_save_date_historico():
        return  """
                INSERT INTO Historicos(historico,numero_conta)
                VALUES (?,?)
                """

    # MÉTODOS DE ATUALIZAÇÃO DE DADOS

    @staticmethod
    def query_update_cliente():
        return  """
                UPDATE Cliente
                SET Nome = ?,Sobrenome = ?,Senha = ?
                WHERE CPF = ?;
                """

    @staticmethod
    def query_update_conta():
        return  """
                UPDATE Conta
                SET cpf_titular = ?,saldo = ?,senha = ?,limite = ?
                WHERE numero = ?;
                """
    @staticmethod
    def query_update_historico():
        return  """
                UPDATE Historico
                SET historico = ?
                WHERE numero_conta = ?;
                """

    # MÉTODOS DE REMOÇÃO DE DADOS

    @staticmethod
    def query_delete_cliente():
        return  """
                DELETE FROM Cliente WHERE CPF = ?
                """
    @staticmethod
    def query_delete_conta():
        return  """
                DELETE FROM Conta WHERE numero = ?
                """
    @staticmethod
    def query_delete_historico():
        return  """
                DELETE FROM Historico WHERE numero_conta = ?
                """
    # MÉTODOS DE CAPTURAS DE DADOS

    @staticmethod
    def query_get_cliente():
        return  """
                    SELECT * FROM Cliente WHERE CPF = ?
                """
    @staticmethod
    def query_get_conta():
        return  """
                    SELECT * FROM Conta WHERE numero = ?
                """
    @staticmethod
    def query_get_historico():
        return  """
                    SELECT * FROM Historico WHERE numero_conta = ?
                """
    # FIM
