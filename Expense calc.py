#Expense calculator or something idk

def create_categories():
    # Create a list to store expense categories
    categories = []

    while True:
        # Ask the user to input a category or type 'done' to finish
        category = input("Enter a category for expenses (or type 'done' to finish): ").strip().lower()
        if category == 'done':
            break  # Exit the loop if the user is done adding categories
        if category in categories:
            print("Category already exists. Please enter a new category.")  # Prevent duplicate categories
        else:
            categories.append(category)  # Add the new category to the list

    return categories  # Return the list of categories

def add_expenses(categories):
    # Create a dictionary to store expenses for each category
    expenses = {category: 0 for category in categories}
    for category in categories:
        while True:
            try:
                # Ask the user to input the total expense for the current category
                expense = float(input(f"Enter the total expense for '{category}': $"))
                expenses[category] += expense  # Add the expense to the category total
                break  # Exit the loop if the input is valid
            except ValueError:
                # Handle invalid input (e.g., if the user enters text instead of a number)
                print("Invalid input. Please enter a number.")
    return expenses

def display_summary(expenses):
    # Display a summary of all expenses
    print("\n--- Expense Summary ---")
    total = 0

    # Initialize a variable to store the total expenses
    for category, amount in expenses.items():
       
    # Add the category total to the overall total
        print(f"{category.capitalize()}: ${amount:.2f}")
        total += amount
    

    # Print the total expenses across all categories
    print(f"Total Expenses: ${total:.2f}")




def main():
    # Main function to run the program
    print("Welcome to the your Expense Calculator BOSS!")

    # Step 1: Create categories
    categories = create_categories()

    if not categories:
        # If no categories were added, exit the program
        print("No categories were added. im leaving...")
        return

    # Step 2: Add expenses for each category
    expenses = add_expenses(categories)

    # Step 3: Display the expense summary
    display_summary(expenses)

# Run the program if this script is executed directly
if __name__ == "__main__":
    main()