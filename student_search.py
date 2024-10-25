from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QPushButton, QFrame, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox, QTableWidget, QTableWidgetItem
from talaba_database import TalabaSql

class StudentSearch(QWidget):
    def __init__(self, main):
        super().__init__()
        self.setWindowTitle("student search")
        self.setFixedSize(700, 400)

        self.main = main

        # boxlar
        self.v_edit_box = QVBoxLayout()
        self.v_label_box = QVBoxLayout()
        self.h_label_edit_box =QHBoxLayout()

        self.v_month_label_box = QVBoxLayout()
        self.v_month_edit_box = QVBoxLayout()
        self.h_month_edit_box = QHBoxLayout()
        self.v_main_box = QVBoxLayout()
        self.button_box = QHBoxLayout()


        # name label
        self.name_label = QLabel("Talaba ismini kiriting")
        self.name_label.setStyleSheet("color:rgb(8, 68, 120); font-size:25px; font-weight:bold")

        self.v_label_box.addWidget(self.name_label)

        # time label
        self.time_label = QLabel("Vaqtini tanlang")
        self.time_label.setStyleSheet("color:rgb(8, 68, 120); font-size:25px; font-weight:bold")
        self.v_label_box.addWidget(self.time_label)

        # day label
        self.day_label = QLabel("Kunni tanlang")
        self.day_label.setStyleSheet("color:rgb(8, 68, 120); font-size:25px; font-weight:bold")
        self.v_label_box.addWidget(self.day_label)
        self.h_label_edit_box.addLayout(self.v_label_box)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # name edit
        self.name_edit  = QLineEdit()
        self.name_edit.setPlaceholderText("ism...")
        self.name_edit.setStyleSheet("border-radius: 3px; border: 1px solid black; font-size: 20px; font-weight: bold;")
        self.v_edit_box.addWidget(self.name_edit)

        # time edit
        self.time_combo = QComboBox()
        self.time_combo.addItem("")
        self.time_combo.addItem("09:00-12:00")
        self.time_combo.addItem("13:00-17:00")
        self.time_combo.setStyleSheet("color:rgb(8, 68, 120); font-size:22px; font-weight:bold;")
        self.v_edit_box.addWidget(self.time_combo)

        # day edit
        self.day_combo = QComboBox()
        self.day_combo.addItem("")
        self.day_combo.addItem("Dushanba-Chorshanba-Juma")
        self.day_combo.addItem("Seshanba-Payshanba-Shanba")
        self.day_combo.setStyleSheet("color:rgb(8, 68, 120); font-size:22px; font-weight:bold;")
        self.v_edit_box.addWidget(self.day_combo)
        self.h_label_edit_box.addLayout(self.v_edit_box)

        # check button
        self.check_button = QPushButton("Tekshirish", clicked = self.CheckTalaba)
        self.check_button.setStyleSheet("QPushButton {color:white;background-color:green; font-size:22px; font-weight:bold;} QPushButton:hover {background-color: rgb(9, 143, 76); border-color: rgb(50, 50, 150);}")

        self.v_main_box.addLayout(self.h_label_edit_box)
        self.v_main_box.addWidget(self.check_button)


        # month label
        self.month_label = QLabel("Oy tanlang")
        self.month_label.setStyleSheet("color:rgb(8, 68, 120); font-size:25px; font-weight:bold")
        self.month_label.hide()
        self.v_month_label_box.addWidget(self.month_label)


        # payment label
        self.payment_label = QLabel("To'lovni kiriting")
        self.payment_label.setStyleSheet("color:rgb(8, 68, 120); font-size:25px; font-weight:bold")
        self.payment_label.hide()
        self.v_month_label_box.addWidget(self.payment_label)
        self.h_month_edit_box.addLayout(self.v_month_label_box)

        # month edit
        self.month_combo = QComboBox()
        self.month_combo.addItem("")
        self.month_combo.addItem("Yanvar")
        self.month_combo.addItem("Fevral")
        self.month_combo.addItem("Mart")
        self.month_combo.addItem("Aprel")
        self.month_combo.addItem("May")
        self.month_combo.addItem("Iyun")
        self.month_combo.addItem("Iyul")
        self.month_combo.addItem("Avgust")
        self.month_combo.addItem("Sentabr")
        self.month_combo.addItem("Oktabr")
        self.month_combo.addItem("Noyabr")
        self.month_combo.addItem("Dekabr")
        self.month_combo.setStyleSheet("border-radius: 3px; border: 1px solid black; font-size: 20px; font-weight: bold;")
        self.month_combo.hide()
        self.v_month_edit_box.addWidget(self.month_combo)

        # payment edit
        self.payment_edit = QLineEdit()
        self.payment_edit.setPlaceholderText("sum...")
        self.payment_edit.setStyleSheet("border-radius: 3px; border: 1px solid black; font-size: 20px; font-weight: bold;")
        self.payment_edit.hide()
        self.v_month_edit_box.addWidget(self.payment_edit)
        self.h_month_edit_box.addLayout(self.v_month_edit_box)
        self.v_main_box.addLayout(self.h_month_edit_box)


        # saqlash
        self.save_button = QPushButton("Saqlash", clicked = self.Save)
        self.save_button.setStyleSheet("QPushButton {color:white;background-color:green; font-size:22px; font-weight:bold;} QPushButton:hover {background-color: rgb(9, 143, 76); border-color: rgb(50, 50, 150);}")
        self.v_main_box.addWidget(self.save_button)



        # full  payment button
        self.full_payment = QPushButton("To'liq to'langan oylar")
        self.full_payment.setStyleSheet("QPushButton {color:white;background-color:green; font-size:22px; font-weight:bold;} QPushButton:hover {background-color: rgb(9, 143, 76); border-color: rgb(50, 50, 150);}")
        

        self.exit_button =QPushButton("Dasturni tugatish", clicked = self.Exit)
        self.exit_button.setStyleSheet("QPushButton {color:black;background-color:red; font-size:22px; font-weight:bold;} QPushButton:hover{background-color: rgb(200, 200, 200); border-color: rgb(50, 50, 150);} ")
        self.button_box.addWidget(self.exit_button)



        # menyu button
        self.menyu = QPushButton("Orqaga", clicked = self.Back)
        self.menyu.setStyleSheet("QPushButton {color:black; background-color:yellow; font-size:22px; font-weight:bold;} QPushButton:hover{background-color: rgb(200, 200, 200); border-color: rgb(50, 50, 150);} ")
        self.button_box.addWidget(self.menyu)
       
        self.v_main_box.addWidget(self.full_payment)
        self.v_main_box.addLayout(self.button_box)
        self.setLayout(self.v_main_box)



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> METHODLAR
    def CheckTalaba(self):
        name = self.name_edit.text().lower()
        day = self.day_combo.currentText()
        time = self.time_combo.currentText()
        if name and day and time:
            self.dataBase = TalabaSql()
            if self.dataBase.Search_student(name, time, day):
                self.msg = QMessageBox()
                self.msg.setText("Tabala ma'lumotlari to'g'ri ")
                self.msg.setIcon(QMessageBox.Information)
                self.msg.exec_()
                self.payment_label.show()
                self.payment_edit.show()
                self.month_combo.show()
                self.month_label.show()
            else:
                self.msg = QMessageBox()
                self.msg.setText("Tabala ma'lumotlari to'g'ri kelmayapdi")
                self.msg.setIcon(QMessageBox.Warning)
                self.msg.exec_()

                
                self.name_edit.clear()

        else:
            self.msg = QMessageBox()
            self.msg.setText("Ma'lumot kiritmadingiz")
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.exec_()


    def Save(self):
        name = self.name_edit.text().lower()
        day = self.day_combo.currentText()
        time = self.time_combo.currentText()
        month = self.month_combo.currentText()
        money = self.payment_edit.text()
    
        if name and day and time and month and money:
            if self.dataBase.Check(name, time, day): 
                self.dataBase.InsertPaymentTable(name, time, day, month, money)                
                self.msg = QMessageBox()
                self.msg.setText("To'lov ma'lumotlari saqlandi")
                self.msg.setIcon(QMessageBox.Information)
                self.msg.exec_()
            else:
                self.msg = QMessageBox()
                self.msg.setText("Bu oy uchun to'lov avval saqlangan")
                self.msg.setIcon(QMessageBox.Critical)
                self.msg.exec_()
        else:
            self.msg = QMessageBox()
            self.msg.setText("Barcha ma'lumotlarni kiriting")
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.exec_()


    def Back(self):
        self.hide()
        self.main.show()

    def Exit(self):
        self.close()
        

            





    








        




        







