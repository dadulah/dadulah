# Python banking program
def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to deposite: "))
    
    if amount < 0:
        print("the amont can not be less than 0!")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter an amount to be withdrawn: "))
    
    if amount > balance:        
         print("The amont can not be grater than your balance!")
         print(f"Your balance is ${balance:.2f}")
         return 0
    elif amount < 0:
        print("the amont can not be less than 0!")
        return 0
    else:
        return amount
def main():
    balance = 0
    is_running = True
    print("___________________")
    print()
    print("  Banking program")
    print("___________________")
    
    while is_running:
        print()
        print("_____ OPTIONS _____")
        print("1.Showe balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        
        choice = input("Enter a choice (1-4): ")
        
        print("___________________")
        print()
        
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
            print("Thanks for chosing us `°-°`")
        else:
            print(f"{choice} is not valid choice!")
        print("___________________")
        

if __name__ == "__main__":
    main()