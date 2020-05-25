# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox,QLabel,QLineEdit,QPushButton,QFrame

from PyQt5.QtGui import QIcon

from PyQt5.QtCore import Qt

from main import *
import hotel_main
import office_main
import dataget


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QIcon
# from hello import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import main
import frame_office_stat
import frame_hotel_stat

import case_hotel
import case_office

# from Ui_Main import Ui_MainWindow

class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(u'展示系统')
        self.resize(400,300)
        #窗体居中
        # self.move(desk.width()/2-self.width()/2,100)
        myframe=QFrame(self)

        lbltitle=QLabel('图像内容识别技术和对比挖掘在网站分析中的应用展示',myframe)

        lbl1=QLabel('用户名：',myframe)
        lbl1.move(30,30)
        lbl2=QLabel('密  码：',myframe)
        lbl2.move(30,60)

        self.leUsername=QLineEdit(myframe)
        self.lePassword=QLineEdit(myframe)
        self.leUsername.move(80,30)
        self.lePassword.move(80,60)
        self.lePassword.setEchoMode(QLineEdit.Password)

        btnLogin=QPushButton('登录',myframe)
        btnQuit=QPushButton('退出',myframe)

        btnLogin.move(30,120)
        btnQuit.move(110,120)

        btnLogin.clicked.connect(self.myBtnClick)
        btnQuit.clicked.connect(self.myBtnClick)

        myframe.move(50,50)
        myframe.resize(300,300)

        #隐藏放大缩小按钮
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.show()

    def myBtnClick(self):
        account = self.leUsername.text()
        password = self.lePassword.text()

        if account == "" or password == "":
            QMessageBox.warning(self,"警告","账号密码不能为空！")
            return

        # elif account == "任萌" and password == "123":
        elif account == "1" and password == "1":
            #mc_main.show()
            import os
            os.system("python main.py")
            self.close()

        else:
            QMessageBox.warning(self,"警告","用户名密码错误！",QMessageBox.Yes)
            self.lineEdit.setFocus()


if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()

    desk=app.desktop()

    mc = MyClass()
    mc_main = Ui_Form()
    app.exec_()

