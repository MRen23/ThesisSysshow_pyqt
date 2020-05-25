# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'office_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox,QLabel,QLineEdit,QPushButton,QFrame,QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
# import dataget

class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("办公室图像对比")
        Form.resize(1127, 871)

        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 10, 1081, 851))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 1071, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")


        #数据获取
        self.pushButton_dataget = QtWidgets.QPushButton(self.horizontalLayoutWidget)

        self.pushButton_dataget.setCheckable(True)
        # self.pushButton_dataget.toggle()
        self.pushButton_dataget.clicked[bool].connect(self.dataGet)
        # self.pushButton_dataget.clicked.connect(self.dataGet)

        # self.pushButton_dataget
        self.pushButton_dataget.setObjectName("pushButton_dataget")
        print('33333')

        self.horizontalLayout.addWidget(self.pushButton_dataget)

        #数据统计
        self.pushButton_datastat = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_datastat.setObjectName("pushButton_datastat")
        self.horizontalLayout.addWidget(self.pushButton_datastat)

        self.pushButton_cluster = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_cluster.setObjectName("pushButton_cluster")
        self.horizontalLayout.addWidget(self.pushButton_cluster)

        self.pushButton_fre = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_fre.setObjectName("pushButton_fre")
        self.horizontalLayout.addWidget(self.pushButton_fre)

        self.pushButton_contrast = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_contrast.setObjectName("pushButton_contrast")
        self.horizontalLayout.addWidget(self.pushButton_contrast)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(380, 10, 411, 31))
        self.label.setObjectName("label")




        # self.frame_2 = QtWidgets.QFrame(self.frame)
        # self.frame_2.setGeometry(QtCore.QRect(20, 140, 1041, 691))
        # self.frame_2.setStyleSheet("image: url(:/no/图像/office_image_get.png);")
        # self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_2.setObjectName("frame_2")


        self.retranslateUi(Form)
        self.dataGet(self.frame)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_dataget.setText(_translate("Form", "数据爬取"))
        self.pushButton_datastat.setText(_translate("Form", "数据统计"))
        self.pushButton_cluster.setText(_translate("Form", "聚类分析"))
        self.pushButton_fre.setText(_translate("Form", "频繁项集挖掘"))
        self.pushButton_contrast.setText(_translate("Form", "对比挖掘"))
        self.label.setText(_translate("Form", "共享型办公室和开放型办公室图像对比"))



    def dataGet(self,p):
        print ('55555')
        if p == True:
            print ('111111111')
            self.frame_2 = QtWidgets.QFrame(self.frame)
            self.frame_2.setGeometry(QtCore.QRect(20, 140, 1041, 691))
            self.frame_2.setStyleSheet("image: url(:/no/图像/office_image_get.png);")
            self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_2.setObjectName("frame_2")
            self.frame_2.show()

import data_get_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow=QtWidgets.QMainWindow()

    ui = Ui_Form1()
    ui.setupUi(MainWindow)
    MainWindow.show()


    sys.exit(app.exec())










# class Ui_Form1(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setupUi()
#         # self.retranslateUi(self)
#
#
#     def setupUi(self):
#
#         self.setWindowTitle(u'办公室图像展示系统')
#
#
#         btn_dataget = QPushButton("数据获取")
#
#         btn_datastat = QPushButton("数据统计")
#
#         btn_cluster = QPushButton("聚类分析")
#
#         btn_frequent = QPushButton("频繁项集")
#
#         btn_contrast = QPushButton("对比分析")
#
#
#         hbl = QHBoxLayout()
#         hbl.addWidget(btn_dataget)
#         hbl.addWidget(btn_datastat)
#         hbl.addWidget(btn_cluster)
#         hbl.addWidget(btn_frequent)
#         hbl.addWidget(btn_contrast)
#
#
#         vbl = QVBoxLayout(self)





