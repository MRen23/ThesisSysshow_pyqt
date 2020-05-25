__author__ = 'TF'
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'office_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


# from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox,QLabel,QLineEdit,QPushButton,QFrame,QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import main


class Ui_Form2(object):
    def setupUi(self, Form):

        # self.setWindowTitle(u'办公室图像对比')
        Form.setObjectName("酒店的图像对比")
        Form.resize(1109, 975)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(30, 10, 1051, 651))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 1041, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(380, 10, 411, 31))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_5.setText(_translate("Form", "数据爬取"))
        self.pushButton_3.setText(_translate("Form", "数据统计"))
        self.pushButton_2.setText(_translate("Form", "聚类分析"))
        self.pushButton.setText(_translate("Form", "频繁项集挖掘"))
        self.pushButton_4.setText(_translate("Form", "对比挖掘"))
        self.label.setText(_translate("Form", "酒店图像对比"))

#
# if __name__=='__main__':
#     import sys
#     app=QApplication(sys.argv)
#     MainWindow=QtWidgets.QMainWindow()
#
#     ui = Ui_Form2()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     app.exec_()
