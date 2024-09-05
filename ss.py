from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # Kalendar yaratish
        self.calendar = QCalendarWidget(self)
        
        # Layout (tartib) yaratish
        layout = QVBoxLayout()
        
        # Layoutga kalendarni qo'shish
        layout.addWidget(self.calendar)
        
        # Layoutni oynaga qo'shish
        self.setLayout(layout)

        # Oyna parametrlari
        self.setWindowTitle("Kalendar Misoli")
        self.resize(400, 300)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
