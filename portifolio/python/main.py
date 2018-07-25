import os, glob

import cliente, empresa, sys, functools
# from interface import mainwindow
from interface import mainwindow, warning
from PyQt5 import QtCore, QtGui, QtWidgets
lista=[]
countRow = 1

def cadastrar():
    c = cliente.Cliente(None, None)
    c.nome = input("Digite seu nome: ")
    c.telefone = input("Digite seu telefone: ")
    if c.nome != None:
        print("Cliente cadastrado com sucesso!")
        lista.append(c)
        return c

def listar_clientes(lista):
    for i in lista:
        print(i.nome+", "+i.telefone)


def remover_cliente(lista, nome):
    for i in lista:
        if i.nome == nome:
            lista.remove(i)
    print(i.nome, "removido com sucesso!")


def add_client():
    global countRow
    mainwindow.ui.tableWidget.setRowCount(countRow)
    codigo = mainwindow.ui.lineEdit_1.text()
    nome = mainwindow.ui.lineEdit_2.text()
    end = mainwindow.ui.lineEdit_3.text()
    num = mainwindow.ui.lineEdit_4.text()
    cid = mainwindow.ui.lineEdit_5.text()
    bairro = mainwindow.ui.lineEdit_6.text()
    estado = mainwindow.ui.lineEdit_7.text()

    if (nome != "") and (codigo != ""):
        lista.append(codigo)
        lista.append(nome)
        lista.append(end)
        lista.append(num)
        lista.append(cid)
        lista.append(bairro)
        lista.append(estado)
        print(lista)
        for i in range(len(lista)):
            item = QtWidgets.QTableWidgetItem()
            mainwindow.ui.tableWidget.setItem(countRow-1, i, item)
            item.setText(lista[i])

            item = QtWidgets.QTableWidgetItem()
            mainwindow.ui.tableWidget.setVerticalHeaderItem(countRow-1, item)
            item.setText(str(countRow-1))
        print(codigo)
        path = os.path.abspath('Data')
        files = glob.glob(path + '/*.txt')
        with open(files[len(files)-1], 'a') as file:
            file.write("\n")
            for i in range(len(lista)):
                file.write(lista[i]+"\t")

        lista.clear()
        countRow += 1
    else:
        print("entrou")
        # app = warning.QtWidgets.QApplication(sys.argv)
        warning.Dialog = QtWidgets.QDialog()
        warning.ui = warning.Ui_Dialog()
        warning.ui.setupUi(warning.Dialog, "Espaços vazios!")
        warning.Dialog.show()
        # sys.exit(app.exec_())
        warning.ui.pushButtom.clicked.connect(functools.partial(warning.Dialog.close))

def check_filename():
    global i
    path = os.path.abspath('Data')
    if os.path.isfile(os.path.abspath('Data/Resultado.txt')) is True:
        print("if")

        files = glob.glob(path+'/*.txt')
        print(files)
        with open(files[len(files)-1], 'r') as file:

            arq = file.read()
            i = arq.split(" ")[1][0]
            i = int(i)+1
        with open(path+"/Resultado_"+str(i)+".txt",'w+') as file:
            file.write("Version "+str(i)+"\nCódigo	Nome	End	Num	Cidade		Bairro	Estado")

    else:

        path = os.path.abspath('Data/Resultado.txt')
        with open(path, 'w+') as file:
            file.write("Version 1\nCódigo	Nome	End	Num	Cidade		Bairro	Estado")


if __name__ == '__main__':

    app = mainwindow.QtWidgets.QApplication(sys.argv)
    mainwindow.MainWindow = mainwindow.QtWidgets.QMainWindow()
    mainwindow.ui = mainwindow.Ui_MainWindow()
    mainwindow.ui.setupUi(mainwindow.MainWindow)
    mainwindow.MainWindow.show()

    check_filename()

    mainwindow.ui.pushButton.clicked.connect(functools.partial(add_client))
    mainwindow.ui.actionSair.triggered.connect(mainwindow.MainWindow.close)

    sys.exit(app.exec_())
