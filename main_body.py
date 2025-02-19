expenses_list = []
organized_expenses = {}

def add_expenses(category, amount, date):

def remove_expenses():
    

def price_check(x):
    try:
        price = float(x)
        return True
    except ValueError:
        return False
    


def expense_tracker():
    while True:
        print("Welcome to our expense tracker! What would you like to do today (please input a number)?")
        print("1. View all expenses")
        print("2. Add an expense")
        print("3. Delete an expense")
        print("4. Caluculate expenses")
        choice = input()

        if choice == "1":
            for expense in expenses_list:
                type_of_category = expense['Category']
                if type_of_category not in organized_expenses:
                    organized_expenses[type_of_category] = []
                organized_expenses[type_of_category].append(expense)

            for type_of_category, expenses in organized_expenses.items():
                print(f"Category: {type_of_category}")
                for expense in expenses:
                    print(f"Amount: {expense['Amount']}$, Date: {expense['Date']}")
            

        elif choice == "2":
        
            
        elif choice == "3":
            remove_expenses()

        elif choice == "4":

        else:
          print("Input valid number")

expense_tracker()
