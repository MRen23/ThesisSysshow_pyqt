# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame_hotel_contrast.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import case_hotel


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("酒店图像对比挖掘")
        Form.resize(926, 927)

        # 官方总 vs 旅游者总
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(350, 0, 331, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(360, 320, 281, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(350, 630, 281, 16))
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(60, 30, 811, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(68)

        for i in range(0,68):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)

        for i in range(0,68):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)

        for i in range(0,68):
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

        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)

        # 官方A vs 官方B
        self.tableWidget_2 = QtWidgets.QTableWidget(Form)
        self.tableWidget_2.setGeometry(QtCore.QRect(60, 340, 811, 271))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(20)
        for i in range(0,20):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setVerticalHeaderItem(i, item)

        for i in range(0,20):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setHorizontalHeaderItem(i, item)

        for i in range(0,20):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setItem(i, 1, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setItem(i, 2, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setItem(i, 3, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setItem(i, 4, item)

        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(150)

        # 旅游者A vs 旅游者B
        self.tableWidget_3 = QtWidgets.QTableWidget(Form)
        self.tableWidget_3.setGeometry(QtCore.QRect(60, 650, 811, 271))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(5)
        self.tableWidget_3.setRowCount(74)

        for i in range(0,74):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_3.setVerticalHeaderItem(i, item)

        for i in range(0,74):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_3.setHorizontalHeaderItem(i, item)

        for i in range(0,74):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_3.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_3.setItem(i, 1, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_3.setItem(i, 2, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_3.setItem(i, 3, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_3.setItem(i, 4, item)

        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(150)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

        # 官方总 vs 旅游者总
        Form.setWindowTitle(_translate("Form", "酒店图像对比挖掘"))
        self.label.setText(_translate("Form", "官方图像总数据集和旅游者图像总数据集对比挖掘"))
        self.label_2.setText(_translate("Form", "官方图像数据集A和官方图像数据集B对比挖掘"))
        self.label_3.setText(_translate("Form", "旅游者图像数据集A和旅游者图像数据集B对比挖掘"))

        for i in range(0,68):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("Form", str(i+1)))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "频繁项集"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "官方图像总数据集(a)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "旅游者图像总数据集(b)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Contrast(a/b)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Contrast(b/a)"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()

        self.tableWidget.setSortingEnabled(False)

        for i in range(0,68):
            item = self.tableWidget.item(i, 0)
            item.setText(_translate("Form", str(case_hotel.contrast_official_traveler[i][0])[10:-1]))
            item = self.tableWidget.item(i, 1)
            item.setText(_translate("Form", str(case_hotel.contrast_official_traveler[i][1])))
            item = self.tableWidget.item(i, 2)
            item.setText(_translate("Form", str(case_hotel.contrast_official_traveler[i][2])))
            item = self.tableWidget.item(i, 3)
            item.setText(_translate("Form", str(case_hotel.contrast_official_traveler[i][3])))
            item = self.tableWidget.item(i, 4)
            item.setText(_translate("Form", str(case_hotel.contrast_official_traveler[i][4])))

        self.tableWidget.setSortingEnabled(__sortingEnabled)


        # 官方A vs 官方B

        # print (case_hotel.contrast_official_45_vs_23)

        for i in range(0,20):
            item = self.tableWidget_2.verticalHeaderItem(i)
            item.setText(_translate("Form", str(i+1)))


        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "频繁项集"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "官方图像数据集A(a)"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "官方图像数据集B(b)"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Contrast(a/b)"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Contrast(b/a)"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()

        self.tableWidget_2.setSortingEnabled(False)

        for i in range(0,20):
            item = self.tableWidget_2.item(i, 0)
            item.setText(_translate("Form", str(case_hotel.contrast_official_45_vs_23[i][0])[10:-1]))
            item = self.tableWidget_2.item(i, 1)
            item.setText(_translate("Form", str(case_hotel.contrast_official_45_vs_23[i][1])))
            item = self.tableWidget_2.item(i, 2)
            item.setText(_translate("Form", str(case_hotel.contrast_official_45_vs_23[i][2])))
            item = self.tableWidget_2.item(i, 3)
            item.setText(_translate("Form", str(case_hotel.contrast_official_45_vs_23[i][3])))
            item = self.tableWidget_2.item(i, 4)
            item.setText(_translate("Form", str(case_hotel.contrast_official_45_vs_23[i][4])))

        self.tableWidget_2.setSortingEnabled(__sortingEnabled)


        # 旅游A vs 旅游B

        for i in range(0,74):
            item = self.tableWidget_3.verticalHeaderItem(i)
            item.setText(_translate("Form", str(i+1)))


        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Form", "频繁项集"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("Form", "旅游者图像数据集A(a)"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("Form", "旅游者图像数据集B(b)"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Contrast(a/b)"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Contrast(b/a)"))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()




        self.tableWidget_3.setSortingEnabled(False)
        for i in range(0,74):
            item = self.tableWidget_3.item(i, 0)
            item.setText(_translate("Form", str(case_hotel.contrast_traveler_45_vs_23[i][0])[10:-1]))
            item = self.tableWidget_3.item(i, 1)
            item.setText(_translate("Form", str(case_hotel.contrast_traveler_45_vs_23[i][1])))
            item = self.tableWidget_3.item(i, 2)
            item.setText(_translate("Form", str(case_hotel.contrast_traveler_45_vs_23[i][2])))
            item = self.tableWidget_3.item(i, 3)
            item.setText(_translate("Form", str(case_hotel.contrast_traveler_45_vs_23[i][3])))
            item = self.tableWidget_3.item(i, 4)
            item.setText(_translate("Form", str(case_hotel.contrast_traveler_45_vs_23[i][4])))


        self.tableWidget_3.setSortingEnabled(__sortingEnabled)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())