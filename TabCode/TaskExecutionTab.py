from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                              QTextEdit, QLabel, QGroupBox)
from PySide6.QtCore import Qt, Slot

class TaskExecutionTab(QWidget):
    def __init__(self, tasks=None, parent=None):
        super().__init__(parent)
        # 确保 tasks 是列表类型
        self.tasks = tasks if isinstance(tasks, list) else []
        print(f"TaskExecutionTab 接收到的任务: {self.tasks}")  # 调试输出
        self.setup_ui()
        self.setup_connections()
        self.update_task_info()


    def setup_ui(self):
        """设置UI"""
        # 创建主布局
        self.main_layout = QVBoxLayout(self)

        # 创建任务信息组
        self.create_task_info_group()

        # 创建控制按钮组
        self.create_control_group()

        # 创建日志显示组
        self.create_log_group()

        # 添加到主布局
        self.main_layout.addWidget(self.task_info_group)
        self.main_layout.addWidget(self.control_group)
        self.main_layout.addWidget(self.log_group)

    def create_task_info_group(self):
        """创建任务信息组"""
        self.task_info_group = QGroupBox("当前任务信息")
        layout = QVBoxLayout()

        # 任务列表显示
        self.task_info = QTextEdit()
        self.task_info.setReadOnly(True)
        self.task_info.setMaximumHeight(100)
        layout.addWidget(self.task_info)

        self.task_info_group.setLayout(layout)

    def create_control_group(self):
        """创建控制按钮组"""
        self.control_group = QGroupBox("任务控制")
        layout = QHBoxLayout()

        # 创建控制按钮
        self.start_button = QPushButton("开始任务")
        self.pause_button = QPushButton("暂停任务")
        self.stop_button = QPushButton("停止任务")

        # 设置按钮样式
        buttons = [self.start_button, self.pause_button, self.stop_button]
        for button in buttons:
            button.setMinimumWidth(120)
            button.setMinimumHeight(35)
            button.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    color: white;
                    border-radius: 5px;
                    padding: 8px;
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: #45a049;
                }
                QPushButton:pressed {
                    background-color: #3d8b40;
                }
                QPushButton:disabled {
                    background-color: #cccccc;
                }
            """)

        # 初始状态设置
        self.pause_button.setEnabled(False)
        self.stop_button.setEnabled(False)

        # 添加按钮到布局
        layout.addWidget(self.start_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.stop_button)
        layout.addStretch()

        self.control_group.setLayout(layout)

    def create_log_group(self):
        """创建日志显示组"""
        self.log_group = QGroupBox("执行日志")
        layout = QVBoxLayout()

        # 创建日志显示区域
        self.log_display = QTextEdit()
        self.log_display.setReadOnly(True)
        self.log_display.setStyleSheet("""
            QTextEdit {
                background-color: #f5f5f5;
                border: 1px solid #ddd;
                font-family: Consolas, Monaco, monospace;
                font-size: 12px;
            }
        """)

        layout.addWidget(self.log_display)
        self.log_group.setLayout(layout)

    def setup_connections(self):
        """设置信号连接"""
        self.start_button.clicked.connect(self.start_tasks)
        self.pause_button.clicked.connect(self.pause_tasks)
        self.stop_button.clicked.connect(self.stop_tasks)

    def update_task_info(self):
        """更新任务信息显示"""
        try:
            if not self.tasks:
                task_info = "没有选择任务"
            else:
                task_info = "当前选择的任务：\n" + "\n".join(f"- {task}" for task in self.tasks)

            print(f"更新任务信息: {task_info}")  # 调试输出
            self.task_info.setText(task_info)

        except Exception as e:
            print(f"更新任务信息时出错: {str(e)}")
            self.task_info.setText("更新任务信息时出错")

    def add_log(self, message):
        """添加日志"""
        self.log_display.append(message)

    @Slot()
    def start_tasks(self):
        """开始执行任务"""
        self.start_button.setEnabled(False)
        self.pause_button.setEnabled(True)
        self.stop_button.setEnabled(True)
        self.add_log("开始执行任务...")
        # TODO: 实现实际的任务执行逻辑

    @Slot()
    def pause_tasks(self):
        """暂停任务"""
        self.start_button.setEnabled(True)
        self.pause_button.setEnabled(False)
        self.add_log("任务已暂停")
        # TODO: 实现实际的暂停逻辑

    @Slot()
    def stop_tasks(self):
        """停止任务"""
        self.start_button.setEnabled(True)
        self.pause_button.setEnabled(False)
        self.stop_button.setEnabled(False)
        self.add_log("任务已停止")
        # TODO: 实现实际的停止逻辑
