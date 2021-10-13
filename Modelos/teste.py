from conta import Conta
from contas import Contas
from cliente import Cliente

contas = Contas()

cliente0 = Cliente(1,2,1)
cliente1 = Cliente(1,2,2)
cliente2 = Cliente(1,2,3)
cliente3 = Cliente(1,2,3)

conta0 = Conta(1,cliente0,1,1)
conta1 = Conta(1,cliente1,1,1)
conta2 = Conta(1,cliente2,1,1)
conta3 = Conta(1,cliente3,1,1)


print(contas.salvar_conta(conta0))
print(contas.salvar_conta(conta1))
print(contas.salvar_conta(conta2))
print(contas.salvar_conta(conta3))

print(contas.get_conta(4))
print(conta0.quantidade_contas())
