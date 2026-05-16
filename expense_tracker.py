# Expense Tracker Project

expenses = []

# Function to add expense
def add_expense():
    category = input("Enter category: ")
    
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    date = input("Enter date (DD-MM-YYYY): ")

    expense = {
        "category": category,
        "amount": amount,
        "date": date
    }

    expenses.append(expense)
    print("Expense added successfully!")

# Function to view expenses
def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
    else:
        print("\nAll Expenses:")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. Category: {expense['category']}, Amount: {expense['amount']}, Date: {expense['date']}")

# Function to calculate total expense
def calculate_total():
    total = 0

    for expense in expenses:
        total += expense['amount']

    print(f"Total Expense: {total}")

# Function to show category summary
def category_summary():
    summary = {}

    for expense in expenses:
        category = expense['category']

        if category in summary:
            summary[category] += expense['amount']
        else:
            summary[category] = expense['amount']

    print("\nCategory Summary:")

    for category, amount in summary.items():
        print(f"{category}: {amount}")

# Function to delete expense
def delete_expense():
    view_expenses()

    if len(expenses) == 0:
        return

    try:
        index = int(input("Enter expense number to delete: "))
        
        if 1 <= index <= len(expenses):
            removed = expenses.pop(index - 1)
            print("Deleted:", removed)
        else:
            print("Invalid index!")

    except ValueError:
        print("Please enter valid number.")

# Main menu loop
while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Category Summary")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_expense()

    elif choice == '2':
        view_expenses()

    elif choice == '3':
        calculate_total()

    elif choice == '4':
        category_summary()

    elif choice == '5':
        delete_expense()

    elif choice == '6':
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")