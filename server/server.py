import socket

class OperacoesServidor:

    def __init__(self):
        self._dados = list()
    
    def realizar_cadastro(self):
        print("server >> cadastro")
        try:
            nome = self._dados[1]
            sobrenome = self._dados[2]
            cpf = self._dados[3] 
            senha = self._dados[4]
        except:
            print("alguns dados incorretos ou faltando")
        
    def realizar_saque(self):
        print("server >> saque")
        try:
            cpf = self._dados[1]
            valor = float(self._dados[2])
        except:
            print("alguns dados incorretos ou faltando")

    def realizar_transferencia(self):
        print("server >> transferencia")
        try:
            cpf = self._dados[1]
            conta_destino = self._dados[2]
            valor = float(self._dados[3])
        except:
            print("alguns dados incorretos ou faltando")
            
    def carregar_extrato(self):
        print("server >> extrato")
        pass

    def realizar_deposito(self):
        print("server >> deposito")
        try:
            cpf = self._dados[1]
            valor_deposito = self._dados[2]
        except:
            print("alguns dados incorretos ou faltando")

    def operacoes(self, informacoes: str):

        self._dados = informacoes.split('/')
        
        operacao = self._dados[0]

        if operacao == "cadastro":
            self.realizar_cadastro()

        elif operacao == "saque":
            self.realizar_saque()

        elif operacao == "transferencia":
            self.realizar_transferencia()

        elif operacao == "deposito":
            self.realizar_deposito()
        
        elif operacao == "extrato":
            self.carregar_extrato()
        
        else:
            print("operacao invalida")

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
                servidor.operacoes(dados_cliente)

                mensagem_servidor = str("✔️")
                conexao.send(mensagem_servidor.encode())

                print("⚠️Cliente desconectou\nAguardando nova conexao...")
                conexao, cliente = servidor_socket.accept()
                print(f"conectado...")
            else:
                print("conexao encerrada")
                servidor_socket.close()
                break;

Server.start()