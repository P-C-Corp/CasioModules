from PyQt5 import QtWidgets, uic, QtCore

from PyQt5.QtCore import QThread, pyqtSignal
import sys
import os
import platform
import getpass
import requests
import time

global app
app = None

def isNetwork()->bool:
    try:
        request = requests.get('http://www.google.com', timeout=5)
        print("Connected to the Internet")
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("No internet connection.")

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
        thePath = path+"/screens/ui/windows"
        return thePath
    else:
        return path+"/screens/ui/unix"

logo = "screens/images/logo.png"


class Connect(QtWidgets.QMainWindow):
    def __init__(self):
        
        super(Connect, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi(f'{pathToUi()}/ConnexionScreen.ui', self) # Load the .ui file
        self.cb = self.checkBox
        
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

        self.label_4.setText('<a href=\"https://github.com/P-C-Corp/CasioModules">See Documentation</a>')
        
        self.show()

    def toggled(self):
        self.cb.setChecked(QtCore.Qt.Checked)
        

        
        
        
    def connectPushed(self, event):
        self.win = Connexion()
        
        self.win.show()
        self.close()
        for i in range(1, 101):
            print(i)
            Connexion.Progress(Connexion())
        #event.accept()



class Connexion(QtWidgets.QMainWindow):
    window_closed = pyqtSignal()
    def __init__(self):
        
        super(Connexion, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi(f'{pathToUi()}/connecting.ui', self) # Load the .ui file

        self.progressBar.setValue(0)


        self.show()
        
    def Progress(self):
        pass
    
    def closeWindow(self, event):
        self.window_closed.emit()
        event.accept()
        

    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication

    widgets = QtWidgets.QStackedWidget()
    connect = Connect()
    connexion = Connexion()

    widgets.addWidget(connect)
    widgets.addWidget(connexion)
    window = Connect() # Create an instance of our class
    app.exec_() # Start the application