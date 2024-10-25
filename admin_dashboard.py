from PyQt5.QtWidgets import  QPushButton,  QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from student_search import StudentSearch
from groupSearch import GroupSearch


class Admin_asosiy_panel(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.setFixedSize(500, 200)

        self.setWindowTitle("admin dashboard")

        # Box layouts
        self.v_main = QVBoxLayout()
        self.h_btn_lay = QHBoxLayout()

        # talaba haqida button
        self.student_info_button = QPushButton("Student haqida ma'lumot", clicked = self.Student)
        self.student_info_button.setStyleSheet("QPushButton {color:rgb(8, 68, 120); font-size:22px; font-weight:bold;} QPushButton:hover{background-color: rgb(200, 200, 200); border-color: rgb(50, 50, 150);} ")
        self.v_main.addWidget(self.student_info_button, alignment=Qt.AlignCenter)


        # guruhlar haqida button
        self.allStudentsInfo = QPushButton("Guruh ma'lumotlari", clicked = self.Guruh)
        self.allStudentsInfo.setStyleSheet("QPushButton {color:rgb(8, 68, 120); font-size:22px; font-weight:bold;} QPushButton:hover{background-color: rgb(200, 200, 200); border-color: rgb(50, 50, 150);} ")

        self.v_main.addWidget(self.allStudentsInfo, alignment=Qt.AlignCenter)



        # exit button
        self.exit_button =QPushButton("Dasturni tugatish", clicked = self.Exit)
        self.exit_button.setStyleSheet("QPushButton {color:rgb(8, 68, 120); font-size:22px; font-weight:bold;} QPushButton:hover{background-color: rgb(200, 200, 200); border-color: rgb(50, 50, 150);} ")

        self.h_btn_lay.addWidget(self.exit_button)



        # menyu button
        self.menyu = QPushButton("Orqaga", clicked= self.Menyu)
        self.menyu.setStyleSheet("QPushButton {color:rgb(8, 68, 120); font-size:22px; font-weight:bold;} QPushButton:hover{background-color: rgb(200, 200, 200); border-color: rgb(50, 50, 150);} ")

        self.h_btn_lay.addWidget(self.menyu)

        self.v_main.addLayout(self.h_btn_lay)
        self.setStyleSheet("background-color:white")
        self.setLayout(self.v_main)


        

       

    # metodlar-------------------------------------------------------------------------------
    
    def Menyu(self):
        self.main.show()
        self.hide()

    def Exit(self):
        self.close()


    def Student(self):
        self.student_search_panel = StudentSearch(self)
        self.student_search_panel.show()
        self.hide()

    def Guruh(self):
        self.guruhlar = GroupSearch(self)
        self.guruhlar.show()
        self.hide()
        


    