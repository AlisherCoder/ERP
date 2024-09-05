from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon

class StdWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.resize(1700,900)
            self.setStyleSheet("background:#fff")

            self.v_main_lay = QVBoxLayout()

            self.h_sidebar_lay = QHBoxLayout()
            self.h_logotip_lay = QHBoxLayout()
            self.h_exit_lay = QHBoxLayout()

            self.h_mainbar_lay = QHBoxLayout()
            self.v_btns_lay = QVBoxLayout()

            self.h_home_lay = QHBoxLayout()
            self.home_btn = QPushButton("   Bosh Sahifa",clicked=self.home)
            self.home_btn.setIcon(QIcon("images\home.jpg"))
            self.home_btn.setStyleSheet("font-size:15px;font-family:Georgia")
            self.home_btn.setFixedHeight(50)
            self.home_btn.setFixedWidth(250)
            self.h_home_lay.addWidget(self.home_btn)
            
            self.h_pay_lay = QHBoxLayout()
            self.pay_btn = QPushButton("    To'lovlarim")
            self.pay_btn.setIcon(QIcon("images\pay.png"))
            self.pay_btn.setStyleSheet("font-size:15px;font-family:Georgia")
            self.pay_btn.setFixedHeight(50)
            self.h_pay_lay.addWidget(self.pay_btn)

            self.h_group_lay = QHBoxLayout()
            self.group_btn = QPushButton("    Guruhlarim")
            self.group_btn.setIcon(QIcon("images\group.png"))
            self.group_btn.setStyleSheet("font-size:15px;font-family:Georgia")
            self.group_btn.setFixedHeight(50)
            self.h_group_lay.addWidget(self.group_btn)

            self.h_grade_lay = QHBoxLayout()
            self.grade_btn = QPushButton("    Ko'rsatgich")
            self.grade_btn.setIcon(QIcon("images\grade.jpg"))
            self.grade_btn.setStyleSheet("font-size:15px;font-family:Georgia")
            self.grade_btn.setFixedHeight(50)
            self.h_grade_lay.addWidget(self.grade_btn)

            self.h_reyting_lay = QHBoxLayout()
            self.reyting_btn = QPushButton("    Reyting")
            self.reyting_btn.setIcon(QIcon("images\\reyting.jpg"))
            self.reyting_btn.setStyleSheet("font-size:15px;font-family:Georgia")
            self.reyting_btn.setFixedHeight(50)
            self.h_reyting_lay.addWidget(self.reyting_btn)

            self.h_market_lay = QHBoxLayout()
            self.market_btn = QPushButton("    Do'kon")
            self.market_btn.setIcon(QIcon("images\market.jpg"))
            self.market_btn.setStyleSheet("font-size:15px;font-family:Georgia")
            self.market_btn.setFixedHeight(50)
            self.h_market_lay.addWidget(self.market_btn)

            self.h_setting_lay = QHBoxLayout()
            self.setting_btn = QPushButton("    Sozlamalar")
            self.setting_btn.setIcon(QIcon("images\setting.png"))
            self.setting_btn.setStyleSheet("font-size:15px;font-family:Georgia")
            self.setting_btn.setFixedHeight(50)
            self.h_setting_lay.addWidget(self.setting_btn)

            self.lst_layouts = [self.h_home_lay,self.h_pay_lay,self.h_group_lay,self.h_grade_lay,self.h_reyting_lay,self.h_pay_lay,self.h_market_lay,self.h_setting_lay]
            for i in self.lst_layouts:
                self.v_btns_lay.addLayout(i)
            self.v_btns_lay.addStretch()
            self.qlist = QListWidget()

            self.h_mainbar_lay.addLayout(self.v_btns_lay)
            self.h_mainbar_lay.addWidget(self.qlist)

            self.logotip = QLabel()
            self.image = QPixmap("images\logo.jpg")
            self.logotip.setPixmap(self.image)

            self.side_btn = QPushButton()
            self.side_btn.setIcon(QIcon("images\sidebar.jpg"))
            self.side_btn.setFixedSize(40,40)
            self.side_btn.setStyleSheet("background:rgb(188,142,91)")

            self.h_logotip_lay.addWidget(self.logotip)
            self.h_logotip_lay.addWidget(self.side_btn)

            self.push_btn = QPushButton()
            self.push_btn.setIcon(QIcon("images\push.jpg"))
            self.push_btn.setFixedSize(40,40)

            self.exit_btn = QPushButton(clicked=self.exit)
            self.exit_btn.setIcon(QIcon("images\exit.jpg"))
            self.exit_btn.setFixedSize(40,40)

            self.h_exit_lay.addWidget(self.push_btn)
            self.h_exit_lay.addWidget(self.exit_btn)

            self.h_sidebar_lay.addLayout(self.h_logotip_lay)
            self.h_sidebar_lay.addStretch()
            self.h_sidebar_lay.addLayout(self.h_exit_lay)


            self.v_main_lay.addLayout(self.h_sidebar_lay)
            self.v_main_lay.addLayout(self.h_mainbar_lay)

            self.setLayout(self.v_main_lay)


        def home(self):
            pass

        def exit(self):
            self.hide()
if __name__ == "__main__":
    app = QApplication([])
    win = StdWindow()
    win.show()
    app.exec_()