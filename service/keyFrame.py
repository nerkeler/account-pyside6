from PySide6 import QtCore, QtWidgets, QtGui

from ui.forms.keyFrame import Ui_Form  # 导入ui_login.py


class KeyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()  # 实例化UI对象
        self.ui.setupUi(self)  # 初始化

    @QtCore.Slot()  # 槽函数用它装饰
    def confirm(self):  # 在Qt Designer中为登录按钮命名的槽函数；
        print("你点击了修改密码")

    @QtCore.Slot()  # 槽函数用它装饰
    def copy(self):  # 在Qt Designer中为登录按钮命名的槽函数；
        print("你点击了修改密码")
