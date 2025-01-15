import os
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QCheckBox,
                              QScrollArea, QPushButton, QMessageBox)
from PySide6.QtCore import Qt
from PySide6.QtCore import Signal
class MainTaskConfiguration(QWidget):
    # 在类的开头定义信号
    task_selected = Signal(list)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("任务配置")
        self.resize(800, 600)
        self.setup_ui()
        self.setup_connections()
        self.load_tasks()


    def setup_ui(self):
        """设置UI"""
        # 创建主布局
        self.main_layout = QVBoxLayout(self)

        # 创建滚动区域
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        # 创建滚动区域的内容控件
        self.scroll_content = QWidget()
        self.task_layout = QVBoxLayout(self.scroll_content)

        # 设置滚动区域的内容
        self.scroll_area.setWidget(self.scroll_content)

        # 将滚动区域添加到主布局
        self.main_layout.addWidget(self.scroll_area)

        # 创建底部按钮
        self.button_layout = QHBoxLayout()
        self.select_all_button = QPushButton("全选")
        self.start_button = QPushButton("开始任务")

        self.button_layout.addStretch()
        self.button_layout.addWidget(self.select_all_button)
        self.button_layout.addWidget(self.start_button)

        # 将按钮布局添加到主布局
        self.main_layout.addLayout(self.button_layout)

    def load_tasks(self):
        """加载任务列表"""
        try:
            # 获取Task文件夹的路径
            current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            task_folder = os.path.join(current_dir, "Task")

            # 检查文件夹是否存在
            if not os.path.exists(task_folder):
                # 尝试在其他位置查找
                alternative_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Task")
                print(f"尝试替代路径: {alternative_path}")

                if os.path.exists(alternative_path):
                    task_folder = alternative_path
                else:
                    QMessageBox.warning(self, "错误", f"Task文件夹不存在！\n已检查路径:\n{task_folder}\n{alternative_path}")
                    return

            # 遍历Task文件夹中的所有子文件夹
            task_folders = []
            for item in os.listdir(task_folder):
                item_path = os.path.join(task_folder, item)
                # 检查是否是文件夹且不以__开头
                if os.path.isdir(item_path) and not item.startswith('__'):
                    task_folders.append(item)

            # 如果没有找到任务文件夹
            if not task_folders:
                checkbox = QCheckBox("没有找到任务")
                checkbox.setEnabled(False)
                self.task_layout.addWidget(checkbox)
                return

            # 添加找到的任务
            for task_name in sorted(task_folders):  # 排序任务名称
                checkbox = QCheckBox(task_name)
                self.task_layout.addWidget(checkbox)

            print(f"找到 {len(task_folders)} 个任务文件夹")

        except Exception as e:
            print(f"加载任务时出错：{str(e)}")
            QMessageBox.critical(self, "错误", f"加载任务时出错：{str(e)}")

    def setup_connections(self):
        """设置信号连接"""
        self.select_all_button.clicked.connect(self.toggle_all_tasks)
        self.start_button.clicked.connect(self.start_tasks)

    def toggle_all_tasks(self):
        """切换全选/取消全选"""
        # 获取所有复选框
        checkboxes = [
            self.task_layout.itemAt(i).widget()
            for i in range(self.task_layout.count())
            if isinstance(self.task_layout.itemAt(i).widget(), QCheckBox)
        ]
        # 检查是否全部选中
        all_checked = all(cb.isChecked() for cb in checkboxes)
        # 切换状态
        for cb in checkboxes:
            cb.setChecked(not all_checked)
        # 更新按钮文本
        self.select_all_button.setText("取消全选" if not all_checked else "全选")

    def start_tasks(self):
        """开始执行选中的任务"""
        try:
            selected_tasks = [
                self.task_layout.itemAt(i).widget().text()
                for i in range(self.task_layout.count())
                if isinstance(self.task_layout.itemAt(i).widget(), QCheckBox)
                and self.task_layout.itemAt(i).widget().isChecked()
            ]

            if not selected_tasks:
                QMessageBox.warning(self, "警告", "请至少选择一个任务！")
                return

            print(f"Selected tasks: {selected_tasks}")  # 调试输出

            # 发送选中的任务列表
            self.task_selected.emit(selected_tasks)

            # 关闭窗口
            self.close()

        except Exception as e:
            print(f"Error in start_tasks: {str(e)}")  # 调试输出
            QMessageBox.critical(self, "错误", f"选择任务时出错：{str(e)}")
