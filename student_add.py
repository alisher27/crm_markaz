from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QPushButton, QFrame, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox, QTableWidget, QTableWidgetItem, QCalendarWidget
from talaba_database import TalabaSql
from datetime import datetime

class StudentAdd(QWidget):
    def __init__(self, main):
        super().__init__()
        self.setWindowTitle("student add")
        self.setFixedSize(1200, 900)

        self.main = main




        # Frame (container for all elements)
        self.frame_button = QFrame()
        self.frame_button.setStyleSheet("border-radius: 20px; ")
        self.frame_button.setStyleSheet("background-color: white;")
        self.frame_layout = QVBoxLayout()
        self.frame_button.setLayout(self.frame_layout)

        # Main Layouts
        self.v_main = QVBoxLayout()
        self.v_dashboard_box = QVBoxLayout()
        self.h_vaqt_box = QHBoxLayout()
        self.h_day_box = QHBoxLayout()
        self.h_buttons_lay = QHBoxLayout()
        self.h_name_lay = QHBoxLayout()

        # Student Name Label
        self.student_name_lbl = QLabel("Talaba ismi")
        self.student_name_lbl.setStyleSheet("color:rgb(8, 68, 120); font-size:25px; font-weight:bold;")
        self.h_name_lay.addWidget(self.student_name_lbl)

        # Student Name LineEdit
        self.student_name_edit = QLineEdit()
        self.student_name_edit.setPlaceholderText("Alisher Matkarimov")
        self.student_name_edit.setStyleSheet("border-radius: 5px; border: 1px solid black; font-size: 22px; font-weight: bold;")
        self.h_name_lay.addWidget(self.student_name_edit)
        self.v_dashboard_box.addLayout(self.h_name_lay)

        # Time Label
        self.time_label = QLabel("Vaqtni tanlang")
        self.time_label.setStyleSheet("color:rgb(8, 68, 120); font-size:22px; font-weight:bold;")
        self.h_vaqt_box.addWidget(self.time_label)

        # Time ComboBox
        self.time_combo = QComboBox()
        self.time_combo.addItem("")
        self.time_combo.addItem("09:00-12:00")
        self.time_combo.addItem("13:00-17:00")
        self.time_combo.setStyleSheet("color:rgb(8, 68, 120); font-size:22px; font-weight:bold;")
        self.h_vaqt_box.addWidget(self.time_combo)
        self.v_dashboard_box.addLayout(self.h_vaqt_box)

        # Days Label
        self.kunlari = QLabel("Kunlari")
        self.kunlari.setStyleSheet("color:rgb(8, 68, 120); font-size:22px; font-weight:bold;")
        self.h_day_box.addWidget(self.kunlari)

        # Days ComboBox
        self.day_combo = QComboBox()
        self.day_combo.addItem("")
        self.day_combo.addItem("Dushanba-Chorshanba-Juma")
        self.day_combo.addItem("Seshanba-Payshanba-Shanba")
        self.day_combo.setStyleSheet("color:rgb(8, 68, 120); font-size:22px; font-weight:bold;")
        self.h_day_box.addWidget(self.day_combo)
        self.v_dashboard_box.addLayout(self.h_day_box)

        # Add v_dashboard_box to the frame layout
        self.frame_layout.addLayout(self.v_dashboard_box)

        # Add Buttons
        self.add_button = QPushButton("Talaba qo'shish", clicked=self.Add)
        self.add_button.setStyleSheet("QPushButton {color:white;background-color:green; font-size:22px; font-weight:bold;} QPushButton:hover {background-color: rgb(9, 143, 76); border-color: rgb(50, 50, 150);}")
        self.h_buttons_lay.addWidget(self.add_button)

        # Search Button
        self.search_button = QPushButton("Qiridish", clicked = self.SearchButton)
        self.search_button.setStyleSheet("QPushButton {color:white; font-size:22px; background-color:rgb(129, 133, 140);font-weight:bold;} QPushButton:hover {background-color: rgb(200, 200, 200); border-color: rgb(50, 50, 150);}")
        self.h_buttons_lay.addWidget(self.search_button)

        # Update Button
        self.update_button = QPushButton("Yangilash", clicked = self.Update)
        self.update_button.setStyleSheet("QPushButton {color:black;background-color:yellow; font-size:22px; font-weight:bold;} QPushButton:hover {background-color: rgb(209, 171, 31); border-color: rgb(50, 50, 150);}")
        self.h_buttons_lay.addWidget(self.update_button)

        # Delete Button
        self.delete_button = QPushButton("O'chirish", clicked=self.Delete)
        self.delete_button.setStyleSheet("QPushButton {color:white;background-color:red; font-size:22px; font-weight:bold;} QPushButton:hover {background-color: rgb(145, 22, 26); border-color: rgb(50, 50, 150);}")
        self.h_buttons_lay.addWidget(self.delete_button)

        # vazifalar bo'limi
        self.task_button = QPushButton("Vazilarlar")
        self.task_button.setStyleSheet("QPushButton {color:white;background-color:red; font-size:22px; font-weight:bold;} QPushButton:hover {background-color: rgb(145, 22, 26); border-color: rgb(50, 50, 150);}")
        self.h_buttons_lay.addWidget(self.task_button)
        




        # Table to display students
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Talaba Ism Fam", "Vaqti", "Kun"])
        self.table.setStyleSheet("color:rgb(8, 68, 120); font-size:22px; font-weight:bold;")
        self.table.adjustSize()



        


        
        self.frame_layout.addLayout(self.h_buttons_lay)
        self.frame_layout.addWidget(self.table)


        # menyu button 
        self.menyu_button = QPushButton("Orqaga", clicked = self.Menyu)
        self.menyu_button.setStyleSheet("QPushButton {color:white;background-color:rgb(48, 171, 171); font-size:22px; font-weight:bold;} QPushButton:hover{background-color: rgb(200, 200, 200); border-color: rgb(50, 50, 150);} ")

        self.frame_layout.addWidget(self.menyu_button)

        # exit button
        self.exit_button = QPushButton("Dasturni tugatish", clicked= self.Exit)
        self.exit_button.setStyleSheet("QPushButton {color:white;background:black; font-size:22px; font-weight:bold;} QPushButton:hover{background-color: rgb(200, 200, 200); border-color: rgb(50, 50, 150);} ")

        self.frame_layout.addWidget(self.exit_button)
        


        self.v_main.addWidget(self.frame_button)
        self.setLayout(self.v_main)


        self.load_students()

    def load_students(self):
        self.dataBaze = TalabaSql()
        students = self.dataBaze.GetAllStudents()  
        self.table.setRowCount(0)  
        for student in students:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(student[0]))
            self.table.setItem(row_position, 1, QTableWidgetItem(student[1]))
            self.table.setItem(row_position, 2, QTableWidgetItem(student[2]))

    def Add(self):
        name = self.student_name_edit.text().lower()
        time = self.time_combo.currentText()
        day = self.day_combo.currentText().lower()
        self.dataBaze = TalabaSql()

        if name and time and day:
            if not self.dataBaze.Check(name, time, day):
                self.dataBaze.InsertTb(name, time, day)

                self.load_students()
                self.student_name_edit.clear()


                aniq_vaqt = datetime.now()
                with open ("allInfo.txt" , "a") as f:
                    f.write(f"talaba ismi  = {name}\t qaysi vaqtda o'qishga kelishi = {time}\t qaysi kunlari o'qishga kelishi = {day}\tguruh qo'shilgan vaqti = {aniq_vaqt}\n")
                
            else:
                self.msg = QMessageBox()
                self.msg.setText("Bu talaba sizda avvaldan mavjud")
                self.msg.setIcon(QMessageBox.Warning)
                self.msg.exec_()  
        else:
            self.msg = QMessageBox()
            self.msg.setText("Ma'lumotlarni to'liq kiritmadingiz")
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.exec_()  

    
   
    def SearchButton(self):
        name = self.student_name_edit.text().lower()
        time = self.time_combo.currentText()
        day = self.day_combo.currentText().lower()

        if name and day and time:
            search_result = self.dataBaze.Search_student(name, time, day)
            if search_result:
                self.table.setRowCount(0)
                for student_1 in search_result:
                    row_position = self.table.rowCount()
                    self.table.insertRow(row_position)

                
                    self.table.setItem(row_position, 0, QTableWidgetItem(student_1[0]))  # Talaba Ismi
                    self.table.setItem(row_position, 1, QTableWidgetItem(student_1[1]))  # Vaqti
                    self.table.setItem(row_position, 2, QTableWidgetItem(student_1[2]))  # Kuni
                  
            else:
                self.student_name_edit.clear()
                self.msg = QMessageBox()
                self.msg.setText("Talaba topilmadi. Ma'lumotlarni tekshiring.")
                self.msg.setIcon(QMessageBox.Warning)
                self.msg.exec_()
        else:
                self.student_name_edit.clear()
                self.msg = QMessageBox()
                self.msg.setText("To'liq ma'lumot kiritmagansiz.")
                self.msg.setIcon(QMessageBox.Warning)
                self.msg.exec_()



    def Delete(self):
        name = self.student_name_edit.text().lower()
        time = self.time_combo.currentText()
        day = self.day_combo.currentText().lower()

        if name and time and day:
            if self.dataBaze.Check(name, time, day):
                self.dataBaze.Delete(name, time, day)
                self.load_students()  
                self.student_name_edit.clear()
              
                self.msg = QMessageBox()
                self.msg.setText("Talaba ro'yhatidan chiqarildi")
                self.msg.setIcon(QMessageBox.Information)
                self.msg.exec_()

                deleted_time = datetime.now()
                with open ("deleted_StudentInfo.txt" , "a") as f:
                    f.write(f"talaba ismi = {name}\t guruhlarga kelish vaqti = {time}\t dars kunlari = {day}\t guruhdan o'chirilgan vaqti  ={deleted_time}\n")
            else:
                self.msg = QMessageBox()
                self.msg.setText("Talaba topilmadi. Ma'lumotlarni tekshiring.")
                self.msg.setIcon(QMessageBox.Warning)
                self.msg.exec_()
        else:
            self.msg = QMessageBox()
            self.msg.setText("Ma'lumotlarni to'liq kiriting")
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.exec_()


    

    def Menyu(self):
        self.main.show()
        self.hide()


    def Exit(self):
        self.close()

    def Update(self):
        name = self.student_name_edit.text().lower()
        time = self.time_combo.currentText()
        day = self.day_combo.currentText().lower()
        if name and time and day:
                self.dataBaze.UpdatingTalabaTable(name, time, day)
                self.msg = QMessageBox()
                self.msg.setText("Talabaning ma'lumotlari yangilandi")
                self.msg.setIcon(QMessageBox.Information)
                self.msg.exec_()
        else:
            self.msg = QMessageBox()
            self.msg.setText("Talabaning ma'lumotlarini to'g'ri kiritmadingiz")
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.exec_()
        self.load_students()

            



        



                
                
            
        



        

            


