from tkinter import messagebox, Toplevel, Label, Entry, Button, Frame, StringVar, OptionMenu
from tkinter import ttk

class SecurityManagement:
    def __init__(self, bank_system):
        self.bank_system = bank_system
    
    def change_pin(self):
        """Handle PIN change"""
        if not self.bank_system.current_user:
            messagebox.showerror("Error", "Please login first!")
            return
        
        # Create PIN change window
        pin_window = Toplevel(self.bank_system.root)
        pin_window.title("Change PIN")
        pin_window.geometry("300x200")
        
        # Create frame
        frame = Frame(pin_window)
        frame.pack(padx=20, pady=20)
        
        # Current PIN
        Label(frame, text="Current PIN:").grid(row=0, column=0, padx=5, pady=5)
        current_pin_entry = Entry(frame, show="*")
        current_pin_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # New PIN
        Label(frame, text="New PIN:").grid(row=1, column=0, padx=5, pady=5)
        new_pin_entry = Entry(frame, show="*")
        new_pin_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Confirm PIN
        Label(frame, text="Confirm PIN:").grid(row=2, column=0, padx=5, pady=5)
        confirm_pin_entry = Entry(frame, show="*")
        confirm_pin_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Change PIN button
        Button(frame, text="Change PIN", command=lambda: self._process_pin_change(
            current_pin_entry.get(),
            new_pin_entry.get(),
            confirm_pin_entry.get(),
            pin_window
        )).grid(row=3, column=0, columnspan=2, pady=10)
    
    def _process_pin_change(self, current_pin, new_pin, confirm_pin, window):
        """Process PIN change"""
        # Validate inputs
        if not current_pin or not new_pin or not confirm_pin:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        # Check if current PIN is correct
        user_data = self.bank_system.users[self.bank_system.current_user]
        if current_pin != user_data['pin']:
            messagebox.showerror("Error", "Current PIN is incorrect!")
            return
        
        # Check if new PIN is valid
        if not new_pin.isdigit() or len(new_pin) != 4:
            messagebox.showerror("Error", "PIN must be a 4-digit number!")
            return
        
        # Check if PINs match
        if new_pin != confirm_pin:
            messagebox.showerror("Error", "New PINs do not match!")
            return
        
        # Update PIN
        user_data['pin'] = new_pin
        
        # Show success message and close window
        messagebox.showinfo("Success", "PIN changed successfully!")
        window.destroy()
    
    def show_security_settings(self):
        """Show security settings window"""
        if not self.bank_system.current_user:
            messagebox.showerror("Error", "Please login first!")
            return
        
        # Create security settings window
        settings_window = Toplevel(self.bank_system.root)
        settings_window.title("Security Settings")
        settings_window.geometry("400x300")
        
        # Create frame
        frame = Frame(settings_window)
        frame.pack(padx=20, pady=20)
        
        # Security question
        Label(frame, text="Security Question:").grid(row=0, column=0, padx=5, pady=5)
        question_var = StringVar(value=self.bank_system.users[self.bank_system.current_user]['security_question'])
        question_menu = OptionMenu(frame, question_var, *self.bank_system.security_questions)
        question_menu.grid(row=0, column=1, padx=5, pady=5)
        
        # Security answer
        Label(frame, text="Security Answer:").grid(row=1, column=0, padx=5, pady=5)
        answer_entry = Entry(frame)
        answer_entry.insert(0, self.bank_system.users[self.bank_system.current_user]['security_answer'])
        answer_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Save button
        Button(frame, text="Save Settings", command=lambda: self._save_security_settings(
            question_var.get(),
            answer_entry.get(),
            settings_window
        )).grid(row=2, column=0, columnspan=2, pady=10)
    
    def _save_security_settings(self, question, answer, window):
        """Save security settings"""
        # Validate inputs
        if not question or not answer:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        # Update security settings
        user_data = self.bank_system.users[self.bank_system.current_user]
        user_data['security_question'] = question
        user_data['security_answer'] = answer
        
        # Show success message and close window
        messagebox.showinfo("Success", "Security settings updated successfully!")
        window.destroy()
    
    def forgot_pin(self):
        """Handle forgot PIN"""
        # Create forgot PIN window
        forgot_window = Toplevel(self.bank_system.root)
        forgot_window.title("Forgot PIN")
        forgot_window.geometry("400x200")
        
        # Create frame
        frame = Frame(forgot_window)
        frame.pack(padx=20, pady=20)
        
        # Username
        Label(frame, text="Username:").grid(row=0, column=0, padx=5, pady=5)
        username_entry = Entry(frame)
        username_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Security question (will be updated when username is entered)
        question_label = Label(frame, text="Security Question:")
        question_label.grid(row=1, column=0, padx=5, pady=5)
        
        # Security answer
        Label(frame, text="Security Answer:").grid(row=2, column=0, padx=5, pady=5)
        answer_entry = Entry(frame)
        answer_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # New PIN
        Label(frame, text="New PIN:").grid(row=3, column=0, padx=5, pady=5)
        new_pin_entry = Entry(frame, show="*")
        new_pin_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Function to update security question when username is entered
        def update_security_question(*args):
            username = username_entry.get().strip()
            if username in self.bank_system.users:
                user_data = self.bank_system.users[username]
                question_label.config(text=f"Security Question: {user_data['security_question']}")
            else:
                question_label.config(text="Security Question: User not found")
        
        # Bind username entry to update function
        username_entry.bind('<KeyRelease>', update_security_question)
        
        # Reset PIN button
        Button(frame, text="Reset PIN", command=lambda: self._process_forgot_pin(
            username_entry.get(),
            answer_entry.get(),
            new_pin_entry.get(),
            forgot_window
        )).grid(row=4, column=0, columnspan=2, pady=10)
    
    def _process_forgot_pin(self, username, answer, new_pin, window):
        """Process forgot PIN"""
        # Validate inputs
        if not username or not answer or not new_pin:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        # Check if user exists
        if username not in self.bank_system.users:
            messagebox.showerror("Error", "User not found!")
            return
        
        # Check if security answer is correct
        user_data = self.bank_system.users[username]
        if answer.lower() != user_data['security_answer'].lower():
            messagebox.showerror("Error", "Incorrect security answer!")
            return
        
        # Check if new PIN is valid
        if not new_pin.isdigit() or len(new_pin) != 4:
            messagebox.showerror("Error", "PIN must be a 4-digit number!")
            return
        
        # Update PIN
        user_data['pin'] = new_pin
        
        # Reset login attempts
        if username in self.bank_system.login_attempts:
            self.bank_system.login_attempts[username] = 0
        
        # Show success message and close window
        messagebox.showinfo("Success", "PIN reset successfully!")
        window.destroy() 