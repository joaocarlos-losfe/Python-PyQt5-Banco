class Cliente():
    def __init__(self, nome:str,sobre_nome:str, cpf:str):
        self._nome = nome
        self.sobre_nome = nome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf
