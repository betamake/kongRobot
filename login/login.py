from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import Slot
from ui_LoginForm import Ui_Form
from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import QUrl
import requests  # 导入 requests 库
import sys
import os
class MainLogin(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initialize()
        self.setup_connections()

    def initialize(self):
        """初始化函数"""
        self.setWindowTitle("登录")
        # 设置注册和忘记密码的URL
        self.register_url = "http://your-register-url.com"
        self.forget_password_url = "http://your-forget-password-url.com"

    def setup_connections(self):
        """设置信号连接"""
        self.ui.loginPushButton.clicked.connect(self.on_login_clicked)
        self.ui.registerPushButton.clicked.connect(self.on_register_clicked)
        self.ui.ForgotPasswordPushButton.clicked.connect(self.on_forget_password_clicked)

    @Slot()
    def on_login_clicked(self):
        """登录按钮点击处理"""
        username = self.ui.usernameLineEdit.text().strip()
        password = self.ui.passwordLineEdit.text().strip()

        # 验证输入
        if not username or not password:
            QMessageBox.warning(self, "输入错误", "用户名和密码不能为空！")
            return

        try:
            # 发送登录请求
            # response = requests.post(
            #     "http://your-api-url/login",
            #     json={
            #         "username": username,
            #         "password": password
            #     }
            # )
            status_code=200

            if status_code == 200:
                QMessageBox.information(self, "成功", "登录成功！")
                # 创建并显示主窗口
                sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
                from widget import MainWidget
                self.main_widget = MainWidget()
                self.main_widget.show()
                # 关闭登录窗口
                self.close()
            else:
                QMessageBox.warning(self, "错误", "用户名或密码错误！")

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "错误", f"网络错误：{str(e)}")

    @Slot()
    def on_register_clicked(self):
        """注册按钮点击处理"""
        QDesktopServices.openUrl(QUrl(self.register_url))

    @Slot()
    def on_forget_password_clicked(self):
        """忘记密码按钮点击处理"""
        QDesktopServices.openUrl(QUrl(self.forget_password_url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainLogin()
    window.show()
    sys.exit(app.exec())
