# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(881, 530)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 50, 821, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(160, 200, 160, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")


        self.pushButton_office_dataget = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_office_dataget.setObjectName("pushButton")
        self.pushButton_office_dataget.setCheckable(True)
        self.pushButton_office_dataget.clicked[bool].connect(self.officeDataGet)
        self.verticalLayout.addWidget(self.pushButton_office_dataget)

        self.pushButton_datastat = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_datastat.setObjectName("pushButton_datastat")
        self.pushButton_datastat.setCheckable(True)
        self.pushButton_datastat.clicked[bool].connect(self.officeDataStat)
        self.verticalLayout.addWidget(self.pushButton_datastat)


        self.pushButton_cluster = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_cluster.setObjectName("pushButton_cluster")
        self.pushButton_cluster.setCheckable(True)
        self.pushButton_cluster.clicked[bool].connect(self.officeCluster_DBI)
        self.verticalLayout.addWidget(self.pushButton_cluster)


        self.pushButton_frequent = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_frequent.setObjectName("pushButton_frequent")
        self.pushButton_frequent.setCheckable(True)
        self.pushButton_frequent.clicked[bool].connect(self.officeFrequent)
        self.verticalLayout.addWidget(self.pushButton_frequent)


        self.pushButton_contrast = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_contrast.setObjectName("pushButton_contrast")
        self.pushButton_contrast.setCheckable(True)
        self.pushButton_contrast.clicked[bool].connect(self.officeContrast)
        self.verticalLayout.addWidget(self.pushButton_contrast)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(540, 190, 160, 291))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")


        self.pushButton_hotel_dataget = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_hotel_dataget.setObjectName("pushButton_hotel_dataget")
        self.pushButton_hotel_dataget.setCheckable(True)
        self.pushButton_hotel_dataget.clicked[bool].connect(self.hotelDataGet)
        self.verticalLayout_2.addWidget(self.pushButton_hotel_dataget)


        self.pushButton_hotel_datastat= QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_hotel_datastat.setObjectName("pushButton_hotel_datastat")
        self.pushButton_hotel_datastat.setCheckable(True)
        self.pushButton_hotel_datastat.clicked[bool].connect(self.hotelDataStat)
        self.verticalLayout_2.addWidget(self.pushButton_hotel_datastat)


        self.pushButton_hotel_cluster = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_hotel_cluster.setObjectName("pushButton_hotel_cluster")
        self.pushButton_hotel_cluster.setCheckable(True)
        self.pushButton_hotel_cluster.clicked[bool].connect(self.hotelCluster_DBI)
        self.verticalLayout_2.addWidget(self.pushButton_hotel_cluster)


        self.pushButton_hotel_frequent = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_hotel_frequent.setObjectName("pushButton_hotel_frequent")
        self.pushButton_hotel_frequent.setCheckable(True)
        self.pushButton_hotel_frequent.clicked[bool].connect(self.hotelFrequent)
        self.verticalLayout_2.addWidget(self.pushButton_hotel_frequent)


        self.pushButton_hotel_contrast = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_hotel_contrast.setObjectName("pushButton_hotel_contrast")
        self.pushButton_hotel_contrast.setCheckable(True)
        self.pushButton_hotel_contrast.clicked[bool].connect(self.hotelContrast)
        self.verticalLayout_2.addWidget(self.pushButton_hotel_contrast)


        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 140, 291, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(560, 140, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "图像内容识别技术和对比挖掘在网站分析中的应用研究系统"))
        self.pushButton_office_dataget.setText(_translate("Form", "数据获取"))
        self.pushButton_datastat.setText(_translate("Form", "数据统计"))
        self.pushButton_cluster.setText(_translate("Form", "聚类分析"))
        self.pushButton_frequent.setText(_translate("Form", "频繁项集挖掘"))
        self.pushButton_contrast.setText(_translate("Form", "对比挖掘"))
        self.pushButton_hotel_dataget.setText(_translate("Form", "数据获取"))
        self.pushButton_hotel_datastat.setText(_translate("Form", "数据统计"))
        self.pushButton_hotel_cluster.setText(_translate("Form", "聚类分析"))
        self.pushButton_hotel_frequent.setText(_translate("Form", "频繁项集挖掘"))
        self.pushButton_hotel_contrast.setText(_translate("Form", "对比挖掘"))
        self.label_2.setText(_translate("Form", "共享型和开放式办公室图像对比"))
        self.label_3.setText(_translate("Form", "酒店图像对比"))


    def officeDataGet(self,p):
        if p:
            os.system("python frame_office_dataget.py")

    def officeDataStat(self,p):
        if p:
            os.system("python frame_office_stat.py")

    def officeCluster_DBI(self,p):
        if p:
            os.system("python frame_office_clustering.py")


    def officeFrequent(self,p):
        if p:
            os.system("python frame_office_frequent.py")

    def officeContrast(self,p):
        if p:
            os.system("python frame_office_contrast.py")



    def hotelDataGet(self,p):
        if p:
            os.system("python frame_hotel_dataget.py")

    def hotelDataStat(self,p):
        if p:
            os.system("python frame_hotel_stat.py")

    def hotelCluster_DBI(self,p):
        if p:
            os.system("python frame_hotel_clustering.py")


    def hotelFrequent(self,p):
        if p:
            os.system("python frame_hotel_frequent.py")

    def hotelContrast(self,p):
        if p:
            os.system("python frame_hotel_contrast.py")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())




