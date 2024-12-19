# concession stand program
menu = {"pizza": 3.00,
                "nachos": 4.50,
                "popcorn": 6.00,
                "fries": 2.50,
                "chips": 1.00,
                "pretzel": 3.50,
                "soda": 3.00,
                "lemonade": 4.25}
                
cart = []
total = 0

print("------- MENU ---------")
for key, value in menu.items():
    print(f" {key:10}: {value:.2f}")
   
print("-----------------------")

while True:
    food = input("Enter a food to buy (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    elif menu.get(food) is None:
        print(f"We don't have {food}")
        
print("-------- Your order --------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Your total is ${total:.2f}") 



