# Expense Tracker

This is a simple Python project to track your daily expenses.  
You can add, view, and manage expenses easily from the command line.

## Features
- Add new expenses with amount and description  
- View all saved expenses  
- Store expenses safely in a database  

## Requirements
- Python 3  
- MySQL  
- mysql-connector-python (Python package)  


## Database Schema

The project uses **MySQL** to store expense records.  
Below is the schema for the `Expense_Tracker` table:

```sql
CREATE TABLE Expense_Tracker (
    id INT PRIMARY KEY AUTO_INCREMENT,
    transaction_date DATE,
    amount DECIMAL(10,2),
    reason TEXT
);