from tkinter import messagebox
import random

class AccountManagement:
    def __init__(self, bank_system):
        self.bank_system = bank_system
    
    def create_account(self):
        """Create a new user account"""
        # Get values from entry fields
        name = self.bank_system.name_entry.get().strip()
        age = self.bank_system.age_entry.get().strip()
        salary = self.bank_system.salary_entry.get().strip()
        pin = self.bank_system.pin_entry.get().strip()
        account_type = self.bank_system.account_type_var.get()
        security_question = self.bank_system.security_question_var.get()
        security_answer = self.bank_system.security_answer_entry.get().strip()
        
        # Validate inputs
        if not all([name, age, salary, pin, security_answer]):
            messagebox.showerror("Error", "All fields are required!")
            return
            
        try:
            age = int(age)
            salary = float(salary)
            if not pin.isdigit() or len(pin) != 4:
                raise ValueError("PIN must be a 4-digit number")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
            
        # Check if user already exists
        if name in self.bank_system.users:
            messagebox.showerror("Error", "User already exists!")
            return
            
        # Generate account number
        account_number = ''.join(random.choices('0123456789', k=10))
        
        # Create user data
        user_data = {
            'name': name,
            'age': age,
            'salary': salary,
            'pin': pin,
            'account_number': account_number,
            'balance': 0,
            'account_type': account_type,
            'security_question': security_question,
            'security_answer': security_answer,
            'transaction_log': []
        }
        
        # Add user to users dictionary
        self.bank_system.users[name] = user_data
        
        # Show success message
        messagebox.showinfo("Success", f"Account created successfully!\nYour account number is: {account_number}")
        
        # Clear entry fields
        self.bank_system.name_entry.delete(0, 'end')
        self.bank_system.age_entry.delete(0, 'end')
        self.bank_system.salary_entry.delete(0, 'end')
        self.bank_system.pin_entry.delete(0, 'end')
        self.bank_system.security_answer_entry.delete(0, 'end')
        
        # Switch back to login frame
        self.bank_system.create_account_frame.pack_forget()
        self.bank_system.login_frame.pack(pady=20)
    
    def login(self, event=None):
        """Handle user login"""
        name = self.bank_system.login_name_entry.get().strip()
        pin = self.bank_system.login_pin_entry.get().strip()
        
        # Check if user exists
        if name not in self.bank_system.users:
            messagebox.showerror("Error", "User not found!")
            return
        
        # Check if PIN is correct
        if self.bank_system.users[name]['pin'] != pin:
            # Increment login attempts
            if name not in self.bank_system.login_attempts:
                self.bank_system.login_attempts[name] = 0
            self.bank_system.login_attempts[name] += 1
            
            # Check if max attempts reached
            if self.bank_system.login_attempts[name] >= self.bank_system.max_login_attempts:
                messagebox.showerror("Error", "Account locked due to too many failed attempts. Please use 'Forgot PIN' to reset.")
                return
            else:
                messagebox.showerror("Error", f"Invalid PIN. {self.bank_system.max_login_attempts - self.bank_system.login_attempts[name]} attempts remaining.")
                return
        
        # Reset login attempts on successful login
        self.bank_system.login_attempts[name] = 0
        
        # Set current user
        self.bank_system.current_user = name
        
        # Update user details display
        user_data = self.bank_system.users[name]
        self.bank_system.name_display.config(text=f"Name: {user_data['name']}")
        self.bank_system.age_display.config(text=f"Age: {user_data['age']}")
        self.bank_system.salary_display.config(text=f"Salary: {user_data['salary']}")
        self.bank_system.balance_display.config(text=f"Balance: {user_data['balance']}")
        self.bank_system.account_type_display.config(text=f"Account Type: {user_data['account_type']}")
        
        # Hide login frame and show user frame
        self.bank_system.login_frame.pack_forget()
        self.bank_system.user_frame.pack(pady=20)
    
    def logout(self):
        """Handle user logout"""
        # Clear current user
        self.bank_system.current_user = None
        
        # Clear login fields
        self.bank_system.login_name_entry.delete(0, 'end')
        self.bank_system.login_pin_entry.delete(0, 'end')
        
        # Hide user frame and show login frame
        self.bank_system.user_frame.pack_forget()
        self.bank_system.login_frame.pack(pady=20) 