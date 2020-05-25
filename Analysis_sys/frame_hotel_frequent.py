# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame_hotel_frequent.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import case_hotel

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("酒店图像数据集频繁项集挖掘")
        Form.resize(1127, 475)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 60, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(380, 60, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(640, 60, 141, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(920, 60, 161, 16))
        self.label_4.setObjectName("label_4")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 100, 231, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(15)

        for i in range(0,15):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)



        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        for i in range(0,15):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 1, item)


        self.tableWidget_2 = QtWidgets.QTableWidget(Form)
        self.tableWidget_2.setGeometry(QtCore.QRect(310, 100, 231, 331))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(15)


        for i in range(0,15):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setVerticalHeaderItem(i, item)


        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)

        for i in range(0,15):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setItem(i, 1, item)


        self.tableWidget_3 = QtWidgets.QTableWidget(Form)
        self.tableWidget_3.setGeometry(QtCore.QRect(590, 100, 231, 331))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setRowCount(15)

        for i in range(0,15):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_3.setVerticalHeaderItem(i, item)


        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)

        for i in range(0,15):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_3.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_3.setItem(i, 1, item)


        self.tableWidget_4 = QtWidgets.QTableWidget(Form)
        self.tableWidget_4.setGeometry(QtCore.QRect(870, 100, 231, 331))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(2)
        self.tableWidget_4.setRowCount(15)

        for i in range(0,15):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_4.setVerticalHeaderItem(i, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)

        for i in range(0,15):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_4.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_4.setItem(i, 1, item)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "酒店图像数据集频繁项集挖掘"))
        self.label.setText(_translate("Form", "官方数据集A频繁项集"))
        self.label_2.setText(_translate("Form", "官方数据集B频繁项集"))
        self.label_3.setText(_translate("Form", "旅游者数据集A频繁项集"))
        self.label_4.setText(_translate("Form", "旅游者数据集B频繁项集"))



        for i in range(0,15):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("Form", str(i+1)))


        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "新建列"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "频率"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        #官方A
        for i in range(0,15):
            item = self.tableWidget.item(i, 0)
            item.setText(_translate("Form", str(case_hotel.gfA_processing[i][0])[10:-1]))
            item = self.tableWidget.item(i, 1)
            item.setText(_translate("Form", str(case_hotel.gfA_processing[i][1])))


        self.tableWidget.setSortingEnabled(__sortingEnabled)

        for i in range(0,15):
            item = self.tableWidget_2.verticalHeaderItem(i)
            item.setText(_translate("Form", str(i+1)))


        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "新建列"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "频率"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)

        #官方B
        for i in range(0,15):
            item = self.tableWidget_2.item(i, 0)
            # print (case_hotel.gfB_processing)
            item.setText(_translate("Form", str(case_hotel.gfB_processing[i][0])[10:-1]))
            item = self.tableWidget_2.item(i, 1)
            item.setText(_translate("Form", str(case_hotel.gfB_processing[i][1])))


        self.tableWidget_2.setSortingEnabled(__sortingEnabled)

        for i in range(0,15):
            item = self.tableWidget_3.verticalHeaderItem(i)
            item.setText(_translate("Form", str(i+1)))


        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Form", "新建列"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("Form", "频率"))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)

        # 旅游A
        for i in range(0,15):
            item = self.tableWidget_3.item(i, 0)
            item.setText(_translate("Form", str(case_hotel.lyA_processing[i][0])[10:-1]))
            item = self.tableWidget_3.item(i, 1)
            item.setText(_translate("Form", str(case_hotel.lyA_processing[i][1])))


        self.tableWidget_3.setSortingEnabled(__sortingEnabled)

        for i in range(0,15):
            item = self.tableWidget_4.verticalHeaderItem(i)
            item.setText(_translate("Form", str(i+1)))

        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("Form", "新建列"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("Form", "频率"))
        __sortingEnabled = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)

        #旅游B
        for i in range(0,15):
            item = self.tableWidget_4.item(i, 0)
            item.setText(_translate("Form", str(case_hotel.lyB_processing[i][0])[10:-1]))
            item = self.tableWidget_4.item(i, 1)
            item.setText(_translate("Form", str(case_hotel.lyB_processing[i][1])))


        self.tableWidget_4.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())