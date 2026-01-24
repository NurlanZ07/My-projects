transactions = []

while True:
    print("\n1 Add transaction")
    print("2 Show all transactions")
    print("3 Show summary")
    print("4 Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        line = input("Enter transaction: ").strip()
        parts = line.split()

        t_type = parts[0]
        amount = float(parts[1])
        category = parts[2]

        record = [t_type, amount, category]
        transactions.append(record)

    elif choice == 2:
        for t in transactions:
            print(t)

    elif choice == 3:
        total_income = 0.0
        total_expense = 0.0

        for t in transactions:
            if t[0] == "income":
                total_income += t[1]
            else:
                total_expense += t[1]

        balance = total_income - total_expense

        print("Income:", total_income)
        print("Expense:", total_expense)
        print("Balance:", balance)

    elif choice == 4:
        break

    else:
        print("Invalid choice")
