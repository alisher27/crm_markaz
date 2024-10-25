from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout,  QFrame
from PyQt5.QtCore import Qt
from admin_panel import Admin
from user_panel import User


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 200)
        self.setWindowTitle("asosiy oyna")


        # Frame to hold buttons
        self.v_main_box = QVBoxLayout()

        self.button_frame = QFrame()
        self.button_frame.setStyleSheet("border-radius:50px; ")
        self.button_frame.setStyleSheet("background-color: white;") 
        self.button_layout = QVBoxLayout()  
        self.button_frame.setLayout(self.button_layout)


        # Admin button
        self.admin_btn = QPushButton("Direktor", clicked = self.Admin)
        self.admin_btn.setStyleSheet("QPushButton {color:rgb(8, 68, 120); font-size:22px; font-weight:bold;} QPushButton:hover{background-color:green; color: white; border-color: rgb(50, 50, 150);} ")
        self.button_layout.addWidget(self.admin_btn, alignment = Qt.AlignCenter)

        # User button 
        self.user_btn = QPushButton("Xodim", clicked = self.User)
        self.user_btn.setStyleSheet("QPushButton {color:rgb(8, 68, 120); font-size:22px; font-weight:bold;} QPushButton:hover{background-color: green;color: white; border-color: rgb(50, 50, 150);} ")
        self.button_layout.addWidget(self.user_btn, alignment=Qt.AlignCenter)

        # asosiy
        self.v_main_box.addWidget(self.button_frame)
        self.setLayout(self.v_main_box)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # admin method
    def Admin(self):
        self.admin_panel = Admin(self)
        self.hide()
        self.admin_panel.show()


    # user method
    def User(self):
        self.user_panel = User(self)
        self.hide()
        self.user_panel.show()

