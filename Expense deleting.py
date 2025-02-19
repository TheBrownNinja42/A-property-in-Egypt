# 

# Initialize an empty list to store expenses
expenses = []

# Function to display the main menu
def display_menu():
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")

# Function to add an expense
def add_expense():
    # Ask the user for the expense details
    description = input("Enter the expense description: ")
    amount = float(input("Enter the expense amount: "))
    
    # Create a dictionary to store the expense details
    expense = {
        "description": description,
        "amount": amount
    }
    
    # Add the expense to the list
    expenses.append(expense)
    print(f"Expense '{description}' of ${amount:.2f} added successfully!")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses to display.")
    else:
        print("\nList of Expenses:")
        for index, expense in enumerate(expenses, start=1):
            print(f"{index}. {expense['description']} - ${expense['amount']:.2f}")

# Function to delete an expense
def delete_expense():
    view_expenses()  # Show the list of expenses first
    if expenses:
        try:
            # Ask the user which expense to delete
            expense_num = int(input("Enter the number of the expense to delete: "))
            if 1 <= expense_num <= len(expenses):
                # Remove the selected expense
                deleted_expense = expenses.pop(expense_num - 1)
                print(f"Expense '{deleted_expense['description']}' deleted successfully!")
            else:
                print("Invalid expense number.")
        except ValueError:
            print("Please enter a valid number.")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        print("Exiting the Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-4).")