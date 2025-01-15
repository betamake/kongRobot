# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QMessageBox,QVBoxLayout, QPushButton)
from PySide6.QtGui import QPixmap, QIcon
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
from PySide6.QtCore import Qt, Slot  # 添加 Slot 导入
from TabCode.SystemSettingTab import SystemSettingTab
from TabCode.AccountListTab import AccountListTab
from TaskConfiguration.TaskConfiguration import MainTaskConfiguration
from TabCode.TaskExecutionTab import TaskExecutionTab
class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.initialize()
        self.setup_systemSettingTab()
        self.setup_accountListTab()
        self.setup_connections()

    def initialize(self):
        """初始化函数，用于设置窗口标题、加载图片等"""
        self.setWindowTitle("disoMTech")  # 设置窗口标题

    def setup_systemSettingTab(self):
        """设置各个标签页"""
        # 创建 SystemSettingTab 实例
        self.system_setting_tab = SystemSettingTab(self)
        self.ui.tabWidget.addTab(self.system_setting_tab, "系统设置")
    def setup_accountListTab(self):
        """设置标签页"""
        self.account_list_tab = AccountListTab(self)
        self.ui.tabWidget.addTab(self.account_list_tab, "账号列表")



    def setup_connections(self):
        """设置信号连接"""
        if hasattr(self.ui, 'TaskConfigurationPushButton'):
            button = self.ui.TaskConfigurationPushButton
            # 直接连接信号
            button.clicked.connect(self.on_button_clicked)

    @Slot()
    def on_button_clicked(self):
        """测试按钮点击"""
        self.show_task_configuration()

    def show_task_configuration(self):
        """显示任务配置窗口"""
        try:
            self.task_window = MainTaskConfiguration()
            # 连接任务选择信号
            self.task_window.task_selected.connect(self.handle_task_selected)
            self.task_window.show()
        except Exception as e:
            QMessageBox.critical(self, "错误", f"打开任务配置窗口时出错：{str(e)}")

    def handle_task_selected(self, selected_tasks):
        """处理选中的任务"""
        try:
            print(f"接收到的任务: {selected_tasks}")  # 调试输出

            # 确保是列表类型
            if not isinstance(selected_tasks, list):
                selected_tasks = [selected_tasks] if selected_tasks else []

            # 关闭任务配置窗口
            if hasattr(self, 'task_window'):
                self.task_window.close()

            # 创建任务执行标签页
            task_tab = TaskExecutionTab(tasks=selected_tasks)

            # 添加或更新任务执行标签页
            execution_tab_index = -1
            for i in range(self.ui.tabWidget.count()):
                if self.ui.tabWidget.tabText(i) == "任务执行":
                    execution_tab_index = i
                    break

            if execution_tab_index >= 0:
                self.ui.tabWidget.removeTab(execution_tab_index)

            # 添加新标签页
            self.ui.tabWidget.addTab(task_tab, "任务执行")
            self.ui.tabWidget.setCurrentWidget(task_tab)

        except Exception as e:
            print(f"处理任务选择时出错: {str(e)}")
            QMessageBox.critical(self, "错误", f"处理任务选择时出错：{str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec())
