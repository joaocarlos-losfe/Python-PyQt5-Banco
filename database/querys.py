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


    # MÉTODOS DE REMOÇÃO DE DADOS

    # MÉTODOS DE ATUALIZAÇÃO DE DADOS
