# Python slote machine program
import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    return [random.choice(symbols) for _ in range(3)]
    
def print_row(row):
    print(" | ".join(row))
    
def get_payout(bet, row):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 2
        elif row[0] == "🍉":
            return bet * 3
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    return 0
    
def main():
    balance = 100
    
    print("*************************")
    print("Welcome to python slots")
    print("Symbols: ⭐🔔🍋🍉🍒")
    print("*************************")
    print()
    
    while balance > 0:
     print("*************************")
     print(f"Current balance: ${balance}")
        
     bet = input("Place your bet amount: ")
     
     if not bet.isdigit():
         print("Pleas enter a valid number!")
         continue
     
     bet = int(bet)
     
     if bet > balance:
         print("Insufficient founds!")
         continue
     
     if bet <= 0:
         print("Bet must be grater then 0!")
         continue
     
     balance -= bet
     row = spin_row()
     print("Spinning\n")
     print_row(row)
     
     payout = get_payout(bet, row)
     
     if payout > 0:
         print(f"You won ${payout}")
     else:
         print("Sorry you lost this round!")
         
     balance += payout
     
     print("*************************")
     play_agian = input("Play agian (y/n): ")
     if not play_agian == "y":
       break
       
    print(f"Game over: Your fainal balnce is {balance}!")       
       
if __name__ == "__main__":
    main()