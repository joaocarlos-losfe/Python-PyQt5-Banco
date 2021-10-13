class Contas():
    def __init__(self):
        self.dict_contas = {}

    def salvar_conta(self,conta):
        if conta.titular.cpf in self.dict_contas.keys():
            return False # não salvou
        else:
            self.dict_contas[conta.titular.cpf] = conta
            return True #salvou 


    def get_conta(self,cpf):
        if cpf in self.dict_contas.keys():
            return self.dict_contas[cpf]
        else:
            return None
