# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hotel_stat.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import case_hotel


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("酒店图像数据集标签统计")
        Form.resize(1315, 887)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 150, 231, 651))
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

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 80, 181, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(580, 20, 231, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(350, 90, 161, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(580, 90, 181, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(830, 90, 171, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(1100, 90, 171, 16))
        self.label_6.setObjectName("label_6")
        self.tableWidget1 = QtWidgets.QTableWidget(Form)
        self.tableWidget1.setGeometry(QtCore.QRect(280, 150, 231, 651))
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



        self.tableWidget_2 = QtWidgets.QTableWidget(Form)
        self.tableWidget_2.setGeometry(QtCore.QRect(540, 150, 231, 651))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(50)
        for  i in range(0,50):
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


        self.tableWidget_3 = QtWidgets.QTableWidget(Form)
        self.tableWidget_3.setGeometry(QtCore.QRect(800, 150, 231, 651))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setRowCount(50)

        for i in range(0,50):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_3.setVerticalHeaderItem(i, item)



        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)

        for i in range(0,50):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_3.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_3.setItem(i, 1, item)


        self.tableWidget_4 = QtWidgets.QTableWidget(Form)
        self.tableWidget_4.setGeometry(QtCore.QRect(1060, 150, 231, 651))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(2)
        self.tableWidget_4.setRowCount(50)

        for i in range(0,50):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_4.setVerticalHeaderItem(i, item)



        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)

        for i in range(0,50):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_4.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_4.setItem(i, 1, item)


        self.btn_gfA = QtWidgets.QPushButton(Form)
        self.btn_gfA.setGeometry(QtCore.QRect(90, 830, 75, 23))
        self.btn_gfA.setCheckable(True)
        self.btn_gfA.clicked[bool].connect(self.officialA_vis)
        self.btn_gfA.setObjectName("btn_gfA")

        self.btn_gfB = QtWidgets.QPushButton(Form)
        self.btn_gfB.setGeometry(QtCore.QRect(350, 830, 75, 23))
        self.btn_gfB.setCheckable(True)
        self.btn_gfB.clicked[bool].connect(self.officialB_vis)
        self.btn_gfB.setObjectName("btn_gfB")

        self.btn_all = QtWidgets.QPushButton(Form)
        self.btn_all.setGeometry(QtCore.QRect(610, 830, 75, 23))
        self.btn_all.setCheckable(True)
        self.btn_all.clicked[bool].connect(self.travelerA_vis)
        self.btn_all.setObjectName("btn_all")

        self.btn_lyB = QtWidgets.QPushButton(Form)
        self.btn_lyB.setGeometry(QtCore.QRect(880, 830, 75, 23))
        self.btn_lyB.setCheckable(True)
        self.btn_lyB.clicked[bool].connect(self.travelerB_vis)
        self.btn_lyB.setObjectName("btn_lyB")

        self.btn_lyA = QtWidgets.QPushButton(Form)
        self.btn_lyA.setGeometry(QtCore.QRect(1150, 830, 75, 23))
        self.btn_lyA.setCheckable(True)
        self.btn_lyA.clicked[bool].connect(self.all_vis)
        self.btn_lyA.setObjectName("btn_lyA")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "酒店图像数据集标签统计"))

        for i in range(0,50):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("Form", str(i+1)))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "官方数据集A"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "频率"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        for i in range(0,50):
            item = self.tableWidget.item(i,0)
            item.setText(_translate("Form", str(case_hotel.official_stat_45[i][0])))
            item = self.tableWidget.item(i, 1)
            item.setText(_translate("Form", str(case_hotel.official_stat_45[i][1])))


        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Form", "官方数据集A图像标签统计"))
        self.label_2.setText(_translate("Form", "酒店图像数据集标签统计"))
        self.label_3.setText(_translate("Form", "官方数据集B图像标签统计"))
        self.label_4.setText(_translate("Form", "旅游者数据集A图像标签统计"))
        self.label_5.setText(_translate("Form", "旅游者数据集B图像标签统计"))
        self.label_6.setText(_translate("Form", "酒店总数据集图像标签统计"))

        for i in range(0,50):
            item = self.tableWidget1.verticalHeaderItem(i)
            item.setText(_translate("Form", str(i+1)))



        item = self.tableWidget1.horizontalHeaderItem(0)
        item.setText(_translate("Form", "官方数据集B"))
        item = self.tableWidget1.horizontalHeaderItem(1)
        item.setText(_translate("Form", "频率"))
        __sortingEnabled = self.tableWidget1.isSortingEnabled()
        self.tableWidget1.setSortingEnabled(False)

        for i in range(0,50):
            item = self.tableWidget1.item(i,0)
            item.setText(_translate("Form", str(case_hotel.official_stat_23[i][0])))
            item = self.tableWidget1.item(i, 1)
            item.setText(_translate("Form", str(case_hotel.official_stat_23[i][1])))

        self.tableWidget1.setSortingEnabled(__sortingEnabled)

        for i in range(0,50):
            item = self.tableWidget_2.verticalHeaderItem(i)
            item.setText(_translate("Form", str(i+1)))


        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "旅游者数据集A"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "频率"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)

        for i in range(0,50):
            item = self.tableWidget_2.item(i, 0)
            item.setText(_translate("Form", str(case_hotel.traveler_stat_45[i][0])))
            item = self.tableWidget_2.item(i, 1)
            item.setText(_translate("Form", str(case_hotel.traveler_stat_45[i][1])))

        self.tableWidget_2.setSortingEnabled(__sortingEnabled)

        for i in range(0,50):
            item = self.tableWidget_3.verticalHeaderItem(i)
            item.setText(_translate("Form", str(i+1)))


        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Form", "旅游者数据集B"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("Form", "频率"))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)

        for i in range(0,50):
            item = self.tableWidget_3.item(i, 0)
            item.setText(_translate("Form", str(case_hotel.traveler_stat_23[i][0])))
            item = self.tableWidget_3.item(i, 1)
            item.setText(_translate("Form", str(case_hotel.traveler_stat_23[i][1])))

        self.tableWidget_3.setSortingEnabled(__sortingEnabled)

        for i in range(0,50):
            item = self.tableWidget_4.verticalHeaderItem(i)
            item.setText(_translate("Form", str(i+1)))


        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("Form", "总数据集"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("Form", "频率"))
        __sortingEnabled = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)

        for i in range(0,50):
            item = self.tableWidget_4.item(i, 0)
            item.setText(_translate("Form", str(case_hotel.all_labels_stat[i][0])))
            item = self.tableWidget_4.item(i, 1)
            item.setText(_translate("Form", str(case_hotel.all_labels_stat[i][1])))


        self.tableWidget_4.setSortingEnabled(__sortingEnabled)
        self.btn_gfA.setText(_translate("Form", "可视化"))
        self.btn_gfB.setText(_translate("Form", "可视化"))
        self.btn_all.setText(_translate("Form", "可视化"))
        self.btn_lyB.setText(_translate("Form", "可视化"))
        self.btn_lyA.setText(_translate("Form", "可视化"))


    def officialA_vis(self,p):
        if p:
            case_hotel.hist_bar(case_hotel.official_stat_45,"官方数据集A图像标签统计")


    def officialB_vis(self,p):
        if p:
            case_hotel.hist_bar(case_hotel.official_stat_23,"官方数据集A图像标签统计")


    def travelerA_vis(self,p):
        if p:
            case_hotel.hist_bar(case_hotel.traveler_stat_45,"旅游者数据集A图像标签统计")


    def travelerB_vis(self,p):
        if p:
            case_hotel.hist_bar(case_hotel.traveler_stat_23,"旅游者数据集B图像标签统计")

    def all_vis(self,p):
        if p:
            case_hotel.hist_bar(case_hotel.all_labels_stat,"酒店总数据集图像标签统计")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())