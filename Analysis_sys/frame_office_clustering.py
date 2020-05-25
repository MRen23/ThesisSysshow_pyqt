# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clustering.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import case_office


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("办公室图像数据集聚类评估")
        Form.resize(791, 409)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(20, 60, 761, 291))
        self.listWidget.setObjectName("listWidget")
        for i in range(0,14):
            item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(item)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(350, 20, 61, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(330, 370, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCheckable(True)
        self.pushButton.clicked[bool].connect(self.cluster_set)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "办公室图像数据集聚类评估"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)

        for i in range(0,14):
            item = self.listWidget.item(i)
            item.setText(_translate("Form", str(i+1)+":  "+str(case_office.values_list[i])))


        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Form", "聚类标签"))
        self.pushButton.setText(_translate("Form", "聚类评估"))

    def cluster_set(self,p):
        if p:
            case_office.bar_vis(case_office.cluster_n,case_office.silhouette_avg)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
