from PyQt5 import QtWidgets, uic
import sys
import os
import platform
import getpass

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
        cb = self.checkBox
        cb.toggle()
        try:
            testFile = open(f'{PathToFiles}/CasioModules/ToDo.txt ')
            testFile.close()
            self.checkBox.setEnabled(False)
        except FileNotFoundError :

            cb.setEnabled(False)
            cb.setText("Online mode required")
            print(cb.text)
        super(Connect, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi(f'{path}/screens/ui/ConnexionScreen.ui', self) # Load the .ui file
        self.label_4.setText('<a href=\"https://github.com/P-C-Corp/CasioModules">See Documentation</a>')
        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = Connect() # Create an instance of our class
    app.exec_() # Start the application