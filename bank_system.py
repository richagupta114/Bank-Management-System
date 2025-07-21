from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
from datetime import datetime

# Import functionality modules
from account_management import AccountManagement
from transaction_management import TransactionManagement
from security_management import SecurityManagement
from admin_panel import AdminPanel
from financial_tools import FinancialTools

class BankSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Management System")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        
        # Initialize user data
        self.users = {}
        self.current_user = None
        self.login_attempts = {}
        self.max_login_attempts = 3
        
        # Admin credentials
        self.admin_username = "admin"
        self.admin_password = "admin123"
        
        # Create frames
        self.create_account_frame = ttk.Frame(root)
        self.login_frame = ttk.Frame(root)
        self.user_frame = ttk.Frame(root)
        
        # Create account type options
        self.account_types = {
            "Savings": {"min_balance": 1000, "interest_rate": 0.04},
            "Current": {"min_balance": 5000, "interest_rate": 0.02},
            "Fixed Deposit": {"min_balance": 10000, "interest_rate": 0.08}
        }
        
        # Security questions
        self.security_questions = [
            "What is your mother's maiden name?",
            "What is the name of your first pet?",
            "What is your favorite book?",
            "What is the name of the school you first attended?",
            "What is your favorite color?"
        ]
        
        # Initialize functionality modules
        self.account_management = AccountManagement(self)
        self.transaction_management = TransactionManagement(self)
        self.security_management = SecurityManagement(self)
        self.admin_panel = AdminPanel(self)
        self.financial_tools = FinancialTools(self)
        
        # Create the UI
        self.create_account_ui()
        self.login_ui()
        self.user_ui()
        
        # Show login frame by default
        self.login_frame.pack(pady=20)
    
    def update_balance_display(self):
        """Update the balance display in the user interface"""
        if self.current_user and hasattr(self, 'balance_display'):
            user_data = self.users[self.current_user]
            self.balance_display.config(text=f"Balance: ${user_data['balance']:.2f}")
    
    def create_account_ui(self):
        """Create the UI for account creation"""
        # Create Account Frame
        self.create_account_frame = Frame(self.root, bg='#F0F0F0')
        self.create_account_frame.pack(pady=20)

        # Labels
        self.name_label = Label(self.create_account_frame, text="Name:", font=('Arial', 12), bg='#F0F0F0')
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.age_label = Label(self.create_account_frame, text="Age:", font=('Arial', 12), bg='#F0F0F0')
        self.age_label.grid(row=1, column=0, padx=10, pady=10)
        self.salary_label = Label(self.create_account_frame, text="Salary:", font=('Arial', 12), bg='#F0F0F0')
        self.salary_label.grid(row=2, column=0, padx=10, pady=10)
        self.pin_label = Label(self.create_account_frame, text="PIN:", font=('Arial', 12), bg='#F0F0F0')
        self.pin_label.grid(row=3, column=0, padx=10, pady=10)
        self.account_type_label = Label(self.create_account_frame, text="Account Type:", font=('Arial', 12), bg='#F0F0F0')
        self.account_type_label.grid(row=4, column=0, padx=10, pady=10)
        
        # Security question label
        self.security_question_label = Label(self.create_account_frame, text="Security Question:", font=('Arial', 12), bg='#F0F0F0')
        self.security_question_label.grid(row=5, column=0, padx=10, pady=10)
        self.security_answer_label = Label(self.create_account_frame, text="Answer:", font=('Arial', 12), bg='#F0F0F0')
        self.security_answer_label.grid(row=6, column=0, padx=10, pady=10)

        # Entries
        self.name_entry = Entry(self.create_account_frame, font=('Arial', 12), bg='#FFFFFF', relief='solid', borderwidth=1)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.age_entry = Entry(self.create_account_frame, font=('Arial', 12), bg='#FFFFFF', relief='solid', borderwidth=1)
        self.age_entry.grid(row=1, column=1, padx=10, pady=10)
        self.salary_entry = Entry(self.create_account_frame, font=('Arial', 12), bg='#FFFFFF', relief='solid', borderwidth=1)
        self.salary_entry.grid(row=2, column=1, padx=10, pady=10)
        self.pin_entry = Entry(self.create_account_frame, show="*", font=('Arial', 12), bg='#FFFFFF', relief='solid', borderwidth=1)
        self.pin_entry.grid(row=3, column=1, padx=10, pady=10)
        
        # Account Type Dropdown
        self.account_type_var = StringVar(value='Savings')
        self.account_type_menu = OptionMenu(self.create_account_frame, self.account_type_var, *self.account_types.keys())
        self.account_type_menu.grid(row=4, column=1, padx=10, pady=10)
        
        # Security question dropdown and answer
        self.security_question_var = StringVar(value=list(self.security_questions)[0])
        self.security_question_menu = OptionMenu(self.create_account_frame, self.security_question_var, *self.security_questions)
        self.security_question_menu.grid(row=5, column=1, padx=10, pady=10)
        self.security_answer_entry = Entry(self.create_account_frame, font=('Arial', 12), bg='#FFFFFF', relief='solid', borderwidth=1)
        self.security_answer_entry.grid(row=6, column=1, padx=10, pady=10)

        # Create account button
        self.create_account_button = Button(self.create_account_frame, text="Create Account", font=('Arial', 12), bg='#4CAF50', fg='#FFFFFF', activebackground='#2E8B57', activeforeground='#FFFFFF', relief='raised', borderwidth=0, command=self.account_management.create_account)
        self.create_account_button.grid(row=7, column=1, pady=20)
    
    def login_ui(self):
        """Create the login UI"""
        # Login Frame
        self.login_frame = ttk.Frame(self.root)
        
        # Create main label
        ttk.Label(self.login_frame, text="Bank Management System", font=('Arial', 16, 'bold')).pack(pady=10)
        
        # Create login frame
        login_inner_frame = ttk.Frame(self.login_frame)
        login_inner_frame.pack(pady=20)
        
        # Username/Name
        ttk.Label(login_inner_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.login_name_entry = ttk.Entry(login_inner_frame)
        self.login_name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # PIN
        ttk.Label(login_inner_frame, text="PIN:").grid(row=1, column=0, padx=5, pady=5)
        self.login_pin_entry = ttk.Entry(login_inner_frame, show="*")
        self.login_pin_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Buttons frame
        button_frame = ttk.Frame(self.login_frame)
        button_frame.pack(pady=10)
        
        # Login button
        ttk.Button(button_frame, text="Login", command=self.account_management.login).pack(side='left', padx=5)
        
        # Create Account button
        ttk.Button(button_frame, text="Create Account", command=self.show_create_account).pack(side='left', padx=5)
        
        # Forgot PIN button
        ttk.Button(button_frame, text="Forgot PIN?", command=self.security_management.forgot_pin).pack(side='left', padx=5)
        
        # Bind Enter key to login
        self.root.bind('<Return>', lambda e: self.account_management.login())
    
    def user_ui(self):
        """Create the user interface"""
        # User Frame
        self.user_frame = ttk.Frame(self.root)
        
        # Create header
        ttk.Label(self.user_frame, text="User Dashboard", font=('Arial', 16, 'bold')).pack(pady=10)
        
        # User Details Frame
        details_frame = ttk.LabelFrame(self.user_frame, text="Account Details")
        details_frame.pack(padx=20, pady=10, fill="x")
        
        # Create and grid labels for user details
        self.name_display = ttk.Label(details_frame, text="Name: ")
        self.name_display.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        self.age_display = ttk.Label(details_frame, text="Age: ")
        self.age_display.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        
        self.salary_display = ttk.Label(details_frame, text="Salary: ")
        self.salary_display.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        
        self.balance_display = ttk.Label(details_frame, text="Balance: ")
        self.balance_display.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        
        self.account_type_display = ttk.Label(details_frame, text="Account Type: ")
        self.account_type_display.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        
        # Transaction Buttons Frame
        transaction_frame = ttk.LabelFrame(self.user_frame, text="Transactions")
        transaction_frame.pack(padx=20, pady=10, fill="x")
        
        # Create and pack transaction buttons
        ttk.Button(transaction_frame, text="Deposit", command=self.transaction_management.deposit).pack(side="left", padx=5, pady=5)
        ttk.Button(transaction_frame, text="Withdraw", command=self.transaction_management.withdraw).pack(side="left", padx=5, pady=5)
        ttk.Button(transaction_frame, text="Transfer", command=self.transaction_management.transfer).pack(side="left", padx=5, pady=5)
        ttk.Button(transaction_frame, text="View Transactions", command=self.transaction_management.view_transaction_log).pack(side="left", padx=5, pady=5)
        
        # Account Management Frame
        management_frame = ttk.LabelFrame(self.user_frame, text="Account Management")
        management_frame.pack(padx=20, pady=10, fill="x")
        
        # Create and pack management buttons
        ttk.Button(management_frame, text="Security Settings", command=self.security_management.show_security_settings).pack(side="left", padx=5, pady=5)
        ttk.Button(management_frame, text="Financial Tools", command=self.financial_tools.show_financial_tools).pack(side="left", padx=5, pady=5)
        ttk.Button(management_frame, text="Change PIN", command=self.security_management.change_pin).pack(side="left", padx=5, pady=5)
        ttk.Button(management_frame, text="Logout", command=self.account_management.logout).pack(side="left", padx=5, pady=5)
    
    def show_create_account(self):
        """Show the create account frame and hide other frames"""
        self.login_frame.pack_forget()
        self.user_frame.pack_forget()
        self.create_account_frame.pack(pady=20) 