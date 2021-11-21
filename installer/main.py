from PyQt5 import QtWidgets, uic, QtCore, QtGui
import queue as q
from PyQt5.QtCore import Q_ARG, QCoreApplication, QObject, QTextStreamManipulator, QThread, QWaitCondition, pyqtSignal, pyqtSlot
import sys
import os
import platform
import getpass
from PyQt5.QtGui import QPixmap
import requests
import time




global app
app = None

def isNetwork()->bool:
    try:
        request = requests.get('http://www.google.com', timeout=5)
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        return False

global path
path = os.path.abspath(os.path.dirname(__file__))

def PathToFiles()->str:
    if platform.system() == 'Windows':
        path = str(r"c:\Users\{}\PCCorp".format(getpass.getuser()))
        
        return path
    else:
        return f"/Users/{getpass.getuser()}/PCCorp"

def pathToUi()->str:
    global path
    if platform.system() == 'Windows':
        thePath = path+r"\screens\ui\windows"
        print()
        
        return thePath
    else:
        return path+"/screens/ui/unix"



class Connect(QtWidgets.QMainWindow):
    window_closed = pyqtSignal()
    def __init__(self):
        
        super(Connect, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi(f'{pathToUi()}/ConnexionScreen.ui', self) # Load the .ui file
        self.cb = self.checkBox
        self.setFixedWidth(700)
        self.setFixedHeight(320)
        self.cb.toggled.connect(self.toggled)

        try:
            testFile = open(f'{PathToFiles()}/CasioModules/ToDo.txt ')
            testFile.close()
            self.checkBox.setEnabled(False)
        except FileNotFoundError :
            self.cb.setEnabled(False)

            self.cb.setToolTip('You must run installer online')
        
        self.pb = self.pushButton
        self.pb.clicked.connect(self.connectPushed)
        
        self.label_2.setPixmap(QtGui.QPixmap(f"{path}/screens/images/logo.png"))
        self.label_4.setText('<a href=\"https://github.com/P-C-Corp/CasioModules">See Documentation</a>')
        
        
        self.show()

    def toggled(self):
        self.cb.setChecked(QtCore.Qt.Checked)
        
    def connectPushed(self, event):
        self.win = Connexion()
        
        self.win.show()
        self.close()
        
    def closeWindow(self, event):
        self.window_closed.emit()
        event.accept()




class Connexion(QtWidgets.QMainWindow):
    window_closed = pyqtSignal()
    
    
    def __init__(self):

        
        super(Connexion, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi(f'{pathToUi()}/connecting.ui', self) # Load the .ui file

        self.label_2.setPixmap(QtGui.QPixmap(f"{path}/screens/images/logo.png"))
        
        self.progressBar.setValue(0)
        
        

        
        self.show()
        self.startProgressBar()

    def startProgressBar(self):
        self.thread = MyThread()
        self.thread.change_value.connect(self.progressBar.setValue)
        self.thread.isConnection.connect(self.showAlert)
        self.thread.next.connect(self.nextStep)
        self.thread.start()

    def nextStep(self, log):
        print(log)
        self.win = Install()
        
        self.win.show()
        self.close()

    def connectPushed(self, event):
        self.win = Connexion()
        
        self.win.show()
        self.close()

    def showAlert(self, isWorking):
        ERROR = self.Alert()
        if ERROR == 1024:
            self.win = Connect()
            self.win.show()
            self.close()
        else:
            self.close()
            QCoreApplication.instance().quit()

    
    def closeWindow(self, event):
        self.window_closed.emit()
        event.accept()


    def Alert(self):
        msg = QtWidgets.QMessageBox()
        msg.setGeometry(750, 500, 400, 100)
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Error :")
        msg.setInformativeText("Unable to fetch internet connection, please check your connection and try again.")
        msg.setWindowTitle("Interner Error")
        msg.setDetailedText("Please report this issue at <github issues> if it persists.")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close)
        msg.buttonClicked.connect(self.press)
        return msg.exec_()

    def press(self, button):
        pass



class MyThread(QThread):
    isConnection = pyqtSignal(bool)
    change_value = pyqtSignal(int)
    next = pyqtSignal(str)
    def run(self):
        
        for i in range(0, 101):
            self.change_value.emit(i)
            if i == 40:
                test = isNetwork()
                if not test :
                    self.isConnection.emit(False)
                    break
                else:
                    pass
            if i == 100:
                self.next.emit("Connected")


            time.sleep(0.02)


class Install(QtWidgets.QMainWindow):
    
    window_closed = pyqtSignal()
    
    
    def __init__(self):
        super(Install, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi(f'{pathToUi()}/WaitForInstall.ui', self) # Load the .ui file
        self.label.setPixmap(QtGui.QPixmap(f"{path}/screens/images/logo.png"))
        self.setFixedWidth(700)
        self.setFixedHeight(320)

        self.checkBox.setChecked(QtCore.Qt.Checked)
        self.comboBox.addItem('test')


        self.show()

    def closeWindow(self, event):
        self.window_closed.emit()
        event.accept()


if __name__ == "__main__":

    a = QtWidgets.QApplication(sys.argv)
    w = Connect()
    w.show()
    currentExitCode = a.exec_()
    a = None 