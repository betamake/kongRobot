from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                              QTextEdit, QLabel, QGroupBox, QMessageBox)
from PySide6.QtCore import Qt, Slot
import importlib.util
import os
import sys
import asyncio
from playwright.async_api import async_playwright
class TaskExecutionTab(QWidget):
    def __init__(self, tasks=None, parent=None):
        super().__init__(parent)
        self.tasks = tasks if isinstance(tasks, list) else []
        self.running = False  # 任务运行状态

        # 修改Task目录路径获取方式
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.task_dir = os.path.join(current_dir, "TaskConfiguration", "Task")
        print(f"Task目录路径: {self.task_dir}")  # 调试输出

        if not os.path.exists(self.task_dir):
            print(f"警告: Task目录不存在: {self.task_dir}")
        else:
            print(f"Task目录存在，内容: {os.listdir(self.task_dir)}")

        if self.task_dir not in sys.path:
            sys.path.append(self.task_dir)

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
        if hasattr(self, 'log_display'):
            self.log_display.append(message)
        print(message)  # 同时打印到控制台
    @Slot()
    def start_tasks(self):
        """开始执行任务"""
        try:
            if not self.tasks:
                self.add_log("错误: 没有可执行的任务")
                return

            self.start_button.setEnabled(False)
            self.pause_button.setEnabled(True)
            self.stop_button.setEnabled(True)
            self.running = True

            # 创建事件循环
            self.loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self.loop)

            # 启动任务执行
            self.loop.run_until_complete(self.execute_tasks())

        except Exception as e:
            self.add_log(f"启动任务时出错: {str(e)}")
            self.reset_buttons()

    async def execute_tasks(self):
        """异步执行任务"""
        try:
            self.add_log("开始执行任务...")
            print(f"当前目录: {os.getcwd()}")
            print(f"Task目录: {self.task_dir}")

            # 使用 async with 确保正确关闭 playwright
            async with async_playwright() as playwright:
                for task_name in self.tasks:
                    if not self.running:
                        self.add_log("任务执行被停止")
                        break

                    try:
                        self.add_log(f"开始执行任务: {task_name}")
                        task_path = os.path.join(self.task_dir, task_name)
                        print(f"检查任务路径: {task_path}")

                        if os.path.exists(task_path):
                            # 检查main.py是否存在
                            main_file = os.path.join(task_path, 'main.py')
                            print(f"检查main文件: {main_file}")

                            if os.path.exists(main_file):
                                print(f"找到main文件: {main_file}")
                                # 直接导入并执行main.py
                                spec = importlib.util.spec_from_file_location("main", main_file)
                                module = importlib.util.module_from_spec(spec)
                                spec.loader.exec_module(module)
                                await module.run(playwright)
                                self.add_log(f"任务 {task_name} 执行完成")
                            else:
                                self.add_log(f"错误: 找不到main.py文件: {main_file}")
                        else:
                            self.add_log(f"任务目录不存在: {task_path}")
                            print(f"尝试的完整路径: {task_path}")

                    except Exception as e:
                        self.add_log(f"执行任务 {task_name} 时出错: {str(e)}")
                        import traceback
                        print(f"错误堆栈: {traceback.format_exc()}")
                        continue

            self.add_log("所有任务执行完成")

        except Exception as e:
            self.add_log(f"执行任务时出错: {str(e)}")
            import traceback
            print(f"错误堆栈: {traceback.format_exc()}")

        finally:
            self.reset_buttons()
    def reset_buttons(self):
        """重置按钮状态"""
        self.start_button.setEnabled(True)
        self.pause_button.setEnabled(False)
        self.stop_button.setEnabled(False)
        self.running = False

    @Slot()
    def stop_tasks(self):
        """停止任务"""
        try:
            self.running = False
            self.add_log("正在停止任务...")
            self.reset_buttons()
        except Exception as e:
            self.add_log(f"停止任务时出错: {str(e)}")

    @Slot()
    def pause_tasks(self):
        """暂停任务"""
        # TODO: 实现暂停功能
        self.add_log("暂停功能暂未实现")
        pass

    def add_log(self, message):
        """添加日志"""
        if hasattr(self, 'log_display'):
            self.log_display.append(message)
        print(message)  # 同时打印到控制台
    def load_task_modules(self):
        """加载任务模块"""
        try:
            # 获取Task文件夹的路径
            current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            task_folder = os.path.join(current_dir, "Task")

            for task_name in self.tasks:
                # 构建任务文件夹的完整路径
                task_dir = os.path.join(task_folder, task_name)

                if not os.path.exists(task_dir):
                    self.add_log(f"错误: 找不到任务文件夹 {task_dir}")
                    continue

                # 查找文件夹中的主文件（通常是 __init__.py 或 main.py）
                main_file = None
                for file_name in ['__init__.py', 'main.py']:
                    file_path = os.path.join(task_dir, file_name)
                    if os.path.exists(file_path):
                        main_file = file_path
                        break

                if not main_file:
                    self.add_log(f"错误: 在 {task_name} 中找不到主文件")
                    continue
        except Exception as e:
            self.add_log(f"加载任务模块时出错: {str(e)}")
