import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QLineEdit

from ui.forms.login import Ui_Form# 导入ui_login.py


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()  # 实例化UI对象
        self.ui.setupUi(self)  # 初始化
        self.setFixedSize(self.width(), self.height())
        self.ui.passwordLabel.setEchoMode(QLineEdit.Password)

    @QtCore.Slot()  # 槽函数用它装饰
    def login(self):  # 在Qt Designer中为登录按钮命名的槽函数；
        print("你点击了登录")
        username = self.ui.usernameLabel.text()
        password = self.ui.passwordLabel.text()
        # password = encode_user(password)
        print(f'user:{username}\t password:{password}')
        # result = self.base.queryOne("1").fetchone()

        if username == "admin" and password == "password":
            sys.exit(app.exec())
        else:
            QtWidgets.QMessageBox.warning(self, "提示", "用户名或密码错误，请重试")

            self.ui.passwordLabel.clear()


    @QtCore.Slot()  # 槽函数用它装饰
    def update_password(self):  # 在Qt Designer中为登录按钮命名的槽函数；
        print("你点击了修改密码")


