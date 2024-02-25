import sqlite3
import os
from dotenv import load_dotenv


load_dotenv()
DB_FILE = os.getenv('DB_FILE')


class DBHandler:
    tables_creation = ('dates (id INTEGER PRIMARY KEY AUTOINCREMENT, date DATE)',
                       'study_levels (id INTEGER PRIMARY KEY AUTOINCREMENT, level TEXT)',
                       'group_statuses (id INTEGER PRIMARY KEY AUTOINCREMENT, status TEXT)',
                       'student_statuses (id INTEGER PRIMARY KEY AUTOINCREMENT, status TEXT)',
                       'lesson_statuses (id INTEGER PRIMARY KEY AUTOINCREMENT, status TEXT)',
                       'groups (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, study_level_id INTEGER, group_status_id INTEGER, is_individual BOOLEAN, is_stable BOOLEAN, lesson_duration INTEGER, lesson_cost FLOAT, study_platform TEXT, description TEXT)',
                       'students (id INTEGER PRIMARY KEY AUTOINCREMENT, lastname TEXT, name TEXT, surname TEXT, birthday DATE, email TEXT, messenger TEXT, balance FLOAT, description TEXT)',
                       'contracts (id INTEGER PRIMARY KEY AUTOINCREMENT, student_id INTEGER, number INTEGER, date_id INTEGER, group_id INTEGER)',
                       'phone_numbers (id INTEGER PRIMARY KEY AUTOINCREMENT, phone_number TEXT, student_id INTEGER, description TEXT)',
                       'payments (id INTEGER PRIMARY KEY AUTOINCREMENT, date_id INTEGER, student_id INTEGER, amount FLOAT)',
                       'group_members (id INTEGER PRIMARY KEY AUTOINCREMENT, group_id INTEGER, student_id INTEGER, student_status_id INTEGER, discount INTEGER, grade TEXT)',
                       'schedules (id INTEGER PRIMARY KEY AUTOINCREMENT, group_id INTEGER, day TEXT, start TIME, end TIME)',
                       'lessons (id INTEGER PRIMARY KEY AUTOINCREMENT, date_id INTEGER, group_id INTEGER, start TIME, end TIME, cost FLOAT, lesson_status_id INTEGER)'
                       )

    def __init__(self):
        self.db = sqlite3.connect(DB_FILE)
        self.cursor = self.db.cursor()
        for table_creation in self.tables_creation:
            self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_creation}''')

    def close_connection(self) -> None:
        self.cursor.close()
        self.db.close()

    def set_mail_last_uid(self, new_uid: int) -> None:
        self.cursor.execute('''UPDATE mail SET last_uid = ?''', (new_uid, ))
        self.db.commit()

    def get_mail_last_uid(self) -> int:
        self.cursor.execute('''SELECT last_uid FROM mail''')
        uid = self.cursor.fetchall()
        if uid:
            return uid[0][0]
        else:
            self.set_mail_start_uid()
            return 1  # self.get_mail_last_uid() should I use recursive function???

    def set_mail_start_uid(self) -> None:
        self.cursor.execute('''INSERT INTO mail (last_uid) VALUES (?)''', (1, ))
        self.db.commit()

    def date_check(self, date: str) -> int:
        self.cursor.execute('''SELECT id, date FROM dates WHERE date = ?''', (date,))
        date_info = self.cursor.fetchall()
        if date_info:
            return date_info[0][0]
        else:
            self.cursor.execute('''INSERT INTO dates (date) VALUES (?)''', (date,))
            self.db.commit()
            return self.date_check(date=date)

    def product_check(self, product: str) -> int:
        self.cursor.execute('''SELECT id, product FROM products WHERE product = ?''', (product,))
        product_info = self.cursor.fetchall()
        if product_info:
            return product_info[0][0]
        else:
            self.cursor.execute('''INSERT INTO products (product) VALUES (?)''', (product,))
            self.db.commit()
            return self.product_check(product=product)

    def code_check(self, code: str, title: str, product_id: int) -> int:
        self.cursor.execute('''SELECT id, code, title FROM codes WHERE code = ?''', (code,))
        code_info = self.cursor.fetchall()
        if code_info:
            if code_info[0][2] != title:
                self.cursor.execute('''UPDATE codes SET title = ? WHERE code = ?''', (title, code))
                self.db.commit()
            return code_info[0][0]
        else:
            self.cursor.execute('''INSERT INTO codes (code, title, product_id) VALUES (?, ?, ?)''',
                                (code, title, product_id))
            self.db.commit()
            return self.code_check(code=code, title=title, product_id=product_id)

    def insert_new_data(self, date: str, product: str, code: str, title: str, amount: int) -> None:
        date_id = self.date_check(date=date)
        product_id = self.product_check(product=product)
        code_id = self.code_check(code=code, title=title, product_id=product_id)
        self.cursor.execute('''INSERT INTO orders (date_id, code_id, amount) VALUES (?, ?, ?)''',
                            (date_id, code_id, amount))
        self.db.commit()