import mysql.connector as mc

class ExpenseTracker:

    def  __init__(self):
        self.connection = self.get_connection()

    def get_connection(self):
        connection = mc.connect(host='hostname',user='your username',password='your password',database="your database")
        return connection

    def insert(self, date, amount, reason):
        try:
            if self.connection is None:
                raise Exception("Database connection failed.")
            with self.connection.cursor() as cursor:
                query = "INSERT INTO expense_tracker (transaction_date, amount, reason) VALUES (%s, %s, %s)"
                cursor.execute(query, (date, amount, reason))
            self.connection.commit()
            return True
        except Exception as e:
            print("Insertion Failed:", e)
            return False

    def delete(self,id):
        try:
            if self.connection is None:
                raise Exception("Database connection failed.")
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM expense_tracker WHERE id = %s", (id,))
                record = cursor.fetchone()
                print("Deleting:", record)
                query = "DELETE FROM expense_tracker WHERE id = %s"
                cursor.execute(query,(id,))
            self.connection.commit()
            return True
        except Exception as e:
            print("Deletion Failed:", e)
            return False

    def retrieve(self):
        try:
            if self.connection is None:
                raise Exception("Database connection failed.")
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM expense_tracker")
                records = cursor.fetchall()
                if not records:
                    print("No records found.")
                    return []
                return records                    
        except Exception as e:
            print("Operation Failed:", e)
            return False