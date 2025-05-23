# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather_app.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Form(object):
    def setupUi(self, Form):
        directory = os.path.dirname(os.path.abspath(__file__))
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(968, 538)
        Form.setStyleSheet("QWidget#Form{\n"
"    background-color:#e6e6fa;\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 270, 55, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalWidget = QtWidgets.QWidget(Form)
        self.verticalWidget.setGeometry(QtCore.QRect(-8, 10, 20, 20))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame1 = QtWidgets.QFrame(Form)
        self.frame1.setGeometry(QtCore.QRect(20, 20, 451, 501))
        self.frame1.setStyleSheet("QFrame#frame1 {\n"
"    border: 2px solid #ADD8E6;\n"
"    border-radius: 20px;\n"
"    background-color:#ADD8E6\n"
"}\n"
"")
        self.frame1.setFrameShape(QtWidgets.QFrame.Box)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame1.setLineWidth(2)
        self.frame1.setObjectName("frame1")
        self.label_judul = QtWidgets.QLabel(self.frame1)
        self.label_judul.setGeometry(QtCore.QRect(150, 20, 131, 51))
        self.label_judul.setStyleSheet("font: 12pt \"Arial\";\n"
"font-weight: bold;")
        self.label_judul.setAlignment(QtCore.Qt.AlignCenter)
        self.label_judul.setObjectName("label_judul")
        self.logo1 = QtWidgets.QLabel(self.frame1)
        self.logo1.setGeometry(QtCore.QRect(150, 80, 131, 121))
        self.logo1.setText("")
        self.logo1.setPixmap(QtGui.QPixmap(os.path.join(directory, "images/weather.png")))
        self.logo1.setScaledContents(True)
        self.logo1.setObjectName("logo1")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame1)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 230, 282, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_pilihSuhu = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_pilihSuhu.setStyleSheet("font: 8pt \"Arial\";\n"
"font-weight: bold;")
        self.label_pilihSuhu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pilihSuhu.setObjectName("label_pilihSuhu")
        self.horizontalLayout.addWidget(self.label_pilihSuhu)
        self.comboBox_suhu = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_suhu.setObjectName("comboBox_suhu")
        self.comboBox_suhu.addItem("")
        self.comboBox_suhu.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_suhu)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame1)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(130, 290, 189, 107))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.search = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.search.setStyleSheet("border: 2px solid #3498db;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: white;\n"
"")
        self.search.setObjectName("search")
        self.verticalLayout_2.addWidget(self.search)
        self.btn_search = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_search.setStyleSheet("QPushButton {\n"
"    border: 2px solid #3498db;\n"
"    border-radius: 10px;\n"
"    font: 8pt \"Arial\";\n"
"    padding: 5px;\n"
"    background-color: #FFC1DA;\n"
"    font-weight : bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #CCCCFF;\n"
"}\n"
"\n"
"")
        self.btn_search.setCheckable(False)
        self.btn_search.setObjectName("btn_search")
        self.verticalLayout_2.addWidget(self.btn_search)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 410, 297, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_nama = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_nama.setStyleSheet("font: 10pt \"Arial\";\n"
"font-weight: bold;\n"
"")
        self.label_nama.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nama.setObjectName("label_nama")
        self.verticalLayout_3.addWidget(self.label_nama)
        self.label_nim = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_nim.setStyleSheet("font: 10pt \"Arial\";\n"
"font-weight: bold;\n"
"")
        self.label_nim.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nim.setObjectName("label_nim")
        self.verticalLayout_3.addWidget(self.label_nim)
        self.frame2 = QtWidgets.QFrame(Form)
        self.frame2.setGeometry(QtCore.QRect(490, 20, 461, 501))
        self.frame2.setStyleSheet("QFrame#frame2 {\n"
"    border: 2px solid#b3cee5;\n"
"    border-radius: 20px;\n"
"    background-color:#b3cee5;\n"
"}\n"
"")
        self.frame2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame2.setLineWidth(2)
        self.frame2.setObjectName("frame2")
        self.label_date = QtWidgets.QLabel(self.frame2)
        self.label_date.setGeometry(QtCore.QRect(100, 20, 261, 31))
        self.label_date.setStyleSheet("font: 12pt \"Calibri\";\n"
"font-weight: bold;")
        self.label_date.setAlignment(QtCore.Qt.AlignCenter)
        self.label_date.setObjectName("label_date")
        self.logo2 = QtWidgets.QLabel(self.frame2)
        self.logo2.setGeometry(QtCore.QRect(160, 60, 151, 141))
        self.logo2.setText("")
        self.logo2.setPixmap(QtGui.QPixmap(os.path.join(directory, "images/weather-forecast.png")))
        self.logo2.setScaledContents(True)
        self.logo2.setObjectName("logo2")
        self.label_cuaca = QtWidgets.QLabel(self.frame2)
        self.label_cuaca.setGeometry(QtCore.QRect(120, 210, 231, 31))
        self.label_cuaca.setStyleSheet("font: 12pt \"Calibri\";\n"
"font-weight: bold;")
        self.label_cuaca.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cuaca.setObjectName("label_cuaca")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 260, 401, 31))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_suhu2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_suhu2.setStyleSheet("font: 9pt \"Calibri\";")
        self.label_suhu2.setObjectName("label_suhu2")
        self.gridLayout_2.addWidget(self.label_suhu2, 0, 2, 1, 1)
        self.label_kosong1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_kosong1.setText("")
        self.label_kosong1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_kosong1.setObjectName("label_kosong1")
        self.gridLayout_2.addWidget(self.label_kosong1, 0, 1, 1, 1)
        self.label_suhu1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_suhu1.setStyleSheet("font: 9pt \"Calibri\";\n"
"")
        self.label_suhu1.setObjectName("label_suhu1")
        self.gridLayout_2.addWidget(self.label_suhu1, 0, 0, 1, 1)
        self.label_kosong2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_kosong2.setText("")
        self.label_kosong2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_kosong2.setObjectName("label_kosong2")
        self.gridLayout_2.addWidget(self.label_kosong2, 0, 3, 1, 1)
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 330, 461, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_kosong3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_kosong3.setStyleSheet("font: 9pt \"Calibri\";\n"
"font-weight: bold;")
        self.label_kosong3.setText("")
        self.label_kosong3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kosong3.setObjectName("label_kosong3")
        self.gridLayout.addWidget(self.label_kosong3, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.label_kosong6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_kosong6.setFont(font)
        self.label_kosong6.setText("")
        self.label_kosong6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kosong6.setObjectName("label_kosong6")
        self.gridLayout.addWidget(self.label_kosong6, 1, 6, 1, 1)
        self.label_kosong5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_kosong5.setStyleSheet("font: 9pt \"Calibri\";\n"
"font-weight: bold;")
        self.label_kosong5.setText("")
        self.label_kosong5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kosong5.setObjectName("label_kosong5")
        self.gridLayout.addWidget(self.label_kosong5, 1, 4, 1, 1)
        self.label_kosong4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_kosong4.setStyleSheet("font: 9pt \"Calibri\";\n"
"font-weight: bold;")
        self.label_kosong4.setText("")
        self.label_kosong4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kosong4.setObjectName("label_kosong4")
        self.gridLayout.addWidget(self.label_kosong4, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 5, 1, 1)
        self.label_pressure = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_pressure.setStyleSheet("font: 9pt \"Calibri\";")
        self.label_pressure.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pressure.setObjectName("label_pressure")
        self.gridLayout.addWidget(self.label_pressure, 0, 4, 1, 1)
        self.label_cloudiness = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_cloudiness.setStyleSheet("font: 9pt \"Calibri\";")
        self.label_cloudiness.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cloudiness.setObjectName("label_cloudiness")
        self.gridLayout.addWidget(self.label_cloudiness, 0, 6, 1, 1)
        self.label_wind = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_wind.setStyleSheet("font: 9pt \"Calibri\";")
        self.label_wind.setAlignment(QtCore.Qt.AlignCenter)
        self.label_wind.setObjectName("label_wind")
        self.gridLayout.addWidget(self.label_wind, 0, 2, 1, 1)
        self.label_humidity = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_humidity.setAlignment(QtCore.Qt.AlignCenter)
        self.label_humidity.setObjectName("label_humidity")
        self.gridLayout.addWidget(self.label_humidity, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 3, 1, 1)
        self.btn_exit = QtWidgets.QPushButton(self.frame2)
        self.btn_exit.setGeometry(QtCore.QRect(360, 460, 91, 30))
        self.btn_exit.setStyleSheet("QPushButton {\n"
"    border: 2px solid #3498db;\n"
"    background-color:  #A3D1C6;\n"
"    border-radius: 10px; \n"
"    padding: 5px 15px;\n"
"    font: 8pt \"Arial\";\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #CCCCFF;\n"
"}\n"
"\n"
"\n"
"")
        self.btn_exit.setObjectName("btn_exit")
        self.checkBox_info = QtWidgets.QCheckBox(self.frame2)
        self.checkBox_info.setGeometry(QtCore.QRect(130, 310, 187, 20))
        self.checkBox_info.setStyleSheet("font: 75 8pt \"Arial\";\n"
"font-weight: bold;")
        self.checkBox_info.setObjectName("checkBox_info")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_judul.setText(_translate("Form", "Weather App"))
        self.label_pilihSuhu.setText(_translate("Form", "Select Temperature Unit :"))
        self.comboBox_suhu.setCurrentText(_translate("Form", "Celcius"))
        self.comboBox_suhu.setItemText(0, _translate("Form", "Celcius"))
        self.comboBox_suhu.setItemText(1, _translate("Form", "Fahrenheit"))
        self.btn_search.setText(_translate("Form", "SEARCH"))
        self.label_nama.setText(_translate("Form", "MUHAMMAD FIQRI JORDY ARDIANTO"))
        self.label_nim.setText(_translate("Form", "F1D022145"))
        self.label_date.setText(_translate("Form", "Today\'s Date"))
        self.label_cuaca.setText(_translate("Form", "Please search for a location "))
        self.label_suhu2.setText(_translate("Form", "Max Temperature : "))
        self.label_suhu1.setText(_translate("Form", "Min Temperature : "))
        self.label_pressure.setText(_translate("Form", "Air Pressure"))
        self.label_cloudiness.setText(_translate("Form", "Cloudiness"))
        self.label_wind.setText(_translate("Form", "Wind Speed"))
        self.label_humidity.setText(_translate("Form", "Humidity"))
        self.btn_exit.setText(_translate("Form", "EXIT"))
        self.checkBox_info.setText(_translate("Form", "Show Details Information"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
