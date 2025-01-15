from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                              QLabel, QLineEdit, QMessageBox, QGroupBox,
                              QGridLayout)
from PySide6.QtCore import Qt, Slot
from .TaskConfiguration import MainTaskConfiguration
import requests

class SystemSettingTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.setup_connections()

    def setup_ui(self):
        """设置UI"""
        # 创建主布局
        self.main_layout = QVBoxLayout(self)

        # 创建各个功能组
        self.create_biter_settings_group()
        self.create_other_settings_group()

        # 添加到主布局
        self.main_layout.addWidget(self.biter_settings_group)
        self.main_layout.addWidget(self.other_settings_group)
        self.main_layout.addStretch()



    def create_biter_settings_group(self):
        """创建比特设置组"""
        self.biter_settings_group = QGroupBox("比特设置")
        layout = QGridLayout()

        # 创建端口设置
        self.biter_port_label = QLabel("比特端口:")
        self.biter_port_input = QLineEdit()
        self.biter_port_input.setText("54345")
        self.biter_test_button = QPushButton("测试连接")

        # 设置样式
        self.biter_test_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)

        # 添加到布局
        layout.addWidget(self.biter_port_label, 0, 0)
        layout.addWidget(self.biter_port_input, 0, 1)
        layout.addWidget(self.biter_test_button, 0, 2)

        self.biter_settings_group.setLayout(layout)

    def create_other_settings_group(self):
        """创建其他设置组"""
        self.other_settings_group = QGroupBox("其他设置")
        layout = QGridLayout()

        # 创建其他设置控件
        self.proxy_label = QLabel("代理设置:")
        self.proxy_input = QLineEdit()
        self.proxy_input.setPlaceholderText("请输入代理地址")

        self.timeout_label = QLabel("超时设置:")
        self.timeout_input = QLineEdit()
        self.timeout_input.setPlaceholderText("请输入超时时间(秒)")

        # 添加到布局
        layout.addWidget(self.proxy_label, 0, 0)
        layout.addWidget(self.proxy_input, 0, 1)
        layout.addWidget(self.timeout_label, 1, 0)
        layout.addWidget(self.timeout_input, 1, 1)

        self.other_settings_group.setLayout(layout)

    def setup_connections(self):
        """设置信号连接"""

        # 比特设置
        self.biter_test_button.clicked.connect(self.test_biter_connection)

    @Slot()
    def test_biter_connection(self):
        """测试比特连接"""
        try:
            port = self.biter_port_input.text().strip()
            if not port:
                QMessageBox.warning(self, "警告", "请输入端口号")
                return

            url = f"http://127.0.0.1:{port}/health"
            print(f"发送 POST 请求到: {url}")

            try:
                response = requests.post(url)
                response.raise_for_status()

                result = response.json()
                if result.get("success", False):
                    QMessageBox.information(self, "成功", "连接比特成功！")
                    print("连接比特成功！")
                else:
                    QMessageBox.warning(self, "失败", "连接比特失败！")
                    print("连接比特失败！")
            except requests.exceptions.RequestException as e:
                QMessageBox.critical(self, "错误", f"请求失败: {str(e)}")
                print(f"请求失败: {e}")

        except Exception as e:
            QMessageBox.critical(self, "错误", f"测试连接时出错：{str(e)}")
