from PyQt5.QtWidgets import QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QComboBox, QTableWidget, QTableWidgetItem, QMessageBox
from talaba_database import TalabaSql


class GroupSearch(QWidget):
    def __init__(self, main):
        super().__init__()

        self.main = main

        # boxlar
        self.setWindowTitle("Group search")
        self.h_time = QHBoxLayout()
        self.h_day = QHBoxLayout()
        self.v_main = QVBoxLayout()
        self.button_box = QHBoxLayout()


        self.setFixedSize(1000, 800)

        #guruh time lbl 
        self.guruh_label = QLabel("Guruh vaqtini belgilang")
        self.guruh_label.setStyleSheet("color:rgb(8, 68, 120); font-size:22px; font-weight:bold;")
        self.h_time.addWidget(self.guruh_label)

        # time combo box
        self.time_combo = QComboBox()
        self.time_combo = QComboBox()
        self.time_combo.addItem("")
        self.time_combo.addItem("09:00-12:00")
        self.time_combo.addItem("13:00-17:00")
        self.time_combo.setStyleSheet("color:rgb(8, 68, 120); font-size:22px; font-weight:bold;")
        self.h_time.addWidget(self.time_combo)
        self.v_main.addLayout(self.h_time)


        # label for day
        self.day_label = QLabel("Guruh kunlarini tanlang")
        self.day_label.setStyleSheet("color:rgb(8, 68, 120); font-size:22px; font-weight:bold;")
        self.h_day.addWidget(self.day_label)


        # combo day
        self.day_combo = QComboBox()
        self.day_combo = QComboBox()
        self.day_combo.addItem("")
        self.day_combo.addItem("Dushanba-Chorshanba-Juma")
        self.day_combo.addItem("Seshanba-Payshanba-Shanba")
        self.day_combo.setStyleSheet("color:rgb(8, 68, 120); font-size:22px; font-weight:bold;")
        self.h_day.addWidget(self.day_combo)
        self.v_main.addLayout(self.h_day)

        # button show
        self.show_button = QPushButton("Ma'lumotlarni chiqarish", clicked = self.Show)
        self.show_button.setStyleSheet("QPushButton {color:black;background-color:green; font-size:22px; font-weight:bold;} QPushButton:hover{background-color: rgb(200, 200, 200); border-color: rgb(50, 50, 150);} ")
        self.v_main.addWidget(self.show_button)



        # bu yerda table bo'lishi kerak
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Talaba ismi ", "Vaqti", "Kunlarni", "To'langan oylari"])
        self.table.setStyleSheet("color:rgb(8, 68, 120); font-size:22px; font-weight:bold;")
        self.table.adjustSize()


        self.v_main.addWidget(self.table)





        # button 
        self.exit_button =QPushButton("Dasturni tugatish", clicked = self.Exit)
        self.exit_button.setStyleSheet("QPushButton {color:black;background-color:red; font-size:22px; font-weight:bold;} QPushButton:hover{background-color: rgb(200, 200, 200); border-color: rgb(50, 50, 150);} ")
        self.button_box.addWidget(self.exit_button)



        # menyu button
        self.menyu = QPushButton("Orqaga", clicked = self.Back)
        self.menyu.setStyleSheet("QPushButton {color:black; background-color:yellow; font-size:22px; font-weight:bold;} QPushButton:hover{background-color: rgb(200, 200, 200); border-color: rgb(50, 50, 150);} ")
        self.button_box.addWidget(self.menyu)
        self.v_main.addLayout(self.button_box)


        self.setLayout(self.v_main)

    def Show(self):
        # self.databaze = TalabaSql()
        day = self.day_combo.currentText()
        time = self.time_combo.currentText()
        if day and time:
            self.load_students()
                           
        else:
            self.msg = QMessageBox()
            self.msg.setText("Yuqoridagi bo'limlarni bo'sh qoldirdingiz")
            self.msg.setIcon(QMessageBox.Information)
            self.msg.exec_()
            self.table.setRowCount(0) 
    

    def load_students(self):
        day = self.day_combo.currentText()
        time = self.time_combo.currentText()
        self.dataBaze = TalabaSql()
        students = self.dataBaze.ShowTalabaInfo(time ,day)
        if students:
            self.table.setRowCount(0)  
            for student in students:
                row_position = self.table.rowCount()
                self.table.insertRow(row_position)
                self.table.setItem(row_position, 0, QTableWidgetItem(student[0]))
                self.table.setItem(row_position, 1, QTableWidgetItem(student[1]))
                self.table.setItem(row_position, 2, QTableWidgetItem(student[2]))
                self.table.setItem(row_position, 3, QTableWidgetItem(student[3]))
        else:
            self.msg = QMessageBox()
            self.msg.setText("Bu guruhda o'quvchilar mavjud emas")
            self.msg.setIcon(QMessageBox.Information)
            self.msg.exec_()
            self.table.setRowCount(0) 

    

    def Exit(self):
        self.close()

    def Back(self):
        self.hide()
        self.main.show()





