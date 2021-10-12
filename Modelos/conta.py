from historico import Historico
class Conta():

    _contador_contas = 0

    __slots__ = ['_numero', '_titular', '_saldo', '_limite', '_historico']

    def __init__(self, numero, titular, saldo, limite = 10000):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        Conta._contador_contas += 1

        #self._definir_historico(f"conta aberta dia {self.historico.data_abertura}. Numero: {self.numero}. Limite: {self.limite} ")

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def titular(self):
        return self._titular

    @property
    def limite(self):
        return self._limite

    def exibir_historico(self):
        self._historico.exibir_historico()

    def _definir_historico(self, msg):
        self._historico.historico_transacoes.append(msg)

    def depositar(self, valor):
        self._saldo += valor
        self._definir_historico(f"deposito no valor de R$ {valor} dia {datetime.today()}. saldo atual: R$ {self._saldo}")

    def sacar(self, valor):
        if(valor > self._saldo):
            self._definir_historico(f"tentativa de saque no valor de R$ {valor} dia {datetime.today()}. valor de saque maior que o saldo disponivel na conta")
            return False
        else:
            self._saldo -= valor
            self._definir_historico(f"saque realizado no valor de R$ {valor} dia {datetime.today()}. saldo atual: R$ {self._saldo}")
            return True

    def transfere(self, conta_destino, valor):
        if(self._saldo < valor):
            self._definir_historico(f"tentativa de transferencia para a conta {conta_destino._numero}. saldo insuficiente para transaferencia")
            return False
        else:
            self.sacar(valor)
            self._definir_historico(f"transferencia realizada para a conta {conta_destino._numero}")
            self._definir_historico(f"você recebeu uma transferencia de {self._titular.nome}. no valor de {valor}")
            conta_destino.depositar(valor)
            return True

    @staticmethod
    def quantidade_contas():
        return Conta._contador_contas