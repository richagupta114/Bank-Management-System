from tkinter import messagebox, Toplevel, Label, Entry, Button, Frame, ttk
from tkinter import StringVar

class AdminPanel:
    def __init__(self, bank_system):
        self.bank_system = bank_system
    
    def show_admin_panel(self):
        """Show admin panel window"""
        # Create admin panel window
        admin_window = Toplevel(self.bank_system.root)
        admin_window.title("Admin Panel")
        admin_window.geometry("800x600")
        
        # Create notebook for tabs
        notebook = ttk.Notebook(admin_window)
        notebook.pack(expand=True, fill='both', padx=10, pady=10)
        
        # User Management tab
        user_frame = Frame(notebook)
        notebook.add(user_frame, text="User Management")
        self._create_user_management_tab(user_frame)
        
        # System Settings tab
        settings_frame = Frame(notebook)
        notebook.add(settings_frame, text="System Settings")
        self._create_system_settings_tab(settings_frame)
    
    def _create_user_management_tab(self, parent):
        """Create user management tab"""
        # Create treeview for users
        columns = ('Username', 'Name', 'Account Number', 'Balance', 'Account Type')
        tree = ttk.Treeview(parent, columns=columns, show='headings')
        
        # Set column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(parent, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack widgets
        tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Populate treeview
        self._populate_user_tree(tree)
        
        # Create buttons frame
        button_frame = Frame(parent)
        button_frame.pack(fill='x', padx=5, pady=5)
        
        # Add buttons
        Button(button_frame, text="Refresh", command=lambda: self._populate_user_tree(tree)).pack(side='left', padx=5)
        Button(button_frame, text="Delete User", command=lambda: self._delete_user(tree)).pack(side='left', padx=5)
        Button(button_frame, text="Edit User", command=lambda: self._edit_user(tree)).pack(side='left', padx=5)
    
    def _create_system_settings_tab(self, parent):
        """Create system settings tab"""
        # Create frame for settings
        frame = Frame(parent)
        frame.pack(padx=20, pady=20)
        
        # Account type settings
        Label(frame, text="Account Type Settings", font=('Arial', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Create variables for minimum balances
        min_balance_vars = {}
        row = 1
        for acc_type, settings in self.bank_system.account_types.items():
            Label(frame, text=f"{acc_type} Minimum Balance:").grid(row=row, column=0, padx=5, pady=5)
            var = StringVar(value=str(settings['min_balance']))
            min_balance_vars[acc_type] = var
            Entry(frame, textvariable=var).grid(row=row, column=1, padx=5, pady=5)
            row += 1
        
        # Save button
        Button(frame, text="Save Settings", command=lambda: self._save_system_settings(min_balance_vars)).grid(row=row, column=0, columnspan=2, pady=10)
    
    def _populate_user_tree(self, tree):
        """Populate user treeview"""
        # Clear existing items
        for item in tree.get_children():
            tree.delete(item)
        
        # Add users
        for username, user_data in self.bank_system.users.items():
            tree.insert('', 'end', values=(
                username,
                user_data['name'],
                user_data['account_number'],
                user_data['balance'],
                user_data.get('account_type', 'Savings')
            ))
    
    def _delete_user(self, tree):
        """Delete selected user"""
        # Get selected item
        selection = tree.selection()
        if not selection:
            messagebox.showerror("Error", "Please select a user to delete!")
            return
        
        # Get username
        username = tree.item(selection[0])['values'][0]
        
        # Confirm deletion
        if messagebox.askyesno("Confirm", f"Are you sure you want to delete user {username}?"):
            # Delete user
            del self.bank_system.users[username]
            if username in self.bank_system.login_attempts:
                del self.bank_system.login_attempts[username]
            
            # Refresh treeview
            self._populate_user_tree(tree)
            messagebox.showinfo("Success", "User deleted successfully!")
    
    def _edit_user(self, tree):
        """Edit selected user"""
        # Get selected item
        selection = tree.selection()
        if not selection:
            messagebox.showerror("Error", "Please select a user to edit!")
            return
        
        # Get user data
        username = tree.item(selection[0])['values'][0]
        user_data = self.bank_system.users[username]
        
        # Create edit window
        edit_window = Toplevel(self.bank_system.root)
        edit_window.title("Edit User")
        edit_window.geometry("400x300")
        
        # Create frame
        frame = Frame(edit_window)
        frame.pack(padx=20, pady=20)
        
        # Name
        Label(frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        name_entry = Entry(frame)
        name_entry.insert(0, user_data['name'])
        name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Balance
        Label(frame, text="Balance:").grid(row=1, column=0, padx=5, pady=5)
        balance_entry = Entry(frame)
        balance_entry.insert(0, str(user_data['balance']))
        balance_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Account Type
        Label(frame, text="Account Type:").grid(row=2, column=0, padx=5, pady=5)
        acc_type_var = StringVar(value=user_data.get('account_type', 'Savings'))
        acc_type_menu = ttk.Combobox(frame, textvariable=acc_type_var, values=list(self.bank_system.account_types.keys()))
        acc_type_menu.grid(row=2, column=1, padx=5, pady=5)
        
        # Save button
        Button(frame, text="Save Changes", command=lambda: self._save_user_changes(
            username,
            name_entry.get(),
            balance_entry.get(),
            acc_type_var.get(),
            edit_window,
            tree
        )).grid(row=3, column=0, columnspan=2, pady=10)
    
    def _save_user_changes(self, username, name, balance, acc_type, window, tree):
        """Save user changes"""
        # Validate inputs
        if not name or not balance or not acc_type:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        try:
            balance = float(balance)
            if balance < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Balance must be a positive number!")
            return
        
        # Update user data
        user_data = self.bank_system.users[username]
        user_data['name'] = name
        user_data['balance'] = balance
        user_data['account_type'] = acc_type
        
        # Refresh treeview and close window
        self._populate_user_tree(tree)
        window.destroy()
        messagebox.showinfo("Success", "User updated successfully!")
    
    def _save_system_settings(self, min_balance_vars):
        """Save system settings"""
        # Update minimum balances
        for acc_type, var in min_balance_vars.items():
            try:
                min_balance = float(var.get())
                if min_balance < 0:
                    raise ValueError
                self.bank_system.account_types[acc_type]['min_balance'] = min_balance
            except ValueError:
                messagebox.showerror("Error", f"Invalid minimum balance for {acc_type}!")
                return
        
        messagebox.showinfo("Success", "System settings updated successfully!") 