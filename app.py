import sys
from PySide6 import QtWidgets

from service.keyFrame import KeyWidget
from service.login import MyWidget

# pyside6-uic ./widgets/login.ui > ./forms/login.py
if __name__ == '__main__':

    app = QtWidgets.QApplication([])
    widget = KeyWidget()
    widget.show()

    widget2 = MyWidget()
    widget2.show()
    sys.exit(app.exec())

