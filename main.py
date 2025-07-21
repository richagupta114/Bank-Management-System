from tkinter import *
from bank_system import BankSystem

def main():
    # Create a Tk object
    root = Tk()

    # Create an instance of the BankSystem class
    bank_system = BankSystem(root)

    # Start the mainloop
    root.mainloop()

if __name__ == '__main__':
    main() 