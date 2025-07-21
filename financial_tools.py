from tkinter import messagebox, Toplevel, Label, Entry, Button, Frame, ttk
from tkinter import StringVar
import math

class FinancialTools:
    def __init__(self, bank_system):
        self.bank_system = bank_system
    
    def show_financial_tools(self):
        """Show financial tools window"""
        # Create financial tools window
        tools_window = Toplevel(self.bank_system.root)
        tools_window.title("Financial Tools")
        tools_window.geometry("800x600")
        
        # Create notebook for tabs
        notebook = ttk.Notebook(tools_window)
        notebook.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Loan Calculator tab
        loan_frame = Frame(notebook)
        notebook.add(loan_frame, text="Loan Calculator")
        self._create_loan_calculator_tab(loan_frame)
        
        # EMI Calculator tab
        emi_frame = Frame(notebook)
        notebook.add(emi_frame, text="EMI Calculator")
        self._create_emi_calculator_tab(emi_frame)
        
        # Interest Calculator tab
        interest_frame = Frame(notebook)
        notebook.add(interest_frame, text="Interest Calculator")
        self._create_interest_calculator_tab(interest_frame)
    
    def _create_loan_calculator_tab(self, parent):
        """Create loan calculator tab"""
        # Create frame
        frame = Frame(parent)
        frame.pack(padx=20, pady=20)
        
        # Loan amount
        Label(frame, text="Loan Amount:").grid(row=0, column=0, padx=5, pady=5)
        loan_amount_entry = Entry(frame)
        loan_amount_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Interest rate
        Label(frame, text="Annual Interest Rate (%):").grid(row=1, column=0, padx=5, pady=5)
        interest_rate_entry = Entry(frame)
        interest_rate_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Loan term
        Label(frame, text="Loan Term (years):").grid(row=2, column=0, padx=5, pady=5)
        loan_term_entry = Entry(frame)
        loan_term_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Calculate button
        Button(frame, text="Calculate", command=lambda: self._calculate_loan(
            loan_amount_entry.get(),
            interest_rate_entry.get(),
            loan_term_entry.get(),
            result_label
        )).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Result label
        result_label = Label(frame, text="", wraplength=300)
        result_label.grid(row=4, column=0, columnspan=2, pady=10)
    
    def _create_emi_calculator_tab(self, parent):
        """Create EMI calculator tab"""
        # Create frame
        frame = Frame(parent)
        frame.pack(padx=20, pady=20)
        
        # Loan amount
        Label(frame, text="Loan Amount:").grid(row=0, column=0, padx=5, pady=5)
        loan_amount_entry = Entry(frame)
        loan_amount_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Interest rate
        Label(frame, text="Annual Interest Rate (%):").grid(row=1, column=0, padx=5, pady=5)
        interest_rate_entry = Entry(frame)
        interest_rate_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Loan term
        Label(frame, text="Loan Term (months):").grid(row=2, column=0, padx=5, pady=5)
        loan_term_entry = Entry(frame)
        loan_term_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Calculate button
        Button(frame, text="Calculate", command=lambda: self._calculate_emi(
            loan_amount_entry.get(),
            interest_rate_entry.get(),
            loan_term_entry.get(),
            result_label
        )).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Result label
        result_label = Label(frame, text="", wraplength=300)
        result_label.grid(row=4, column=0, columnspan=2, pady=10)
    
    def _create_interest_calculator_tab(self, parent):
        """Create interest calculator tab"""
        # Create frame
        frame = Frame(parent)
        frame.pack(padx=20, pady=20)
        
        # Principal amount
        Label(frame, text="Principal Amount:").grid(row=0, column=0, padx=5, pady=5)
        principal_entry = Entry(frame)
        principal_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Interest rate
        Label(frame, text="Annual Interest Rate (%):").grid(row=1, column=0, padx=5, pady=5)
        interest_rate_entry = Entry(frame)
        interest_rate_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Time period
        Label(frame, text="Time Period (years):").grid(row=2, column=0, padx=5, pady=5)
        time_entry = Entry(frame)
        time_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Calculate button
        Button(frame, text="Calculate", command=lambda: self._calculate_interest(
            principal_entry.get(),
            interest_rate_entry.get(),
            time_entry.get(),
            result_label
        )).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Result label
        result_label = Label(frame, text="", wraplength=300)
        result_label.grid(row=4, column=0, columnspan=2, pady=10)
    
    def _calculate_loan(self, amount, rate, term, result_label):
        """Calculate loan details"""
        try:
            # Convert inputs to float
            amount = float(amount)
            rate = float(rate) / 100
            term = float(term)
            
            # Calculate monthly payment
            monthly_rate = rate / 12
            num_payments = term * 12
            monthly_payment = (amount * monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)
            
            # Calculate total payment and interest
            total_payment = monthly_payment * num_payments
            total_interest = total_payment - amount
            
            # Display results
            result_text = f"Monthly Payment: ${monthly_payment:.2f}\n"
            result_text += f"Total Payment: ${total_payment:.2f}\n"
            result_text += f"Total Interest: ${total_interest:.2f}"
            result_label.config(text=result_text)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")
    
    def _calculate_emi(self, amount, rate, term, result_label):
        """Calculate EMI details"""
        try:
            # Convert inputs to float
            amount = float(amount)
            rate = float(rate) / 100
            term = float(term)
            
            # Calculate monthly interest rate
            monthly_rate = rate / 12
            
            # Calculate EMI
            emi = (amount * monthly_rate * (1 + monthly_rate)**term) / ((1 + monthly_rate)**term - 1)
            
            # Calculate total payment and interest
            total_payment = emi * term
            total_interest = total_payment - amount
            
            # Display results
            result_text = f"EMI: ${emi:.2f}\n"
            result_text += f"Total Payment: ${total_payment:.2f}\n"
            result_text += f"Total Interest: ${total_interest:.2f}"
            result_label.config(text=result_text)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")
    
    def _calculate_interest(self, principal, rate, time, result_label):
        """Calculate interest details"""
        try:
            # Convert inputs to float
            principal = float(principal)
            rate = float(rate) / 100
            time = float(time)
            
            # Calculate simple interest
            simple_interest = principal * rate * time
            
            # Calculate compound interest (annually)
            compound_interest = principal * (1 + rate)**time - principal
            
            # Display results
            result_text = f"Simple Interest: ${simple_interest:.2f}\n"
            result_text += f"Compound Interest: ${compound_interest:.2f}\n"
            result_text += f"Total Amount (Simple): ${principal + simple_interest:.2f}\n"
            result_text += f"Total Amount (Compound): ${principal + compound_interest:.2f}"
            result_label.config(text=result_text)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!") 