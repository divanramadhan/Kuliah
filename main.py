import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit, QPushButton, QCheckBox, QCalendarWidget, QMessageBox, QFileDialog
from PyQt5.QtCore import QDate

class ToDoListApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('To-Do List')
        self.setGeometry(300, 300, 400, 300)

        self.task_list = QListWidget()
        self.task_input = QLineEdit()
        self.date_input = QCalendarWidget()
        self.add_button = QPushButton('Add Task')
        self.remove_button = QPushButton('Remove Task')
        self.save_button = QPushButton('Save')

        vbox = QVBoxLayout()
        vbox.addWidget(self.task_list)

        hbox = QHBoxLayout()
        hbox.addWidget(self.task_input)
        hbox.addWidget(self.date_input)
        hbox.addWidget(self.add_button)
        hbox.addWidget(self.remove_button)
        hbox.addWidget(self.save_button)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.add_button.clicked.connect(self.add_task)
        self.remove_button.clicked.connect(self.remove_task)
        self.save_button.clicked.connect(self.save_tasks)

        self.show()

    def add_task(self):
        task_text = self.task_input.text()
        selected_date = self.date_input.selectedDate()
        if task_text:
            task_item = QCheckBox(f'{task_text} ({selected_date.toString("dd/MM/yyyy")})')
            self.task_list.addItem('')
            self.task_list.setItemWidget(self.task_list.item(self.task_list.count() - 1), task_item)
            self.task_input.clear()
        else:
            QMessageBox.warning(self, 'Empty Task', 'Please enter a task.')

    def remove_task(self):
        selected_items = self.task_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, 'No Task Selected', 'Please select a task to remove.')
        for item in selected_items:
            row = self.task_list.row(item)
            self.task_list.takeItem(row)

    def save_tasks(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Save Tasks', '', 'Text Files (*.txt)')
        if filename:
            try:
                with open(filename, 'w') as file:
                    for index in range(self.task_list.count()):
                        task_item = self.task_list.itemWidget(self.task_list.item(index))
                        task_text = task_item.text().split('(')[0].strip()
                        task_date = task_item.text().split('(')[1].split(')')[0].strip()
                        file.write(f'{task_text} ({task_date})\n')
                QMessageBox.information(self, 'Tasks Saved', 'Tasks have been saved successfully.')
            except Exception as e:
                QMessageBox.warning(self, 'Save Error', f'An error occurred while saving tasks: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo_app = ToDoListApp()
    sys.exit(app.exec_())
