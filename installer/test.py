import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal

from main import Alert

class Foo(QtWidgets.QMainWindow):

    # Define a new signal called 'trigger' that has no arguments.
    trigger = pyqtSignal()

    def connect_and_emit_trigger(self):
        # Connect the trigger signal to a slot.
        self.trigger.connect(self.handle_trigger)

        # Emit the signal.
        self.trigger.emit()

    def handle_trigger(self):
        # Show that the slot has been called.

        print ("trigger signal received")

if __name__ == "__main__":
    currentExitCode = Alert.EXIT_CODE_REBOOT
    while currentExitCode == Alert.EXIT_CODE_REBOOT:
        a = QtWidgets.QApplication(sys.argv)
        w = Foo()
        w.show()
        currentExitCode = a.exec_()
        a = None 