# # -*- coding: utf-8 -*-
#
# # Form implementation generated from reading ui file 'main.ui'
# #
# # Created by: PyQt5 UI code generator 5.13.0
# #
# # WARNING! All changes made in this file will be lost!
#
#
# from PyQt5 import QtCore, QtGui, QtWidgets
# import os
#
# class Ui_Form(object):
#     def setupUi(self, Form):
#         Form.setObjectName("Form")
#         Form.resize(901, 599)
#         self.label = QtWidgets.QLabel(Form)
#         self.label.setGeometry(QtCore.QRect(290, 60, 351, 31))
#         self.label.setObjectName("label")
#
#         self.verticalLayoutWidget = QtWidgets.QWidget(Form)
#         self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 260, 160, 271))
#         self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
#         self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
#         self.verticalLayout.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout.setObjectName("verticalLayout")
#
#         self.pushButton_office_dataget = QtWidgets.QPushButton(self.verticalLayoutWidget)
#         self.pushButton_office_dataget.setObjectName("pushButton")
#         self.pushButton_office_dataget.setCheckable(True)
#         self.pushButton_office_dataget.clicked[bool].connect(self.officeDataGet)
#         self.verticalLayout.addWidget(self.pushButton_office_dataget)
#
#         self.pushButton_datastat = QtWidgets.QPushButton(self.verticalLayoutWidget)
#         self.pushButton_datastat.setObjectName("pushButton_datastat")
#         self.pushButton_datastat.setCheckable(True)
#         self.pushButton_datastat.clicked[bool].connect(self.officeDataStat)
#         self.verticalLayout.addWidget(self.pushButton_datastat)
#
#         self.pushButton_cluster = QtWidgets.QPushButton(self.verticalLayoutWidget)
#         self.pushButton_cluster.setObjectName("pushButton_cluster")
#         self.pushButton_cluster.setCheckable(True)
#         self.pushButton_cluster.clicked[bool].connect(self.officeCluster_DBI)
#         self.verticalLayout.addWidget(self.pushButton_cluster)
#
#         self.pushButton_frequent = QtWidgets.QPushButton(self.verticalLayoutWidget)
#         self.pushButton_frequent.setObjectName("pushButton_frequent")
#         self.pushButton_frequent.setCheckable(True)
#         self.pushButton_frequent.clicked[bool].connect(self.officeFrequent)
#         self.verticalLayout.addWidget(self.pushButton_frequent)
#
#         self.pushButton_contrast = QtWidgets.QPushButton(self.verticalLayoutWidget)
#         self.pushButton_contrast.setObjectName("pushButton_contrast")
#         self.pushButton_contrast.setCheckable(True)
#         self.pushButton_contrast.clicked[bool].connect(self.officeContrast)
#         self.verticalLayout.addWidget(self.pushButton_contrast)
#
#         self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
#         self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(640, 260, 160, 271))
#         self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
#         self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
#         self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_2.setObjectName("verticalLayout_2")
#
#         self.pushButton_hotel_dataget = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
#         self.pushButton_hotel_dataget.setObjectName("pushButton_hotel_dataget")
#         self.pushButton_hotel_dataget.setCheckable(True)
#         self.pushButton_hotel_dataget.clicked[bool].connect(self.hotelDataGet)
#         self.verticalLayout_2.addWidget(self.pushButton_hotel_dataget)
#
#         self.pushButton_hotel_datastat= QtWidgets.QPushButton(self.verticalLayoutWidget_2)
#         self.pushButton_hotel_datastat.setObjectName("pushButton_hotel_datastat")
#         self.pushButton_hotel_datastat.setCheckable(True)
#         self.pushButton_hotel_datastat.clicked[bool].connect(self.hotelDataStat)
#         self.verticalLayout_2.addWidget(self.pushButton_hotel_datastat)
#
#         self.pushButton_hotel_cluster = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
#         self.pushButton_hotel_cluster.setObjectName("pushButton_hotel_cluster")
#         self.pushButton_hotel_datastat.setCheckable(True)
#         self.pushButton_hotel_datastat.clicked[bool].connect(self.hotelCluster_DBI)
#         self.verticalLayout_2.addWidget(self.pushButton_hotel_cluster)
#
#         self.pushButton_hotel_frequent = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
#         self.pushButton_hotel_frequent.setObjectName("pushButton_hotel_frequent")
#         self.pushButton_hotel_frequent.setCheckable(True)
#         self.pushButton_hotel_frequent.clicked[bool].connect(self.hotelFrequent)
#
#         self.verticalLayout_2.addWidget(self.pushButton_hotel_frequent)
#
#         self.pushButton_hotel_contrast = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
#         self.pushButton_hotel_contrast.setObjectName("pushButton_hotel_contrast")
#         self.pushButton_hotel_contrast.setCheckable(True)
#         self.pushButton_hotel_contrast.clicked[bool].connect(self.hotelContrast)
#         self.verticalLayout_2.addWidget(self.pushButton_hotel_contrast)
#
#         self.label_2 = QtWidgets.QLabel(Form)
#         self.label_2.setGeometry(QtCore.QRect(110, 200, 181, 51))
#         self.label_2.setObjectName("label_2")
#         self.label_3 = QtWidgets.QLabel(Form)
#         self.label_3.setGeometry(QtCore.QRect(680, 220, 81, 16))
#         self.label_3.setObjectName("label_3")
#
#         self.retranslateUi(Form)
#         QtCore.QMetaObject.connectSlotsByName(Form)
#
#     def retranslateUi(self, Form):
#         _translate = QtCore.QCoreApplication.translate
#         Form.setWindowTitle(_translate("Form", "Form"))
#         self.label.setText(_translate("Form", "图像内容识别技术和对比挖掘在网站分析中的应用研究系统"))
#         self.pushButton_office_dataget.setText(_translate("Form", "数据获取"))
#         self.pushButton_datastat.setText(_translate("Form", "数据统计"))
#         self.pushButton_cluster.setText(_translate("Form", "聚类分析"))
#         self.pushButton_frequent.setText(_translate("Form", "频繁项集挖掘"))
#         self.pushButton_contrast.setText(_translate("Form", "对比挖掘"))
#         self.pushButton_hotel_dataget.setText(_translate("Form", "数据获取"))
#         self.pushButton_hotel_datastat.setText(_translate("Form", "数据统计"))
#         self.pushButton_hotel_cluster.setText(_translate("Form", "聚类分析"))
#         self.pushButton_hotel_frequent.setText(_translate("Form", "频繁项集挖掘"))
#         self.pushButton_hotel_contrast.setText(_translate("Form", "对比挖掘"))
#         self.label_2.setText(_translate("Form", "共享型和开放式办公室图像对比"))
#         self.label_3.setText(_translate("Form", "酒店图像对比"))
#
#     def officeDataGet(self,p):
#         if p:
#             os.system("python frame_office_dataget.py")
#
#     def officeDataStat(self,p):
#         if p:
#             os.system("python frame_office_stat.py")
#
#     def officeCluster_DBI(self,p):
#         if p:
#             os.system("python frame_office_clustering.py")
#
#
#     def officeFrequent(self,p):
#         if p:
#             os.system("python frame_office_frequent.py")
#
#     def officeContrast(self,p):
#         if p:
#             os.system("python frame_office_contrast.py")
#
#
#
#     def hotelDataGet(self,p):
#         if p:
#             os.system("python frame_hotel_dataget.py")
#
#     def hotelDataStat(self,p):
#         if p:
#             os.system("python frame_hotel_stat.py")
#
#     def hotelCluster_DBI(self,p):
#         if p:
#             os.system("python frame_hotel_clustering.py")
#
#
#     def hotelFrequent(self,p):
#         if p:
#             os.system("python frame_hotel_frequent.py")
#
#     def hotelContrast(self,p):
#         if p:
#             os.system("python frame_hotel_contrast.py")
#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow=QtWidgets.QMainWindow()
#     ui = Ui_Form()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec())
