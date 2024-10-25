from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QFrame, QMessageBox
from data_baza import Mysql
from admin_dashboard import Admin_asosiy_panel

class Admin(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.setFixedSize(700, 400)
        self.setWindowTitle("admin panel")

        # frame
        self.frame_button = QFrame()
        self.frame_button.setStyleSheet("border-radius:50px; ")
        self.frame_button.setStyleSheet("background-color: white;") 
        self.frame_layout = QVBoxLayout()
        self.frame_button.setLayout(self.frame_layout)



        # box layouts
        self.v_main = QVBoxLayout()
        self.h_name_box = QHBoxLayout()
        self.h_parol_box = QHBoxLayout()
        self.h_button_box = QHBoxLayout()


        # admin name label
        self.user_name_lbl = QLabel("Direktor ismi")
        self.user_name_lbl.setStyleSheet("color:rgb(8, 68, 120); font-size:25px; font-weight:bold")
        self.h_name_box.addWidget(self.user_name_lbl)



        # admin name editline
        self.user_name_edit = QLineEdit()
        self.user_name_edit.setPlaceholderText("Ism....")
        self.user_name_edit.setStyleSheet("border-radius: 3px; border: 1px solid black; font-size: 20px; font-weight: bold;")
        self.h_name_box.addWidget(self.user_name_edit)
        self.frame_layout.addLayout(self.h_name_box)


        # parol label
        self.user_parol = QLabel("Direktor Parol")
        self.h_parol_box.addWidget(self.user_parol)
        self.user_parol.setStyleSheet("color:rgb(8, 68, 120); font-size:25px; font-weight:bold")


        # parol editline
        self.user_parol_edit = QLineEdit()
        self.user_parol_edit.setPlaceholderText("parol....")
        self.user_parol_edit.setEchoMode(QLineEdit.Password)
        self.user_parol_edit.setStyleSheet("border-radius: 3px; border: 1px solid black; font-size: 20px; font-weight: bold;")
        self.h_parol_box.addWidget(self.user_parol_edit)
        self.frame_layout.addLayout(self.h_parol_box)
        


        # submit button
        self.submit_btn =QPushButton("Saqlash", clicked = self.Submit)
        self.submit_btn.setStyleSheet("QPushButton {color:black; background-color: green;font-size:22px; font-weight:bold;} QPushButton:hover{color:rgb(8, 68, 120); background-color:white; border-color: rgb(50, 50, 150);} ")
        self.h_button_box.addWidget(self.submit_btn)

        # menyu
        self.menyu_btn = QPushButton("Orqaga", clicked = self.Menyu)
        self.menyu_btn.setStyleSheet("QPushButton {color:black; background-color: yellow; font-size:22px; font-weight:bold;} QPushButton:hover{color:rgb(8, 68, 120);background-color:white; border-color: rgb(50, 50, 150);} ")
        self.h_button_box.addWidget(self.menyu_btn)
        self.frame_layout.addLayout(self.h_button_box)


        self.v_main.addWidget(self.frame_button)
        self.setLayout(self.v_main)



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # menyu method
    def Menyu(self):
        self.hide()
        self.main.show()

    # submit method
    def Submit(self):
        self.database = Mysql()

        admin_name = self.user_name_edit.text().lower()
        admin_parol = self.user_parol_edit.text()

        if admin_name and admin_parol:
            if self.database.Check_admin(admin_name, admin_parol):
                self.student_panel = Admin_asosiy_panel(self)
                self.hide()
                self.student_panel.show()

                self.user_name_edit.clear()
                self.user_parol_edit.clear()

            else:
                self.user_name_edit.clear()
                self.user_parol_edit.clear()

                self.msg = QMessageBox()
                self.msg.setText("Ism yoki parolda xatolik mavjud")
                self.msg.setIcon(QMessageBox.Warning)
                self.msg.exec_()
        else:
            self.user_name_edit.clear()
            self.user_parol_edit.clear()

            self.msg = QMessageBox()
            self.msg.setText("Ism yoki parolda xatolik mavjud")
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.exec_()

        
            
        

