**Bank Account System**
======================

A simple bank account system implemented in Python, using SQLite as the database.

**Features**
------------

* Create and manage bank accounts
* Deposit and withdraw funds
* View account balances and transaction history
* Track total number of customers

**Getting Started**
---------------

1. Clone the repository: `git clone https://github.com/your-username/bank-account-system.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the system: `python main.py`

**Usage**
-----

* Create an account: `system.create_account(account_number, name, email, phone_number, balance)`
* Deposit funds: `system.deposit(account_number, amount)`
* Withdraw funds: `system.withdraw(account_number, amount)`
* Check account balance: `system.check_balance(account_number)`
* Show customer details: `system.show_customer_details()`
* Show total customers: `system.show_total_customers()`

**Directory Structure**
---------------------

* `src/`: The package containing the system's modules
	+ `__main__.py`: Initializes the package
	+ `main.py`: Database module
	+ `bank.py`: Account and Transaction models & The main system module
* `main.py`: The entry point for the system
* `requirements.txt`: Lists the required dependencies

**License**
-------

This project is licensed under the MIT License. See `LICENSE` for details.

**Contributing**
------------

Contributions are welcome! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request.

**Author**
------

Sudharshan
