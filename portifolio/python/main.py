import cliente, empresa, sys, functools
# from interface import mainwindow
from interface import mainwindow
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

# listar_clientes(lista)


def get_codigo():
    global countRow
    mainwindow.ui.tableWidget.setRowCount(countRow)
    codigo = mainwindow.ui.lineEdit_1.text()
    nome = mainwindow.ui.lineEdit_2.text()
    end = mainwindow.ui.lineEdit_3.text()
    num = mainwindow.ui.lineEdit_4.text()
    cid = mainwindow.ui.lineEdit_5.text()
    bairro = mainwindow.ui.lineEdit_6.text()
    estado = mainwindow.ui.lineEdit_7.text()
    # mainwindow.ui.listWidget.addItem(codigo)

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
    # mainwindow.ui.tableWidget.setItem(0,0,codigo)
    print(codigo)
    lista.clear()
    countRow += 1
    # return codigo



if __name__ == '__main__':

    # cadastrar()
    app = mainwindow.QtWidgets.QApplication(sys.argv)
    mainwindow.MainWindow = mainwindow.QtWidgets.QMainWindow()
    mainwindow.ui = mainwindow.Ui_MainWindow()
    mainwindow.ui.setupUi(mainwindow.MainWindow)
    mainwindow.MainWindow.show()

    mainwindow.ui.pushButton.clicked.connect(functools.partial(get_codigo))

    sys.exit(app.exec_())
