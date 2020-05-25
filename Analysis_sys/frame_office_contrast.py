# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame_office_contrast.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import case_office


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("办公室图像对比展示")
        Form.resize(735, 457)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(280, 20, 191, 16))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 50, 691, 371))
        self.tableWidget.setRowCount(24)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")

        for i in range(0,24):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)


        for i in range(0,24):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)


        for i in range(0,24):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 1, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 2, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 3, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 4, item)


        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "办公室图像对比展示"))
        self.label.setText(_translate("Form", "办公室图像对比挖掘"))

        for i in range(0,24):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("Form", str(i+1)))


        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "频繁项集"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "共享型办公室(a)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "开放式办公室(b)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Contrast(a/b)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Contrast(b/a)"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        for i in range(0,24):
            item = self.tableWidget.item(i, 0)
            item.setText(_translate("Form", str(case_office.show_list[i][0])[10:-1]))
            item = self.tableWidget.item(i, 1)
            item.setText(_translate("Form", str(case_office.show_list[i][1])))
            item = self.tableWidget.item(i, 2)
            item.setText(_translate("Form", str(case_office.show_list[i][2])))
            item = self.tableWidget.item(i, 3)
            item.setText(_translate("Form", str(case_office.show_list[i][3])))
            item = self.tableWidget.item(i, 4)
            item.setText(_translate("Form", str(case_office.show_list[i][4])))

        self.tableWidget.setSortingEnabled(__sortingEnabled)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())