from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon
from admin import Admin
from student import Student
from teacher import Teacher

parol_admin = 1111
name_admin = "ALisher"

parol_teacher = 2222
name_teacher = "Temur"

parol_student = 3333
name_student = "Muxtorhon"


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1700,900)
        self.setStyleSheet("background:#fff")
        self.h_main_lay = QHBoxLayout()
        self.v_img_lay = QVBoxLayout()
        self.v_edit_lay = QVBoxLayout()
        self.v_login_lay = QVBoxLayout()
        self.h_log_lay = QHBoxLayout()

        self.lbl = QLabel("Kirish")
        self.lbl.setStyleSheet("font-size:24px;color:rgb(51,51,51)")
        font = QFont("SB Sans Text, Helvetica, Arial, sans-serif",8,QFont.Bold)
        self.lbl.setFont(font)

        self.log_edit = QLineEdit()
        self.log_edit.setPlaceholderText("Kirish")
        self.log_edit.setFixedHeight(40)

        self.par_edit = QLineEdit()
        self.par_edit.setPlaceholderText("Parol")
        self.par_edit.setFixedHeight(40)
        self.par_edit.setEchoMode(QLineEdit.Password)

        self.eye_btn = QPushButton()
        self.eye_btn.setCheckable(True)
        self.eye_btn.setIcon(QIcon("hide.png"))
        self.eye_btn.setFixedSize(30, 30)
        self.eye_btn.clicked.connect(self.toggle_password_visibility)

        par_layout = QHBoxLayout()
        par_layout.addWidget(self.par_edit)
        par_layout.addWidget(self.eye_btn)

        self.kirish_btn = QPushButton("Kirish",clicked=self.kirish)
        self.kirish_btn.setFixedHeight(40)
        self.kirish_btn.setStyleSheet("background-color:rgb(188,142,91);color:white;font-size:16px;font-family:sans-serif")

        self.v_login_lay.addWidget(self.lbl)
        self.v_login_lay.addWidget(self.log_edit)
        self.v_login_lay.addLayout(par_layout)
        self.v_login_lay.addWidget(self.kirish_btn)
    
        self.h_log_lay.addStretch()
        self.h_log_lay.addLayout(self.v_login_lay)
        self.h_log_lay.addStretch()

        self.v_edit_lay.addStretch()
        self.v_edit_lay.addLayout(self.h_log_lay)
        self.v_edit_lay.addStretch()

        self.left_lbl = QLabel()
        self.image = QPixmap("img.jpg")
        self.left_lbl.setPixmap(self.image)
        self.left_lbl.setScaledContents(True)
        self.v_img_lay.addWidget(self.left_lbl)

        self.h_main_lay.addLayout(self.v_img_lay)
        self.h_main_lay.addLayout(self.v_edit_lay)

        self.setLayout(self.h_main_lay)

    def kirish(self):
        name = self.log_edit.text()
        parol = self.par_edit.text()
        try:
            if name == name_admin and parol == parol_admin:
                Admin()
            elif name == name_student and parol == parol_student:
                Student()
            elif name == name_teacher and parol == parol_teacher:
                Teacher()
            else:
                self.msg = QMessageBox()
                self.msg.setText("Siz xato ma'lumot kiritdingiz.!")
                self.msg.move(1500,100)
                self.msg.setIcon(QMessageBox.Information)
                self.msg.exec_()
        except:
            self.msg = QMessageBox()
            self.msg.setText("Siz xato ma'lumot kiritdingiz.!")
            self.msg.move(1500,100)
            self.msg.setIcon(QMessageBox.Information)
            self.msg.exec_()


    def toggle_password_visibility(self):
        if self.eye_btn.isChecked():
            self.par_edit.setEchoMode(QLineEdit.Normal)
            self.eye_btn.setIcon(QIcon("view.png"))
            self.eye_btn.setFixedSize(30,30)
        else:
            self.par_edit.setEchoMode(QLineEdit.Password)
            self.eye_btn.setIcon(QIcon("hide.png"))
            self.eye_btn.setFixedSize(30,30)

if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec_()