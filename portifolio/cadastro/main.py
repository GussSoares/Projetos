import os, glob
import time

import cliente, empresa, sys, functools
# from interface import mainwindow
from interface import mainwindow, warning
from PyQt5 import QtCore, QtGui, QtWidgets
lista=[]
countRow = 1

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
            item.setFlags(QtCore.Qt.ItemIsEnabled)

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
        warning.Dialog = warning.QtWidgets.QDialog()
        warning.ui = warning.Ui_Dialog()
        warning.ui.setupUi(warning.Dialog, "Espaços vazios!")
        warning.Dialog.show()
        # os.system("pause")
        warning.ui.pushButtom.clicked.connect(functools.partial(warning.Dialog.close))
        # sys.exit(app.exec_())

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

def auto_add():
    global countRow
    mainwindow.ui.tableWidget.setRowCount(countRow)
    total_list=[]
    path = os.path.abspath('Data')
    files = glob.glob(path + '/*.txt')
    with open(files[len(files) - 1], 'r') as file:
        lines=file.readlines()
        for i in range(2):
            lines.pop(0)
        # print(lines)
        for element in lines:
            total_list.append(element.split("\t"))
    for j in range(len(total_list)):
        for k in range(7):
            print(total_list[j][k])
            element = QtWidgets.QTableWidgetItem()
            mainwindow.ui.tableWidget.setItem(countRow-1, k, element)
            # item.setText(total_list[j][k])


            # item = QtWidgets.QTableWidgetItem()
            # mainwindow.ui.tableWidget.setVerticalHeaderItem(countRow - 1, item)
            # item.setText(str(countRow - 1))

        # countRow += 1

if __name__ == '__main__':

    app = mainwindow.QtWidgets.QApplication(sys.argv)
    mainwindow.MainWindow = mainwindow.QtWidgets.QMainWindow()
    mainwindow.ui = mainwindow.Ui_MainWindow()
    mainwindow.ui.setupUi(mainwindow.MainWindow)
    mainwindow.MainWindow.show()

    # auto_add()
    # # check_filename()
    #
    mainwindow.ui.pushButton.clicked.connect(functools.partial(add_client))
    mainwindow.ui.actionSair.triggered.connect(mainwindow.MainWindow.close)
    mainwindow.ui.pushButton_2.clicked.connect(functools.partial(auto_add))

    sys.exit(app.exec_())
