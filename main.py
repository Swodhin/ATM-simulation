balance = 15000

print("-- Welcome to easy bank atm --")

while True:
    text = """
What do you want to do?
1. Check Balance
2. Deposit Amount
3. Withdraw Amount
4. Exit
---------------------
"""
    choice = int(input(text))

    if choice == 1:
        print(f"Your balance is {balance} ")

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"Successfully deposited!")
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        if balance >= amount:
            balance -= amount
            print(f"Successfully withdrawn")
        else:
            print("Insufficient Balance")
    elif choice == 4:
        print("-- Thank you --")
        break
    else:
        print("Try again")
