import socket
from Modelos.contas import Contas
from Modelos.cliente import Cliente
from Modelos.conta import Conta

class OperacoesServidor:

    def __init__(self):
        self.contas = Contas()

        cliente1 = Cliente("joao", "de sousa", "111")
        conta1 = Conta(cliente1, "111")
        conta1.depositar(200)
        self.contas.salvar_conta(conta1)

        cliente2 = Cliente("vitor", "santos de lima", "222")
        conta2 = Conta(cliente2, "222")
        self.contas.salvar_conta(conta2)
    
    def obter_usuario(self, cpf, senha):
        conta = self.contas.get_conta_cpf(cpf)

        if conta is not None and conta.senha == senha:
            return conta.titular.nome+"/"+conta.titular.sobre_node
        
        else:
            return "False"

    
    def realizar_cadastro(self, nome, sobre_nome,cpf, senha):
        
        cliente = Cliente(nome, sobre_nome, cpf)
        conta = Conta(cliente, senha)

        if self.contas.salvar_conta(conta):
            print(f"conta salva > {conta.numero}")
            return "True/"+conta.numero

        return "False"

        
    def realizar_saque(self):
        pass

    def realizar_transferencia(self):
        pass
            
    def carregar_extrato(self):
        pass

    def realizar_deposito(self):
        pass

    def operacoes(self, informacoes: str):

        informacoes = informacoes.split('/')
        
        sucesso = "False"

        if informacoes[0] == "cadastro":
            return self.realizar_cadastro(informacoes[1], informacoes[2], informacoes[3], informacoes[4])
        
        if informacoes[0] == "obter_usuario":
            return self.obter_usuario(informacoes[1], informacoes[2])

        elif informacoes[0] == "saque":
            sucesso = self.realizar_saque()

        elif informacoes[0] == "transferencia":
            sucesso = self.realizar_transferencia()

        elif informacoes[0] == "deposito":
            sucesso = self.realizar_deposito()
        
        elif informacoes[0] == "extrato":
            sucesso = self.carregar_extrato()
        
        else:
            print("informacoes[0] invalida")
    
        return sucesso

class Server:
    @staticmethod
    def start():
        print("---servidor---")

        host = "localhost"
        porta = 8000
        endereco = (host, porta)

        servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor_socket.bind(endereco)
        servidor_socket.listen(10)
        print(" Aguardando conexao...")
        conexao, cliente = servidor_socket.accept()
        print("Conectado...")

        dados_cliente = ''
        mensagem_servidor = ''

        servidor = OperacoesServidor()

        while(True):

            dados_cliente = conexao.recv(1024)
            dados_cliente = dados_cliente.decode()
            
            if dados_cliente != "~desconectar~":

                print(f"🗨️: {dados_cliente}")
            
                mensagem_servidor = servidor.operacoes(dados_cliente)
                
                conexao.send(mensagem_servidor.encode())

                print("⚠️Cliente desconectou\nAguardando nova conexao...")
                conexao, cliente = servidor_socket.accept()
                print(f"conectado...")
            else:
                print("conexao encerrada")
                servidor_socket.close()
                break;

Server.start()