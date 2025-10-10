from database import ExpenseTracker
from datetime import datetime

class ExpenseTrackerCLI:

    def __init__(self):
        self.expenses = ExpenseTracker()

    def record(self):
        try:
            date = input("Enter The Date (yyyy-mm-dd):")
            try:
                datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Use yyyy-mm-dd.")
                return
            try:
                amount = float(input("Enter The Amount: "))
            except ValueError:
                print("Amount must be a number.")
                return
            reason = input("Enter The Reason: ")
            is_inserted = self.expenses.insert(date=date, amount=amount, reason=reason)
            if is_inserted:
                print(f"Successfully Inserted ₹{amount:.2f} on {date} for {reason}!")
        except Exception as e:
            print(f"Error: {e}")
        
    def display(self):
        try:
            records = self.expenses.retrieve()
            print("\n--------Records--------\n")
            for record in records:
                print(f"{type(record[0])}) ₹{type(record[2])} on {type(record[1])} for {type(record[3])}")
        except Exception as e:
            print(e)
    
    def delete(self):
        try:
            id = int(input("Enter The Id: "))
            is_deleted = self.expenses.delete(id)
            if is_deleted:
                print("Record deleted successfully!")
        except Exception as e:
            print(e)
    
    def main(self):
        try:
            print("\nWelcome To Expenses Tracker")
            while True:
                print("\n1) Insert Record\n2) Delete Records\n3) Show Record\n4) Exit")
                choice = int(input("\nEnter The Choice: "))
                if choice == 1:
                    self.record()
                elif choice == 2:
                    self.delete()
                elif choice == 3:
                    self.display()
                elif choice == 4:
                    print("Thank You, Bye!")
                    break
                else:
                    print("Invalid Input!")
                    continue
        except Exception as e:
            print(e)

if __name__=="__main__":
    etcli = ExpenseTrackerCLI()
    etcli.main()