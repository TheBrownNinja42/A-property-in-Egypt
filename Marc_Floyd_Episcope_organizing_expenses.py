for expense in expenses_list:
  organized_expenses.clear()
                
  type_of_category = expense['Category']              
  if type_of_category not in organized_expenses:          
    organized_expenses[type_of_category] = []           
    organized_expenses[type_of_category].append(expense)

            
    for category, expenses in organized_expenses.items():
      print(f"Category: {type_of_category}")    
      for expense in expenses:      
        print(f"Amount: {expense['Amount']}$, Date: {expense['Date']}")
