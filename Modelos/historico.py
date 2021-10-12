from datetime import datetime

class Historico():
    def __init__(self):
        self.data_abertura = datetime.today()
        self.historico_transacoes = []

    def exibir_historico(self):
        count = 1;
        print("\nexibindo seu historico")
        for historico in self.historico_transacoes:
            print(f"{count}: {historico}")
            count +=1
