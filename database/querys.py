class Query:

    # MÉTODOS DE CRIAÇÃO DAS TABELAS

    @staticmethod
    def create_table_client():
        return """
                CREATE TABLE IF NOT EXISTS Cliente
                (
                    CPF VARCHAR(14) NOT NULL PRIMARY KEY,
                    Nome VARCHAR(20) NOT NULL,
                    Sobrenome VARCHAR(50) NOT NULL,
                    Senha VARCHAR(8) NOT NULL
                );
                """

    @staticmethod
    def create_table_conta():
        return """
            CREATE TABLE IF NOT EXISTS Conta
            (
                numero VARCHAR(15) NOT NULL PRIMARY KEY,
                cpf_titular VARCHAR(8) NOT NULL,
                saldo FLOAT NOT NULL,
                senha VARCHAR(8) NOT NULL,
                limite VARCHAR(8) NOT NULL
            );
        """
    @staticmethod
    def create_table_historico():
        return """
            CREATE TABLE IF NOT EXISTS Historico
            (
                historico TEXT NOT NULL PRIMARY KEY,
                numero_conta VARCHAR(15) NOT NULL FOREING KEY
            );
        """

    # MÉTODOS DE SALVAMENTO DE DADOS

    @staticmethod
    def query_save_date_cliente():
        return  """
                INSERT INTO Cliente(CPF,Nome,Sobrenome,Senha)
                VALUES (?,?,?,?)
                """
    @staticmethod
    def query_save_date_conta():
        return  """
                INSERT INTO Conta(numero,cpf_titular,saldo,senha,limite)
                VALUES (?,?,?,?,?)
                """
    @staticmethod
    def query_save_date_historico():
        return  """
                INSERT INTO Historico(historico,numero_conta)
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
