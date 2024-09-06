import json
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon

class Admin(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1700, 900)
        self.setStyleSheet("background:#fff")

        self.v_main_lay = QVBoxLayout()
        self.h_sidebar_lay = QHBoxLayout()
        self.h_logotip_lay = QHBoxLayout()
        self.h_exit_lay = QHBoxLayout()

        self.h_mainbar_lay = QHBoxLayout()
        self.v_btns_lay = QVBoxLayout()

        self.stacked_widget = QStackedWidget()

        self.h_home_lay = QHBoxLayout()
        self.home_btn = QPushButton(" Bosh Sahifa",clicked=self.dastlab)
        self.home_btn.setIcon(QIcon("images/home.jpg"))
        self.home_btn.setStyleSheet("font-size:20px;font-family:Georgia")
        self.home_btn.setFixedHeight(50)
        self.home_btn.setFixedWidth(250)
        self.h_home_lay.addWidget(self.home_btn)

        self.h_pay_lay = QHBoxLayout()
        self.pay_btn = QPushButton("   \U0001F4DD O'quvchi qo'shish", clicked=self.add_sdt)
        self.pay_btn.setStyleSheet("font-size:20px;font-family:Georgia")
        self.pay_btn.setFixedHeight(50)
        self.h_pay_lay.addWidget(self.pay_btn)

        self.h_group_lay = QHBoxLayout()
        self.group_btn = QPushButton("   \U0001F5D1 O'quvchi o'chirish", clicked=self.dell_sdt)
        self.group_btn.setStyleSheet("font-size:20px;font-family:Georgia")
        self.group_btn.setFixedHeight(50)
        self.h_group_lay.addWidget(self.group_btn)

        self.h_grade_lay = QHBoxLayout()
        self.grade_btn = QPushButton("    Guruhlar", clicked=self.group_sdt)
        self.grade_btn.setIcon(QIcon("images/group.png"))
        self.grade_btn.setStyleSheet("font-size:20px;font-family:Georgia")
        self.grade_btn.setFixedHeight(50)
        self.h_grade_lay.addWidget(self.grade_btn)

        self.h_reyting_lay = QHBoxLayout()
        self.reyting_btn = QPushButton("  \U0001F50D  Qidiruv", clicked=self.search_sdt)
        self.reyting_btn.setStyleSheet("font-size:20px;font-family:Georgia")
        self.reyting_btn.setFixedHeight(50)
        self.h_reyting_lay.addWidget(self.reyting_btn)

        self.h_market_lay = QHBoxLayout()
        self.market_btn = QPushButton("    Do'kon", clicked=self.shop_sdt)
        self.market_btn.setIcon(QIcon("images/market.jpg"))
        self.market_btn.setStyleSheet("font-size:20px;font-family:Georgia")
        self.market_btn.setFixedHeight(50)
        self.h_market_lay.addWidget(self.market_btn)

        self.h_setting_lay = QHBoxLayout()
        self.setting_btn = QPushButton("    Sozlamalar", clicked=self.setings)
        self.setting_btn.setIcon(QIcon("images/setting.png"))
        self.setting_btn.setStyleSheet("font-size:20px;font-family:Georgia")
        self.setting_btn.setFixedHeight(50)
        self.h_setting_lay.addWidget(self.setting_btn)

        self.lst_layouts = [self.h_home_lay, self.h_pay_lay, self.h_group_lay, self.h_grade_lay, self.h_reyting_lay, self.h_market_lay, self.h_setting_lay]
        for i in self.lst_layouts:
            self.v_btns_lay.addLayout(i)
        self.v_btns_lay.addStretch()

        self.h_mainbar_lay.addLayout(self.v_btns_lay)
        self.h_mainbar_lay.addWidget(self.stacked_widget)

        self.logotip = QLabel()
        self.image = QPixmap("images/logo.jpg")
        self.logotip.setPixmap(self.image)

        self.side_btn = QPushButton()
        self.side_btn.setIcon(QIcon("images/sidebar.jpg"))
        self.side_btn.setFixedSize(40, 40)
        self.side_btn.setStyleSheet("background:rgb(188,142,91)")

        self.h_logotip_lay.addWidget(self.logotip)
        self.h_logotip_lay.addWidget(self.side_btn)

        self.push_btn = QPushButton()
        self.push_btn.setIcon(QIcon("images/push.jpg"))
        self.push_btn.setFixedSize(40, 40)

        self.exit_btn = QPushButton()
        self.exit_btn.setIcon(QIcon("images/exit.jpg"))
        self.exit_btn.setFixedSize(40, 40)

        self.h_exit_lay.addWidget(self.push_btn)
        self.h_exit_lay.addWidget(self.exit_btn)

        self.h_sidebar_lay.addLayout(self.h_logotip_lay)
        self.h_sidebar_lay.addStretch()
        self.h_sidebar_lay.addLayout(self.h_exit_lay)

        self.v_main_lay.addLayout(self.h_sidebar_lay)
        self.v_main_lay.addLayout(self.h_mainbar_lay)

        self.setLayout(self.v_main_lay)

        self.data_file = 'students.json'
        self.groups_file = 'groups.json'
        self.students = self.load_data(self.data_file)
        self.groups = self.load_data(self.groups_file)

        self.init_add_student_form()

    def dastlab(self):
        for i in range(self.stacked_widget.count()):
            self.stacked_widget.widget(i).hide()

    def init_add_student_form(self):
        self.add_student_form = QWidget()
        self.add_student_layout = QFormLayout()
        self.first_name_input = QLineEdit()
        self.last_name_input = QLineEdit()
        self.direction_input = QLineEdit()
        self.group_number_input = QLineEdit()
        self.grade_input = QLineEdit()
        self.add_student_button = QPushButton("Saqlash", clicked=self.save_student)
        
        self.add_student_layout.addRow("Ism:", self.first_name_input)
        self.add_student_layout.addRow("Familiya:", self.last_name_input)
        self.add_student_layout.addRow("Yo'nalish:", self.direction_input)
        self.add_student_layout.addRow("Guruh raqami:", self.group_number_input)
        self.add_student_layout.addRow("Bosqich:", self.grade_input)
        self.add_student_layout.addRow("", self.add_student_button)
        self.add_student_form.setLayout(self.add_student_layout)

    def add_sdt(self):
        self.stacked_widget.addWidget(self.add_student_form)
        self.stacked_widget.setCurrentWidget(self.add_student_form)

    def save_student(self):
        student_id = str(len(self.students) + 1)
        
        student = {
            'ID': student_id,
            'Ism': self.first_name_input.text(),
            'Familiya': self.last_name_input.text(),
            'Yo\'nalish': self.direction_input.text(),
            'Guruh': self.group_number_input.text(),
            'Bosqich': self.grade_input.text()
        }

        self.students[student_id] = student
        self.save_data(self.data_file, self.students)
        self.add_student_to_group(student_id, self.group_number_input.text())
        self.clear_add_student_form()

    def clear_add_student_form(self):
        self.first_name_input.clear()
        self.last_name_input.clear()
        self.direction_input.clear()
        self.group_number_input.clear()
        self.grade_input.clear()

    def load_data(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return json.load(f)
        return {}

    def save_data(self, file_path, data):
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def add_student_to_group(self, student_id, group_number):
        if group_number not in self.groups:
            self.groups[group_number] = []
        self.groups[group_number].append(student_id)
        self.save_data(self.groups_file, self.groups)

    def dell_sdt(self):
        widget = QWidget()
        layout = QFormLayout()
        self.delete_id_input = QLineEdit()
        delete_button = QPushButton("O'chirish", clicked=self.delete_student)
        layout.addRow("O'quvchi ID:", self.delete_id_input)
        layout.addWidget(delete_button)
        widget.setLayout(layout)
        self.stacked_widget.addWidget(widget)
        self.stacked_widget.setCurrentWidget(widget)

    def delete_student(self):
        student_id = self.delete_id_input.text()
        if student_id.isdigit():
            student_id = str(student_id)
            if student_id in self.students:
                group_number = self.students[student_id]['Guruh']
                self.groups[group_number].remove(student_id)
                if not self.groups[group_number]:
                    del self.groups[group_number]
                del self.students[student_id]
                self.save_data(self.data_file, self.students)
                self.save_data(self.groups_file, self.groups)
                self.stacked_widget.setCurrentIndex(0)
                QMessageBox.information(self, "To'g'ri","O'quvchi o'chirildi")
            else:
                QMessageBox.warning(self, "Xato", "O'quvchi topilmadi!")
        else:
            QMessageBox.warning(self, "Xato", "ID raqam noto'g'ri formatda!")

    def group_sdt(self):
        widget = QWidget()
        layout = QVBoxLayout()

        group_list_widget = QListWidget()
        for group_number in self.groups.keys():
            group_list_widget.addItem(f"Guruh {group_number}")

        group_list_widget.itemClicked.connect(self.display_group_students)
        layout.addWidget(group_list_widget)
        widget.setLayout(layout)
        self.stacked_widget.addWidget(widget)
        self.stacked_widget.setCurrentWidget(widget)

    def display_group_students(self, item):
        group_number = item.text().split()[1]
        widget = QWidget()
        layout = QVBoxLayout()
        student_list_widget = QListWidget()

        for s_i in self.groups.get(group_number, []):
            student = self.students[str(s_i)]
            student_list_widget.addItem(f"ID: {student['ID']}\nIsm: {student['Ism']}\nFamiliya: {student['Familiya']}\nYo'nalish: {student['Yo\'nalish']}\nBosqich: {student['Bosqich']}")

        layout.addWidget(student_list_widget)
        widget.setLayout(layout)
        self.stacked_widget.addWidget(widget)
        self.stacked_widget.setCurrentWidget(widget)

    def search_sdt(self):
        widget = QWidget()
        layout = QFormLayout()
        self.search_id_input = QLineEdit()
        search_button = QPushButton("Qidirish", clicked=self.perform_search)
        layout.addRow("O'quvchi ID:", self.search_id_input)
        layout.addWidget(search_button)
        self.result_label = QLabel()
        layout.addWidget(self.result_label)
        widget.setLayout(layout)
        self.stacked_widget.addWidget(widget)
        self.stacked_widget.setCurrentWidget(widget)

    def perform_search(self):
        student_id = self.search_id_input.text()
        if student_id.isdigit():
            student_id = str(student_id)
            student = self.students.get(student_id)
            if student:
                self.result_label.setText(f"ID: {student['ID']}\nIsm: {student['Ism']}\nFamiliya: {student['Familiya']}\nYo'nalish: {student['Yo\'nalish']}\nGuruh: {student['Guruh']}\nBosqich: {student['Bosqich']}")
            else:
                self.result_label.setText("O'quvchi topilmadi!")
        else:
            self.result_label.setText("ID raqam noto'g'ri formatda!")

    def shop_sdt(self):
        QMessageBox.information(self, "Do'kon", "Do'kon bo'limi hali yaratilmagan.")

    def setings(self):
        QMessageBox.information(self, "Sozlamalar", "Sozlamalar bo'limi hali yaratilmagan.")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Admin()
    window.show()
    sys.exit(app.exec_())
