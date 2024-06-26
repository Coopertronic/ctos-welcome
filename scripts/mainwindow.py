# This Python file uses the following encoding: utf-8
import sys
import subprocess
from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_home.clicked.connect(self.btn_home_action)
        self.ui.btn_about.clicked.connect(self.btn_about_action)

    def btn_home_action(self):
        print("HOME PAGE button pressed")
        subprocess.run(["xdg-open","https://coopertronic.co.uk/"])

    def btn_about_action(self):
        print("ABOUT button pressed")
        subprocess.Popen(["about",""])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
