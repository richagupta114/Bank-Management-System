from tkinter import messagebox, Toplevel, Label, Entry, Button, Frame, Text
from tkinter import ttk
from datetime import datetime

class TransactionManagement:
    def __init__(self, bank_system):
        self.bank_system = bank_system
    
    def deposit(self):
        """Handle deposit transaction"""
        if not self.bank_system.current_user:
            messagebox.showerror("Error", "Please login first!")
            return
        
        # Create deposit window
        deposit_window = Toplevel(self.bank_system.root)
        deposit_window.title("Deposit")
        deposit_window.geometry("300x200")
        
        # Create frame
        frame = Frame(deposit_window)
        frame.pack(padx=20, pady=20)
        
        # Amount entry
        Label(frame, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
        amount_entry = Entry(frame)
        amount_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Deposit button
        Button(frame, text="Deposit", 
            command=lambda: self._process_deposit(amount_entry.get(), deposit_window)).grid(row=1, column=0, columnspan=2, pady=10)
    
    def _process_deposit(self, amount, window):
        """Process deposit transaction"""
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive amount!")
            return
        
        # Update balance
        user_data = self.bank_system.users[self.bank_system.current_user]
        user_data['balance'] += amount
        
        # Log transaction
        self.log_transaction("Deposit", amount)
        
        # Update balance display
        self.bank_system.update_balance_display()
        
        # Show success message and close window
        messagebox.showinfo("Success", f"${amount:.2f} deposited successfully!")
        window.destroy()
    
    def withdraw(self):
        """Handle withdrawal transaction"""
        if not self.bank_system.current_user:
            messagebox.showerror("Error", "Please login first!")
            return
        
        # Create withdrawal window
        withdraw_window = Toplevel(self.bank_system.root)
        withdraw_window.title("Withdraw")
        withdraw_window.geometry("300x200")
        
        # Create frame
        frame = Frame(withdraw_window)
        frame.pack(padx=20, pady=20)
        
        # Amount entry
        Label(frame, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
        amount_entry = Entry(frame)
        amount_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Withdraw button
        Button(frame, text="Withdraw", 
            command=lambda: self._process_withdraw(amount_entry.get(), withdraw_window)).grid(row=1, column=0, columnspan=2, pady=10)
    
    def _process_withdraw(self, amount, window):
        """Process withdrawal transaction"""
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive amount!")
            return
        
        user_data = self.bank_system.users[self.bank_system.current_user]
        
        # Check minimum balance requirement
        account_type = user_data.get('account_type', 'Savings')
        min_balance = self.bank_system.account_types[account_type]['min_balance']
        
        if user_data['balance'] - amount < min_balance:
            messagebox.showerror("Error", 
                f"Insufficient balance! Minimum balance requirement: ${min_balance:.2f}")
            return
        
        # Update balance
        user_data['balance'] -= amount
        
        # Log transaction
        self.log_transaction("Withdrawal", -amount)
        
        # Update balance display
        self.bank_system.update_balance_display()
        
        # Show success message and close window
        messagebox.showinfo("Success", f"${amount:.2f} withdrawn successfully!")
        window.destroy()
    
    def transfer(self):
        """Handle transfer transaction"""
        if not self.bank_system.current_user:
            messagebox.showerror("Error", "Please login first!")
            return
        
        # Create transfer window
        transfer_window = Toplevel(self.bank_system.root)
        transfer_window.title("Transfer")
        transfer_window.geometry("300x250")
        
        # Create frame
        frame = Frame(transfer_window)
        frame.pack(padx=20, pady=20)
        
        # Recipient entry
        Label(frame, text="Recipient:").grid(row=0, column=0, padx=5, pady=5)
        recipient_entry = Entry(frame)
        recipient_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Amount entry
        Label(frame, text="Amount:").grid(row=1, column=0, padx=5, pady=5)
        amount_entry = Entry(frame)
        amount_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Transfer button
        Button(frame, text="Transfer", 
            command=lambda: self._process_transfer(
                recipient_entry.get(),
                amount_entry.get(),
                transfer_window
            )).grid(row=2, column=0, columnspan=2, pady=10)
    
    def _process_transfer(self, recipient, amount, window):
        """Process transfer transaction"""
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive amount!")
            return
        
        # Check if recipient exists
        if recipient not in self.bank_system.users:
            messagebox.showerror("Error", "Recipient not found!")
            return
        
        # Check if trying to transfer to self
        if recipient == self.bank_system.current_user:
            messagebox.showerror("Error", "Cannot transfer to yourself!")
            return
        
        sender_data = self.bank_system.users[self.bank_system.current_user]
        recipient_data = self.bank_system.users[recipient]
        
        # Check minimum balance requirement
        account_type = sender_data.get('account_type', 'Savings')
        min_balance = self.bank_system.account_types[account_type]['min_balance']
        
        if sender_data['balance'] - amount < min_balance:
            messagebox.showerror("Error", 
                f"Insufficient balance! Minimum balance requirement: ${min_balance:.2f}")
            return
        
        # Update balances
        sender_data['balance'] -= amount
        recipient_data['balance'] += amount
        
        # Log transactions
        self.log_transaction("Transfer to " + recipient, -amount)
        self._log_transaction_for_user(recipient, "Transfer from " + self.bank_system.current_user, amount)
        
        # Update balance display
        self.bank_system.update_balance_display()
        
        # Show success message and close window
        messagebox.showinfo("Success", f"${amount:.2f} transferred successfully to {recipient}!")
        window.destroy()
    
    def log_transaction(self, transaction_type, amount):
        """Log a transaction for the current user"""
        self._log_transaction_for_user(self.bank_system.current_user, transaction_type, amount)
    
    def _log_transaction_for_user(self, username, transaction_type, amount):
        """Log a transaction for a specific user"""
        user_data = self.bank_system.users[username]
        
        # Initialize transaction log if it doesn't exist
        if 'transactions' not in user_data:
            user_data['transactions'] = []
        
        # Create transaction record
        transaction = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'type': transaction_type,
            'amount': amount,
            'balance': user_data['balance']
        }
        
        # Add transaction to log
        user_data['transactions'].append(transaction)
    
    def view_transaction_log(self):
        """Show transaction log window"""
        if not self.bank_system.current_user:
            messagebox.showerror("Error", "Please login first!")
            return
        
        # Create transaction log window
        log_window = Toplevel(self.bank_system.root)
        log_window.title("Transaction Log")
        log_window.geometry("600x400")
        
        # Create frame
        frame = Frame(log_window)
        frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        # Create text widget with custom styling
        text_widget = Text(frame, width=70, height=20, font=('Arial', 10))
        text_widget.pack(side='left', fill='both', expand=True)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(frame, orient='vertical', command=text_widget.yview)
        scrollbar.pack(side='right', fill='y')
        text_widget.configure(yscrollcommand=scrollbar.set)
        
        # Get user's transactions
        user_data = self.bank_system.users[self.bank_system.current_user]
        transactions = user_data.get('transactions', [])
        
        # Display transactions
        if transactions:
            # Add header
            text_widget.insert('end', "Transaction History\n", 'header')
            text_widget.insert('end', "=" * 50 + "\n\n")
            
            # Display each transaction
            for transaction in transactions:
                text_widget.insert('end',
                    f"Date: {transaction['date']}\n"
                    f"Type: {transaction['type']}\n"
                    f"Amount: ${abs(transaction['amount']):.2f}\n"
                    f"Balance: ${transaction['balance']:.2f}\n"
                    f"{'-'*50}\n\n"
                )
        else:
            text_widget.insert('end', "No transactions found.\n")
        
        # Configure tags for styling
        text_widget.tag_configure('header', font=('Arial', 12, 'bold'))
        
        # Make text widget read-only
        text_widget.configure(state='disabled') 