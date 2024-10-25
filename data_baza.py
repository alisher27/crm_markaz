import mysql.connector


class Mysql:
    def __init__(self):
        self.Connect()
        self.CreateDb()
        self.CreateTb()
        self.CreateTB_hodim()
        self.Insert_hodimTb()

    def Connect(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234"
        )
        self.cursor = self.db.cursor()

    def CreateDb(self):
        self.cursor.execute('CREATE DATABASE IF NOT EXISTS ustoz_loyiha')
        self.cursor.execute("USE ustoz_loyiha")

    def CreateTb(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS admin (
                                name VARCHAR(255) PRIMARY KEY,
                                password VARCHAR(255)
                              )''')
        self.db.commit()

        # Insert default admin user if the table is empty
        self.InsertTB()

    def InsertTB(self):
        # Check if the table is empty
        self.cursor.execute("SELECT COUNT(*) FROM admin")
        count = self.cursor.fetchone()[0]

        if count == 0:
            # Insert default admin values
            self.cursor.execute('INSERT INTO admin (name, password) VALUES (%s, %s)', ("admin", "1234"))
            self.db.commit()

    def Check_admin(self, name, password):
        self.cursor.execute(f'SELECT name FROM admin WHERE name= "{name}"  and password = "{password}"' )
        natija = self.cursor.fetchall()
        return natija

    # ------------------------------------hodim table 

    def CreateTB_hodim(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS hodim (name VARCHAR(255), parol VARCHAR(255))')
        self.db.commit()

    def Insert_hodimTb(self):
        # Check if the table is empty
        self.cursor.execute("SELECT COUNT(*) FROM hodim")
        count = self.cursor.fetchone()[0]

        if count == 0:
            # Insert default hodim values
            self.cursor.execute('INSERT INTO hodim (name, parol) VALUES (%s, %s)', ("ali", "1234"))
            self.db.commit()

    def Check_hodim(self, name, parol):
        self.cursor.execute(f'SELECT name FROM hodim WHERE name= "{name}" and parol = "{parol}"')
        res = self.cursor.fetchall()
        return res


    # --------------------------------------------
    