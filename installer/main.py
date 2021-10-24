from PyQt5 import QtWidgets, uic, QtCore, QtGui

from PyQt5.QtCore import QThread, pyqtSignal
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
        
        #event.accept()



class Connexion(QtWidgets.QMainWindow):
    window_closed = pyqtSignal()
    def __init__(self):
        
        super(Connexion, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi(f'{pathToUi()}/connecting.ui', self) # Load the .ui file
        self.label_2.setPixmap(QtGui.QPixmap(f"{path}/screens/images/logo.png"))
        self.progressBar.setValue(0)
        self.setFixedWidth(700)
        self.setFixedHeight(320)
        self.status = bool
        self.show()
        self.sendInvoice()
        

    def sendInvoice(self):
        runnable = InvoiceRunnable(self.progressBar)
        QtCore.QThreadPool.globalInstance().start(runnable)
    
    def closeWindow(self, event):
        self.window_closed.emit()
        event.accept()
        
    
class Alert(QtWidgets.QDialog):
    EXIT_CODE_REBOOT = -123
    window_closed = pyqtSignal()
    def __init__(self):
        
        super(Alert, self).__init__() # Call the inherited classes __init__ method
        self.setWindowTitle('Network Error')
        self.setFixedWidth(300)
        self.setFixedHeight(75)
        
        message = QtWidgets.QLabel("Can't find network,\nplease check your connexion and try again")
        
        self.button = QtWidgets.QPushButton('Ok')
        self.layout = QtWidgets.QGridLayout()
        self.layout.setColumnStretch( 300, 30)
        self.layout.addWidget(message)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    
    def RestartApp(self):
        QtGui.qApp.exit(self.EXIT_CODE_REBOOT )
    

class InvoiceRunnable(QtCore.QRunnable):
    def __init__(self, progressbar):
        QtCore.QRunnable.__init__(self)
        self.progressbar = progressbar

    def run(self):
        for i in range(1, 101):
            currentPercentage = i
            time.sleep(0.02)
            QtCore.QMetaObject.invokeMethod(self.progressbar, "setValue",
            QtCore.Qt.QueuedConnection,
            QtCore.Q_ARG(int, currentPercentage))
            if currentPercentage == 40:
                if not isNetwork():
                    #dlg = Alert()
                    
                    #dlg.exec()
                    break
                else:
                    print("connected")


if __name__ == "__main__":
    currentExitCode = Alert.EXIT_CODE_REBOOT
    while currentExitCode == Alert.EXIT_CODE_REBOOT:
        a = QtWidgets.QApplication(sys.argv)
        w = Connect()
        w.show()
        currentExitCode = a.exec_()
        a = None 