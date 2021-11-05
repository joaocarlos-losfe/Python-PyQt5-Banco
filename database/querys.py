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
            CREATE TABLE IF NOT EXISTS Conta
            (
                historico TEXT NOT NULL PRIMARY KEY,
                numero_conta VARCHAR(15) NOT NULL FOREING KEY
            );
        """
