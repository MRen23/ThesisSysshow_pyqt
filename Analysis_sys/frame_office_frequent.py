# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame_office_frequent.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import case_office


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("办公室图像数据集频繁项集挖掘")
        Form.resize(682, 713)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 50, 161, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(420, 50, 171, 16))
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(40, 90, 241, 581))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(23)

        for i in range(0,23):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)


        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        for i in range(0,23):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 1, item)

        self.tableWidget_2 = QtWidgets.QTableWidget(Form)
        self.tableWidget_2.setGeometry(QtCore.QRect(360, 90, 251, 581))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(23)
        for i in range(0,23):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setVerticalHeaderItem(i, item)


        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)

        for i in range(0,23):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setItem(i, 1, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "办公室图像数据集频繁项集挖掘"))
        self.label.setText(_translate("Form", "共享型办公室频繁项集展示"))
        self.label_2.setText(_translate("Form", "开放式办公室频繁项集展示"))

        #共享型办公室
        for i in range(0,23):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("Form", str(i+1)))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "频繁项集"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "频率"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        for i in range(0,23):
            item = self.tableWidget.item(i, 0)
            item.setText(_translate("Form", str(case_office.co_processing[i][0])[10:-1]))
            item = self.tableWidget.item(i, 1)
            item.setText(_translate("Form", str(case_office.co_processing[i][1])))

        self.tableWidget.setSortingEnabled(__sortingEnabled)

        #开放式办公室
        for i in range(0,23):
            item = self.tableWidget_2.verticalHeaderItem(i)
            item.setText(_translate("Form", str(i+1)))


        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "频繁项集"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "频率"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)

        for i in range(0,23):
            item = self.tableWidget_2.item(i, 0)
            item.setText(_translate("Form", str(case_office.open_processing[i][0])[10:-1]))
            item = self.tableWidget_2.item(i, 1)
            item.setText(_translate("Form", str(case_office.open_processing[i][1])))

        self.tableWidget_2.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())