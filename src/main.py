from bank import BankAccountSystem

def main():
    system = BankAccountSystem("bank.db")
    system.create_table()

    # Create some sample accounts
    accounts = [
        {"account_number": 1, "name": "John Doe", "email": "johndoe@example.com", "phone_number": 1234567890, "balance": 1000},
        {"account_number": 2, "name": "Jane Doe", "email": "janedoe@example.com", "phone_number": 9876543210, "balance": 500},
        {"account_number": 3, "name": "Bob Smith", "email": "bobsmith@example.com", "phone_number": 5551234567, "balance": 2000},
    ]

    for account in accounts:
        system.create_account(account["account_number"], account["name"], account["email"], account["phone_number"], account["balance"])

    # Perform some transactions
    transactions = [
        {"type": "deposit", "account_number": 1, "amount": 500},
        {"type": "withdraw", "account_number": 2, "amount": 200},
        {"type": "deposit", "account_number": 3, "amount": 1000},
    ]

    system.process_transactions(transactions)

    # Show account balances and transaction history
    system.show_customer_details()
    system.show_total_customers()

    for account_number in [1, 2, 3]:
        system.show_transaction_history(account_number)

#main()