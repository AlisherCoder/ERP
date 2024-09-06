from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import QSize

class Techwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1700, 900)
        self.setStyleSheet("background:#fff")
        
        self.setWindowIcon(QIcon("ERP/images/nt_logo.png"))

        self.v_main_lay = QVBoxLayout()

        self.h_sidebar_lay = QHBoxLayout()
        self.h_logotip_lay = QHBoxLayout()
        self.h_exit_lay = QHBoxLayout()

        self.h_mainbar_lay = QHBoxLayout()
        self.v_btns_lay = QVBoxLayout()

        self.h_home_lay = QHBoxLayout()
        self.home_btn = QPushButton("   Bosh Sahifa", clicked=self.home)
        self.home_btn.setIcon(QIcon("ERP/images/home.jpg"))
        self.home_btn.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                font-family: SBSansText, Helvetica, Arial, sans-serif;
                padding: 0px;
                border-radius: 10px;
                margin-bottom: 4px;
                color: rgb(51, 51, 51);
                background-color: #fff;
                border: none;
            }
            QPushButton:hover {
                background-color: rgb(188, 142, 91);
                color: white;
            }
        """)
        self.home_btn.setFixedHeight(50)
        self.home_btn.setFixedWidth(300)
        self.h_home_lay.addWidget(self.home_btn)

        self.h_group_lay = QHBoxLayout()
        self.group_btn = QPushButton("    Guruhlarim")
        self.group_btn.setIcon(QIcon("ERP/images/group.png"))
        self.group_btn.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                font-family: SBSansText, Helvetica, Arial, sans-serif;
                padding: 0px;
                border-radius: 10px;
                margin-bottom: 4px;
                color: rgb(51, 51, 51);
                background-color: #fff;
                border: none;
            }
            QPushButton:hover {
                 background-color: rgb(238, 242, 246);
                color: rgb(51, 51, 51);
            }
        """)
        self.group_btn.setFixedHeight(50)
        self.h_group_lay.addWidget(self.group_btn)

        self.h_reyting_lay = QHBoxLayout()
        self.reyting_btn = QPushButton("    Reyting")
        self.reyting_btn.setIcon(QIcon("ERP/images/reyting.jpg"))
        self.reyting_btn.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                font-family: SBSansText, Helvetica, Arial, sans-serif;
                padding: 0px;
                border-radius: 10px;
                margin-bottom: 4px;
                color: rgb(51, 51, 51);
                background-color: #fff;
                border: none;
            }
            QPushButton:hover {
                 background-color: rgb(238, 242, 246);
                color: rgb(51, 51, 51);
            }
        """)
        self.reyting_btn.setFixedHeight(50)
        
        self.h_reyting_lay.addWidget(self.reyting_btn)

        self.h_setting_lay = QHBoxLayout()
        self.setting_btn = QPushButton("    Sozlamalar")
        self.setting_btn.setIcon(QIcon("ERP/images/setting.png"))
        self.setting_btn.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                font-family: SBSansText, Helvetica, Arial, sans-serif;
                padding: 0px;
                border-radius: 10px;
                margin-bottom: 4px;
                color: rgb(51, 51, 51);
                background-color: #fff;
                border: none;
            }
            QPushButton:hover {
                background-color: rgb(238, 242, 246);
                color: rgb(51, 51, 51);
            }
        """)
        self.setting_btn.setFixedHeight(50)
        self.h_setting_lay.addWidget(self.setting_btn)

        self.lst_layouts = [self.h_home_lay, self.h_group_lay, self.h_reyting_lay, self.h_setting_lay]

        for i in self.lst_layouts:
            self.v_btns_lay.addLayout(i)
        self.v_btns_lay.addStretch()

        self.qlist = QListWidget()
        
        self.qlist.setIconSize(QSize(1359, 1200))
        self.qlist.setStyleSheet("background: rgb(238, 242, 246);")
        
        item = QListWidgetItem(QIcon("ERP/images/lis.png"),"")
        font = QFont()
        font.setPointSize(18)
        item.setFont(font)
        self.qlist.addItem(item)

        self.h_mainbar_lay.addLayout(self.v_btns_lay)
        self.h_mainbar_lay.addWidget(self.qlist)

        self.logotip = QLabel()
        self.image = QPixmap("ERP/images/logo.jpg")
        self.logotip.setPixmap(self.image)

        self.side_btn = QPushButton()
        self.side_btn.setIcon(QIcon("ERP/images/men.png"))
        self.side_btn.setFixedSize(40, 40)
        self.side_btn.setStyleSheet("""
            background: rgb(188, 142, 91);
            border-radius: 10px;
            margin-bottom: 4px;
        """)

        self.h_logotip_lay.addWidget(self.logotip)
        self.h_logotip_lay.addWidget(self.side_btn)

        self.push_btn = QPushButton()
        self.push_btn.setIcon(QIcon("ERP/images/push.jpg"))
        self.push_btn.setFixedSize(40, 40)
        self.push_btn.setStyleSheet("""
            QPushButton {
            font-size: 20px;
            font-family: SBSansText, Helvetica, Arial, sans-serif;
            padding: 0px;
            border-radius: 10px;
            margin-bottom: 4px;
            color: rgb(51, 51, 51);
            background-color: #fff;
            border: none;
            }
            QPushButton:hover {
            background-color: rgb(238, 242, 246);
            color: rgb(51, 51, 51);
            }""")

        self.exit_btn = QPushButton(clicked=self.exit)
        self.exit_btn.setIcon(QIcon("ERP/images/exit.jpg"))
        self.exit_btn.setFixedSize(40, 40)
        self.exit_btn.setStyleSheet("""
            QPushButton {
            font-size: 20px;
            font-family: SBSansText, Helvetica, Arial, sans-serif;
            padding: 0px;
            border-radius: 10px;
            margin-bottom: 4px;
            color: rgb(51, 51, 51);
            background-color: #fff;
            border: none;
            }
            QPushButton:hover {
            background-color: rgb(238, 242, 246);
            color: rgb(51, 51, 51);
            }""")

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
    win = Techwindow()
    win.setWindowTitle("Offline student panel")
    win.show()
    app.exec_()
