
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import paho.mqtt.client as mqtt
import time
import serial
import logging
import threading
import sys
import time
from PyQt5.QtCore import QTimer
import threading


def startScript():
    import publisher.py

x = threading.Thread(target=startScript)
x.start()




temperature = "0"
light = "0"

def on_message(client,userdata, message):
    
    global temperature
    if len(str(message.payload.decode("utf-8"))) >= 1:
        temperature = str(message.payload.decode("utf-8"))
        
        
def on_message2(client,userdata, message):
    
    global light
    if len(str(message.payload.decode("utf-8"))) >= 1:
        light = str(message.payload.decode("utf-8"))
        




class Ui_MainWindow(QMainWindow):
    
    def onClick(self):
        self.Terminal.clear()
        
    def onClickON(self):
        self.Terminal.append("LIGHTS ARE ON")
        self.client3.publish("setthelight069",1)
        self.label.setText("Lights are ON")
        
    def onClickOFF(self):
        self.Terminal.append("LIGHTS ARE OFF")
        self.client3.publish("setthelight069",0)
        self.label.setText("Lights are OFF")
        

    def getSensorValue(self):
        global temperature
        if temperature != "":
            self.Terminal.append("Temperature: " + temperature)
            self.Terminal.append("Light Level: " + light)
            self.label_7.setText(temperature)
            self.label_6.setText(light)
            time.sleep(1)
    
    def setupUi(self, MainWindow):
        
        
        
        broker = "broker.emqx.io"
        self.client = mqtt.Client("ature78678678678678")
        self.client.connect(broker,1883)
        self.client.subscribe("temperature0")
        self.client.on_message = on_message
        self.client.loop_start()
        
        self.client2 = mqtt.Client("ature7867867")
        self.client2.connect(broker,1883)
        self.client2.subscribe("light0")
        self.client2.on_message = on_message2
        self.client2.loop_start()
        
        self.client3 = mqtt.Client("ature786")
        self.client3.connect(broker,1883)
        
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 601)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 811, 571))
        self.widget.setStyleSheet("\n"
"\n"
"QWidget#widget{\n"
"\n"
"\n"
"background-color:\n"
"\n"
"qlineargradient(spread:pad, x1:0.744318, y1:0.302, x2:1, y2:0, stop:0 rgba(158, 113, 142, 255), stop:1 rgba(255, 255, 255, 255))\n"
"\n"
"\n"
"}")
        self.widget.setObjectName("widget")
        self.Terminal = QtWidgets.QTextBrowser(self.widget)
        self.Terminal.setGeometry(QtCore.QRect(10, 30, 360, 184))
        self.Terminal.setObjectName("Terminal")
        self.clearBtn = QtWidgets.QPushButton(self.widget)
        self.clearBtn.setGeometry(QtCore.QRect(10, 220, 75, 23))
        self.clearBtn.setObjectName("clearBtn")
        
        self.clearBtn.clicked.connect(self.onClick)
        
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(60, 470, 171, 31))
        self.label_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 440, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(230, 480, 71, 21))
        self.label_3.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.clearBtn_3 = QtWidgets.QPushButton(self.widget)
        self.clearBtn_3.setGeometry(QtCore.QRect(180, 440, 75, 23))
        self.clearBtn_3.setObjectName("clearBtn_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(390, 20, 121, 31))
        self.label_4.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(390, 60, 121, 31))
        self.label_5.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(490, 60, 41, 31))
        self.label_6.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(510, 20, 21, 31))
        self.label_7.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(10, 0, 121, 31))
        self.label_8.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(380, 100, 171, 61))
        self.widget_2.setStyleSheet("\n"
"QWidget#widget_2{\n"
"\n"
"\n"
"background-color:rgb(255, 255, 255)\n"
"\n"
"\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.clearBtn_2 = QtWidgets.QPushButton(self.widget_2)
        self.clearBtn_2.setGeometry(QtCore.QRect(10, 0, 75, 23))
        self.clearBtn_2.setObjectName("clearBtn_2")
        
        self.clearBtn_2.clicked.connect(self.onClickON)
        
        
        self.clearBtn_4 = QtWidgets.QPushButton(self.widget_2)
        self.clearBtn_4.setGeometry(QtCore.QRect(90, 0, 75, 23))
        self.clearBtn_4.setObjectName("clearBtn_2")
        
        self.clearBtn_4.clicked.connect(self.onClickOFF)
        
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(40, 30, 111, 21))
        self.label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.qTimer = QTimer()
        self.qTimer.setInterval(100)
        self.qTimer.timeout.connect(self.getSensorValue)
        self.qTimer.start()
        self.retranslateUi(MainWindow)
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clearBtn.setText(_translate("MainWindow", "CLEAR"))
        self.label_2.setText(_translate("MainWindow", "ALARM TIMER:"))
        self.lineEdit.setText(_translate("MainWindow", "2"))
        self.label_3.setText(_translate("MainWindow", "43"))
        self.clearBtn_3.setText(_translate("MainWindow", "Create"))
        self.label_4.setText(_translate("MainWindow", "Temperature:"))
        self.label_5.setText(_translate("MainWindow", "Light Level: "))
        self.label_6.setText(_translate("MainWindow", "30"))
        self.label_7.setText(_translate("MainWindow", "40"))
        self.label_8.setText(_translate("MainWindow", "Output"))
        self.clearBtn_2.setText(_translate("MainWindow", "ON"))
        self.clearBtn_4.setText(_translate("MainWindow", "OFF"))
        self.label.setText(_translate("MainWindow", "Light Status"))


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())