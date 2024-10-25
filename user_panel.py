from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QFrame, QMessageBox
from data_baza import Mysql
from student_add import StudentAdd

class User(QWidget):
    def __init__(self, main):
        super().__init__()

        self.main = main
        self.setFixedSize(700, 400)
        self.setWindowTitle("user panel")


        # box layouts
        self.v_main = QVBoxLayout()
        self.h_button_box = QHBoxLayout()
        self.h_box_name = QHBoxLayout()
        self.h_parol_box = QHBoxLayout()


        # frame
        self.frame_button = QFrame()
        self.frame_button.setStyleSheet("border-radius:50px; ")
        self.frame_button.setStyleSheet("background-color: white;") 
        self.frame_layout = QVBoxLayout()
        self.frame_button.setLayout(self.frame_layout)


        # user name label
        self.name_user_lbl = QLabel("Hodim Ismi ")
        self.name_user_lbl.setStyleSheet("color:rgb(8, 68, 120); font-size:25px; font-weight:bold")
        self.h_box_name.addWidget(self.name_user_lbl)

        # user name sedit
        self.name_user_edit = QLineEdit()
        self.name_user_edit.setPlaceholderText("Ism....")
        self.name_user_edit.setStyleSheet("border-radius: 3px; border: 1px solid black; font-size: 20px; font-weight: bold;")
        self.h_box_name.addWidget(self.name_user_edit)
        self.frame_layout.addLayout(self.h_box_name)


        # parol label
        self.parol_user = QLabel("Hodim Parol")
        self.parol_user.setStyleSheet("color:rgb(8, 68, 120); font-size:25px; font-weight:bold")
        self.h_parol_box.addWidget(self.parol_user)

        # parol edit line
        self.parol_edit =QLineEdit()
        self.parol_edit.setPlaceholderText("parol....")
        self.parol_edit.setEchoMode(QLineEdit.Password)
        self.parol_edit.setStyleSheet("border-radius: 3px; border: 1px solid black; font-size: 20px; font-weight: bold;")
        self.h_parol_box.addWidget(self.parol_edit)
        self.frame_layout.addLayout(self.h_parol_box)


        # checker button
        self.checker_btn = QPushButton("Tekshirish", clicked = self.Check)
        self.checker_btn.setStyleSheet("QPushButton {color:black; background-color: green;font-size:22px; font-weight:bold;} QPushButton:hover{color:rgb(8, 68, 120); background-color:white; border-color: rgb(50, 50, 150);} ")
        self.h_button_box.addWidget(self.checker_btn)

        # menyu button
        self.menyu_button = QPushButton("Orqaga", clicked = self.Menyu)
        self.menyu_button.setStyleSheet("QPushButton {color:black; background-color: yellow; font-size:22px; font-weight:bold;} QPushButton:hover{color:rgb(8, 68, 120);background-color:white; border-color: rgb(50, 50, 150);} ")
        self.h_button_box.addWidget(self.menyu_button)



        self.frame_layout.addLayout(self.h_button_box)
        self.v_main.addWidget(self.frame_button)
        self.setLayout(self.v_main)



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # menyu method
    def Menyu(self):
        self.hide()
        self.main.show()

    # check method
    def Check(self):
        self.dataBaza = Mysql()
        name = self.name_user_edit.text().lower()
        parol = self.parol_edit.text()
       
        if name and parol:
            if self.dataBaza.Check_hodim(name, parol):
                self.student_dashboard = StudentAdd(self)
                self.student_dashboard.show()
                self.hide()
                self.name_user_edit.clear()
                self.parol_edit.clear()
                
            else:
                self.msg = QMessageBox()
                self.msg.setText("Parol yoki ism to'g'ri kelmadi")
                self.msg.setIcon(QMessageBox.Warning)
                self.msg.exec_()

                self.name_user_edit.clear()
                self.parol_edit.clear()
        else:
            self.msg = QMessageBox()
            self.msg.setText("Siz kerakli bo'limlarni to'ldirmagansiz")
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.exec_()


            self.name_user_edit.clear()
            self.parol_edit.clear()


        


