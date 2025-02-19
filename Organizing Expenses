for expense in expenses_list:
                type_of_category = expense['Category']
                if type_of_category not in organized_expenses:
                    organized_expenses[type_of_category] = []
                organized_expenses[type_of_category].append(expense)

            for type_of_category, expenses in organized_expenses.items():
                print(f"Category: {type_of_category}")
                for expense in expenses:
                    print(f"Amount: {expense['Amount']}$, Date: {expense['Date']}")
