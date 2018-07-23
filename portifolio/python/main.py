import cliente, empresa, sys, functools
# from interface import mainwindow
from interface import mainwindow

lista=[]

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
    codigo = mainwindow.ui.lineEdit.text()
    # mainwindow.ui.listWidget.addItem(codigo)
    mainwindow.ui.tableWidget.insertRow(0,0,codigo)
    print(codigo)
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
