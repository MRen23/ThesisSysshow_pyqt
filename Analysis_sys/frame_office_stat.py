# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'office_stat.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import case_office


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("办公室图像数据统计")
        Form.resize(993, 800)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(50, 60, 245, 650))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(50)

        for i in range(0,50):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        for i in range(0,50):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 1, item)

        self.tableWidget1 = QtWidgets.QTableWidget(Form)
        self.tableWidget1.setGeometry(QtCore.QRect(380, 60, 245, 650))
        self.tableWidget1.setObjectName("tableWidget1")
        self.tableWidget1.setColumnCount(2)
        self.tableWidget1.setRowCount(50)
        for i in range(0,50):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget1.setVerticalHeaderItem(i, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(1, item)

        for i in range(0,50):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget1.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget1.setItem(i, 1, item)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 20, 200, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(410, 20, 200, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(710, 20, 200, 21))
        self.label_3.setObjectName("label_3")

        self.tableWidget_2 = QtWidgets.QTableWidget(Form)
        self.tableWidget_2.setGeometry(QtCore.QRect(680, 60, 245, 650))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(50)

        for i in range(0,50):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setVerticalHeaderItem(i, item)


        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)

        for i in range(0,50):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setItem(i, 1, item)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 740, 75, 23))
        self.pushButton.setCheckable(True)
        self.pushButton.clicked[bool].connect(self.coshare_vis)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 740, 75, 23))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.clicked[bool].connect(self.open_vis)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(750, 740, 75, 23))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.clicked[bool].connect(self.office_all)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "办公室图像数据统计"))

        self.label.setText(_translate("Form", "共享型办公室图像标签统计"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "共享型办公室"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "频率"))
        for i in range(0,50):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("Form", str(i+1)))

        __sortingEnabled = self.tableWidget.isSortingEnabled()

        self.tableWidget.setSortingEnabled(False)

        for j in range(0,50):
            item = self.tableWidget.item(j, 0)
            item.setText(_translate("Form", str(case_office.coshared_stat[j][0])))
            item = self.tableWidget.item(j, 1)
            item.setText(_translate("Form", str(case_office.coshared_stat[j][1])))

        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_2.setText(_translate("Form", "开放式办公室图像标签统计"))

        for i in range(0,50):
            item = self.tableWidget1.verticalHeaderItem(i)
            item.setText(_translate("Form", str(i+1)))


        item = self.tableWidget1.horizontalHeaderItem(0)
        item.setText(_translate("Form", "开放式办公室"))
        item = self.tableWidget1.horizontalHeaderItem(1)
        item.setText(_translate("Form", "频率"))

        __sortingEnabled = self.tableWidget1.isSortingEnabled()

        self.tableWidget1.setSortingEnabled(False)

        for i in range(0,50):
            item = self.tableWidget1.item(i, 0)
            item.setText(_translate("Form", str(case_office.open_stat[i][0])))
            item = self.tableWidget1.item(i, 1)
            item.setText(_translate("Form", str(case_office.open_stat[i][1])))

        self.tableWidget1.setSortingEnabled(__sortingEnabled)

        self.label_3.setText(_translate("Form", "办公室总图像数据集标签统计"))

        for i in range(0,50):
            item = self.tableWidget_2.verticalHeaderItem(i)
            item.setText(_translate("Form", str(i+1)))

        
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "总数据集标签"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "频率"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()


        self.tableWidget_2.setSortingEnabled(False)
        
        for i in range(0,50):
            item = self.tableWidget_2.item(i, 0)
            item.setText(_translate("Form", str(case_office.coshared_stat[i][0])))
            item = self.tableWidget_2.item(i, 1)
            item.setText(_translate("Form", str(case_office.all_labels_stat[i][1])))

        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Form", "可视化"))
        self.pushButton_2.setText(_translate("Form", "可视化"))
        self.pushButton_3.setText(_translate("Form", "可视化"))


    def coshare_vis(self,p):
        if p:
            case_office.hist_bar(case_office.coshared_stat,'共享型办公室数据集')

    def open_vis(self,p):
        if p:
            case_office.hist_bar(case_office.coshared_stat,'开放式办公室数据集')

    def office_all(self,p):
        if p:
            case_office.hist_bar(case_office.all_labels_stat,'办公室图像总数据集')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())