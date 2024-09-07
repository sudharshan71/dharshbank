import sqlite3
from tabulate import tabulate
from tqdm import tqdm

class BankAccountSystem:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                account_number INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone_number INTEGER NOT NULL,
                balance REAL NOT NULL DEFAULT 0
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transaction_history (
                transaction_id INTEGER PRIMARY KEY,
                account_number INTEGER NOT NULL,
                transaction_type TEXT NOT NULL,
                amount REAL NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (account_number) REFERENCES accounts (account_number)
            )
        ''')
        self.conn.commit()

    def create_account(self, account_number, name, email, phone_number, balance=0):
        self.cursor.execute('''
            SELECT * FROM accounts WHERE account_number = ?
        ''', (account_number,))
        if self.cursor.fetchone():
            print("Account already exists!")
        else:
            self.cursor.execute('''
                INSERT INTO accounts (account_number, name, email, phone_number, balance)
                VALUES (?, ?, ?, ?, ?)
            ''', (account_number, name, email, phone_number, balance))
            self.conn.commit()
            print("Account created successfully!")

    def deposit(self, account_number, amount):
        self.cursor.execute('''
            UPDATE accounts
            SET balance = balance + ?
            WHERE account_number = ?
        ''', (amount, account_number))
        self.conn.commit()
        self.cursor.execute('''
            INSERT INTO transaction_history (account_number, transaction_type, amount)
            VALUES (?, ?, ?)
        ''', (account_number, "deposit", amount))
        self.conn.commit()

    def withdraw(self, account_number, amount):
        self.cursor.execute('''
            SELECT balance
            FROM accounts
            WHERE account_number = ?
        ''', (account_number,))
        balance = self.cursor.fetchone()[0]
        if amount > balance:
            print("Insufficient balance!")
        else:
            self.cursor.execute('''
                UPDATE accounts
                SET balance = balance - ?
                WHERE account_number = ?
            ''', (amount, account_number))
            self.conn.commit()
            self.cursor.execute('''
                INSERT INTO transaction_history (account_number, transaction_type, amount)
                VALUES (?, ?, ?)
            ''', (account_number, "withdraw", amount))
            self.conn.commit()

    def check_balance(self, account_number):
        self.cursor.execute('''
            SELECT balance
            FROM accounts
            WHERE account_number = ?
        ''', (account_number,))
        balance = self.cursor.fetchone()[0]
        print(f"Account balance: ${balance:.2f}")

    def show_total_customers(self):
        self.cursor.execute('''
            SELECT COUNT(*)
            FROM accounts
        ''')
        total_customers = self.cursor.fetchone()[0]
        print(f"Total customers: {total_customers}")

    def show_customer_details(self):
        self.cursor.execute('''
            SELECT * FROM accounts
        ''')
        rows = self.cursor.fetchall()
        headers = ["Account Number", "Name", "Email", "Phone Number", "Balance"]
        print(tabulate(rows, headers, tablefmt="grid"))
    
    def show_transaction_history(self, account_number):
        self.cursor.execute('''
            SELECT * FROM transaction_history
            WHERE account_number = ?
        ''', (account_number,))
        rows = self.cursor.fetchall()
        headers = ["Transaction ID", "Account Number", "Transaction Type", "Amount", "Timestamp"]
        print(tabulate(rows, headers, tablefmt="grid"))

    def process_transactions(self, transactions):
        for transaction in tqdm(transactions, desc="Processing transactions"):
            if transaction["type"] == "deposit":
                self.deposit(transaction["account_number"], transaction["amount"])
            elif transaction["type"] == "withdraw":
                self.withdraw(transaction["account_number"], transaction["amount"])