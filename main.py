import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QFileDialog,QMessageBox
from PyQt5.QtCore import QCoreApplication

from Telas.home_page import Telas
from conta import Conta
from historico import Historico
from cliente import Cliente

class Ui_Main(QtWidgets.QWidget):

    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640,480)
        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        #self.stack1 = QtWidgets.QMainWindow()
        #self.stack2 = QtWidgets.QMainWindow()

        self.tela_inicio = Telas()
        self.tela_inicio.setupUi(self.stack0)
        self.QtStack.addWidget(self.stack0)

        '''

        self.tela_cadastro = Tela_cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_busca = Tela_busca()
        self.tela_busca.setupUi(self.stack2)

        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
'''

class Main(QMainWindow,Ui_Main):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)

        self.cad = Conta()
        self.tela_inicio.pushButton.clicked.connect(self.abrir_tela_cadastro)
        '''
        self.tela_inicio.pushButton_2.clicked.connect(self.abrir_tela_busca)

        self.tela_cadastro.pushButton.clicked.connect(self.botao_cadastro)
        self.tela_busca.pushButton.clicked.connect(self.botao_busca)
        self.tela_busca.pushButton_2.clicked.connect(self.botar_voltar)
        '''
    def botao_cadastro(self):
        nome = self.tela_inicio.le_cad_nome_completo_2.text()
        cpf = self.tela_inicio.le_cad_cpf_2.text()
        nascimento = self.tela_inicio.le_cad_nascimento_2.text()
        senha = self.tela_inicio.le_cad_senha_2.text()
        if not(nome == '' or cpf == '' or nascimento == '' or senha == ''):
            p = Pessoa(nome,cpf,nascimento,senha)
            if( self.cad.cadastra(p)):
                QMessageBox.information(None,' [ ! ]','Cadastro Feito com Sucesso!')
                self.tela_inicio.lineEdit.setText('')
                self.tela_inicio.lineEdit_2.setText('')
                self.tela_inicio.lineEdit_3.setText('')
                self.tela_inicio.lineEdit_4.setText('')
            else:
                QMessageBox.information(None,' [ ! ]','CPF já existe!')
        else:
                QMessageBox.information(None,' [ ! ]','DADOS INCORRETOS')

        self.QtStack.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
