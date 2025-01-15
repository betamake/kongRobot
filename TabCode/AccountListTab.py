from PySide6.QtWidgets import (QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem,
                              QHeaderView, QHBoxLayout, QPushButton, QMessageBox)
from PySide6.QtCore import Qt
import requests
import json

class AccountListTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.setup_connections()
        # 初始加载数据
        self.refresh_data()

    def setup_ui(self):
        """设置UI"""
        # 创建主布局
        self.main_layout = QVBoxLayout(self)

        # 创建按钮布局
        self.button_layout = QHBoxLayout()

        # 创建按钮
        self.add_account_button = QPushButton("添加账号")
        self.delete_account_button = QPushButton("删除账号")
        self.refresh_button = QPushButton("刷新")

        # 添加按钮到布局
        self.button_layout.addWidget(self.add_account_button)
        self.button_layout.addWidget(self.delete_account_button)
        self.button_layout.addWidget(self.refresh_button)
        self.button_layout.addStretch()

        # 创建表格
        self.table = QTableWidget()
        self.setup_table()

        # 将所有元素添加到主布局
        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addWidget(self.table)

    def setup_table(self):
        """设置表格"""
        # 设置列数和标题
        self.headers = [
            "序号", "浏览器ID", "注册账号邮箱", "邮箱密码", "登录密码",
            "注册名字", "A地址", "S地址", "C地址", "助记词"
        ]
        self.table.setColumnCount(len(self.headers))
        self.table.setHorizontalHeaderLabels(self.headers)

        # 设置表格属性
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)

        # 设置列宽
        header = self.table.horizontalHeader()
        for i in range(len(self.headers)):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

    def setup_connections(self):
        """设置信号连接"""
        self.add_account_button.clicked.connect(self.add_account)
        self.delete_account_button.clicked.connect(self.delete_account)
        self.refresh_button.clicked.connect(self.refresh_data)

    def fetch_account_data(self):
        """从接口获取账号数据"""
        try:
            # 设置API接口地址
            url = "http://localhost:8000/api/accounts"  # 替换为实际的API地址

            # 发送GET请求
            response = requests.get(url)
            response.raise_for_status()  # 检查请求是否成功

            # 解析JSON响应
            data = response.json()

            # 检查响应数据格式
            if not isinstance(data, list):
                raise ValueError("Invalid data format")

            return data

        except requests.RequestException as e:
            QMessageBox.critical(self, "错误", f"获取数据失败: {str(e)}")
            return None
        except json.JSONDecodeError as e:
            QMessageBox.critical(self, "错误", f"解析数据失败: {str(e)}")
            return None
        except Exception as e:
            QMessageBox.critical(self, "错误", f"发生未知错误: {str(e)}")
            return None

    def update_table(self, data):
        """更新表格数据"""
        try:
            # 清空表格
            self.table.setRowCount(0)

            if not data:
                return

            # 添加新数据
            for row_idx, account in enumerate(data):
                self.table.insertRow(row_idx)

                # 设置序号
                self.table.setItem(row_idx, 0, QTableWidgetItem(str(row_idx + 1)))

                # 设置其他字段
                columns = {
                    1: "browser_id",
                    2: "email",
                    3: "email_password",
                    4: "login_password",
                    5: "username",
                    6: "address_a",
                    7: "address_s",
                    8: "address_c",
                    9: "mnemonic"
                }

                for col_idx, field in columns.items():
                    value = account.get(field, "")
                    item = QTableWidgetItem(str(value))
                    self.table.setItem(row_idx, col_idx, item)

        except Exception as e:
            QMessageBox.critical(self, "错误", f"更新表格失败: {str(e)}")

    def refresh_data(self):
        """刷新数据"""
        try:
            # 显示加载提示
            self.refresh_button.setEnabled(False)
            self.refresh_button.setText("正在刷新...")

            # 获取数据
            # data = self.fetch_account_data()
            data = {}

            # 更新表格
            if data is not None:
                self.update_table(data)
                # QMessageBox.information(self, "成功", "数据刷新成功！")

        except Exception as e:
            QMessageBox.critical(self, "错误", f"刷新数据失败: {str(e)}")

        finally:
            # 恢复按钮状态
            self.refresh_button.setEnabled(True)
            self.refresh_button.setText("刷新")

    def add_account(self):
        """添加账号"""
        # TODO: 实现添加账号功能
        pass

    def delete_account(self):
        """删除账号"""
        try:
            # 获取选中的行
            current_row = self.table.currentRow()
            if current_row < 0:
                QMessageBox.warning(self, "警告", "请先选择要删除的账号！")
                return

            # 获取账号信息
            browser_id = self.table.item(current_row, 1).text()

            # 确认删除
            reply = QMessageBox.question(self, "确认删除",
                                       f"确定要删除浏览器ID为 {browser_id} 的账号吗？",
                                       QMessageBox.Yes | QMessageBox.No)

            if reply == QMessageBox.Yes:
                # TODO: 调用删除API
                # url = f"http://localhost:8000/api/accounts/{browser_id}"
                # response = requests.delete(url)
                # response.raise_for_status()

                # 刷新数据
                self.refresh_data()

        except Exception as e:
            QMessageBox.critical(self, "错误", f"删除账号失败: {str(e)}")
