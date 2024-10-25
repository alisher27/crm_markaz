import mysql.connector


class TalabaSql:
    def __init__(self):
        self.ConnectDb()
        self.CreateDb()
        self.CreateTb()
        self.CreatePaymentTable()

    def ConnectDb(self):
    
        self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234"
            )
        self.cursor = self.db.cursor()



    def CreateDb(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS talaba")
        self.cursor.execute("USE talaba")


    def CreateTb(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS talaba_table (
            id int auto_increment primary key,
            name TEXT,
            time TEXT,  
            day TEXT,
            active BOOLEAN default True,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)
        self.db.commit()


    def InsertTb(self, name, time, day):
        self.cursor.execute(f'INSERT INTO talaba_table (name, time, day) VALUES ("{name}", "{time}", "{day}")')
        self.db.commit()

    def Check(self, name, time, day):
        self.cursor.execute(f'SELECT name FROM talaba_table WHERE name = "{name}" and time = "{time}" and day= "{day}"')
        return self.cursor.fetchall()

    def GetAllStudents(self):
        self.cursor.execute("SELECT name, time, day FROM talaba_table")
        return self.cursor.fetchall()

    def Search_student(self, name, time, day):
        self.cursor.execute(f'SELECT name, time, day FROM talaba_table WHERE name ="{name}" and time = "{time}" and day = "{day}" ')
        return self.cursor.fetchall()

    def Delete(self, name, time, day):
        self.cursor.execute(f'DELETE FROM talaba_table WHERE name = "{name}" and time = "{time}" and day = "{day}"')
        self.db.commit()
        

    def CreatePaymentTable(self):
        self.cursor.execute('''CREATE TABLE if not exists talabaPayment (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name TEXT,
                            time TEXT,
                            day TEXT,
                            active BOOLEAN DEFAULT TRUE,
                            month TEXT, 
                            money INT,
                            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                            
                        )''')
        self.db.commit()

    def InsertPaymentTable(self, name, time, day, month, money):
        self.cursor.execute(f'''insert into talabaPayment (name, time, day, month, money) values ("{name}", "{time}", "{day}", "{month}", {money})''')
        self.db.commit()



    def Payment(self):
        self.cursor.execute(f'''select name, time, day json_array_agg''')




    def ShowTalabaInfo(self, time, day):
        self.cursor.execute(f'select name, time, day, month from talabaPayment where time = "{time}" and day ="{day}"')
        group = self.cursor.fetchall()
        return group
    

    def UpdatingTalabaTable(self, name, time, day):
        self.cursor.execute(f'Update talaba_table set time = "{time}" , day = "{day.lower()}" where name = "{name.lower()}"  ')
        self.db.commit()
        
   


    def close(self):
        self.cursor.close()
        self.db.close()
