from PyQt5 import QtWidgets, uic, QtCore
import sys
import os
import platform
import getpass
import requests


global app
app = None

def isNetwork()->bool:
    try:
        request = requests.get('http://www.google.com', timeout=5)
        print("Connected to the Internet")
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("No internet connection.")

def PathToFiles()->str:
    if platform.system() == 'Windows':
        path = str(r"c:\Users\{}\PCCorp".format(getpass.getuser()))
        return path
    else:
        return f"/Users/{getpass.getuser()}/PCCorp"

path = os.path.abspath(os.path.dirname(__file__))

class Connect(QtWidgets.QMainWindow):
    def __init__(self):
        
        super(Connect, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi(f'{path}/screens/ui/ConnexionScreen.ui', self) # Load the .ui file
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
        
    def connectPushed(self):
        self.pb.setEnabled(False)
        print(widgets.currentIndex())
        widgets.setCurrentIndex(widgets.currentIndex()+1)
        


class Connexion(QtWidgets.QMainWindow):
    def __init__(self):
        
        super(Connexion, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi(f'{path}/screens/ui/connecting.ui', self) # Load the .ui file

        


        self.show()

    def load(self):
        for i in range(1, 101):
            self.progressBar.setValue(i)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication

    widgets = QtWidgets.QStackedWidget()
    connect = Connect()
    connexion = Connexion()

    widgets.addWidget(connect)
    widgets.addWidget(connexion)
    window = Connect() # Create an instance of our class
    app.exec_() # Start the application