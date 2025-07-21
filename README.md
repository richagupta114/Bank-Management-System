# Bank Management System

A comprehensive banking system built with Python and Tkinter, featuring user account management, transactions, financial tools, and administrative controls.

## Features

- User Account Management
  - Account creation and login
  - PIN management and security settings
  - Account type selection (Savings, Current, Fixed Deposit)

- Transaction Management
  - Deposits and withdrawals
  - Fund transfers between accounts
  - Transaction history and logging

- Financial Tools
  - Loan calculator
  - EMI calculator
  - Interest calculator

- Security Features
  - PIN protection
  - Security questions
  - Login attempt tracking
  - Account locking after multiple failed attempts

- Administrative Controls
  - User management
  - System settings
  - Account type configuration

## Project Structure

```
bank-management-system/
├── main.py                 # Main entry point
├── bank_system.py          # Core banking system
├── account_management.py   # Account-related functionality
├── transaction_management.py # Transaction handling
├── security_management.py  # Security features
├── admin_panel.py         # Administrative controls
├── financial_tools.py     # Financial calculators
├── ui_components.py       # Reusable UI elements
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/bank-management-system.git
   cd bank-management-system
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python main.py
   ```

## Usage

1. Launch the application using `python main.py`
2. Create a new account or login with existing credentials
3. Use the various features available in the user dashboard
4. Access financial tools for calculations
5. Administrators can access the admin panel for system management

## Security Considerations

- PINs are stored in plain text for demonstration purposes. In a production environment, use proper encryption.
- Implement proper session management and timeout mechanisms.
- Add additional security layers like OTP verification for sensitive operations.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with Python and Tkinter
- Inspired by modern banking systems
- Created for educational purposes

<h1 align="center"> Bank Management System 🏦 </h1>


| ![Screenshot from 2023-03-21 13-34-33](https://user-images.githubusercontent.com/77020164/227250461-fdabfefc-1ab7-4b0e-97bb-e798fd3bfd64.png) | ![Screenshot from 2023-03-14 14-17-29](https://user-images.githubusercontent.com/77020164/225007866-fae033ba-1696-4d02-9015-8d700f87faa0.png) 
|-|-|
| ![Screenshot from 2023-03-13 23-58-53](https://user-images.githubusercontent.com/77020164/225008278-2c693b5d-3236-476c-903a-15a244e18a32.png) | ![Screenshot from 2023-03-23 20-54-29](https://user-images.githubusercontent.com/77020164/227252416-e2525b05-44db-40d1-975d-efc2de0ae2af.png)|
| ![Screenshot from 2023-03-23 20-55-27](https://user-images.githubusercontent.com/77020164/227252530-caa81399-610f-4034-8ff6-e70911d055bc.png) | ![Screenshot from 2023-03-23 20-55-09](https://user-images.githubusercontent.com/77020164/227252707-215ccd74-30d2-4641-967a-4e5c6a3633d6.png)



## Demo Video:

[Screencast from 07-04-23 10:32:50 PM IST.webm](https://user-images.githubusercontent.com/77020164/230648449-6332a8a2-22ce-4525-874a-85d6bce9bf79.webm)


## About
The Bank Management System is a software application designed to handle various banking activities such as account creation, deposit, withdrawal, money transfer, account balance inquiry, and transaction history. It provides a user-friendly interface to customers and bank employees to manage their banking operations efficiently.

## Blog

Check out our project blog post for more information on the development process and our thoughts on the Bank Management project:

* [Bank Management System Using Python](https://www.codingninjas.com/codestudio/library/bank-management-system-project-in-python?utm_source=github&utm_medium=organic&utm_campaign=blog-bank-management-system-project-in-python)


## Features
* User login and Create Account
* Deposit and withdrawal transactions
* Account balance inquiry
* Transaction history view


## Requirements
* Python 3.x
* Tkinter library (which is usually included with Python)


## Getting Started
1. Clone this repository to your local machine.
2. Open a terminal window and navigate to the cloned repository.
3. Run the following command to start the program: python bank-management.py

## Code Structure

The code is organized into the following functions:

- `__init__(self, master)` : This function initializes the BankSystem object with the specified parameters, sets the title and geometry of the main window, and creates the "Create Account" and "Login" frames.
- `create_account()` : This function creates a new account with the name, age, salary, and PIN entered by the user in the corresponding Entry widgets.
- `login()` : This function validates the entered PIN against the saved account details and displays the account information if the PIN is correct.
- `deposit()` : This function allows the user to deposit money into their bank account and updates the balance accordingly.
- `withdraw()` : This function allows the user to withdraw money from their bank account, if the balance is sufficient, and updates the balance accordingly.
- `view_transaction()` : This function allows the user to view their transaction history for the current session.

### The code also defines the following labels and buttons for the game:

- Labels:
    - `name_label` : This label displays "Name:" in the "Create Account" frame.
    - `age_label` : This label displays "Age:" in the "Create Account" frame.
    - `salary_label` : This label displays "Salary:" in the "Create Account" frame.
    - `pin_label` : This label displays "PIN:" in the "Create Account" frame.
    - `login_pin_label` : This label displays "PIN:" in the "Login" frame.
- Entry widgets:
    - `name_entry` : This Entry widget allows the user to enter their name in the "Create Account" frame.
    - `age_entry` : This Entry widget allows the user to enter their age in the "Create Account" frame.
    - `salary_entry` : This Entry widget allows the user to enter their salary in the "Create Account" frame.
    - `pin_entry` : This Entry widget allows the user to enter their PIN in the "Create Account" frame.
    - `login_pin_entry` : This Entry widget allows the user to enter their PIN in the "Login" frame.
- Buttons:
    - `create_account_button` : This button calls the `create_account()` function when clicked.
    - `login_button` : This button calls the `login()` function when clicked.



<div align="center">
  
## Made with ❤️ , Python, and Tkinter. Enjoy!
  
</div>

