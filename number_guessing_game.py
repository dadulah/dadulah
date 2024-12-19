#python number guessing game
lowest = 1
heighest = 1000
answer = random.randint(lowest, heighest)
guesses = 0
is_running = True

print("Python number guessing game")
print(f"Select a number between {lowest} and {heighest}")

while is_running:
    guess = input("Enter your guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < lowest or guess > heighest:
            print("That number is out of range!")
            print(f"Select a number between {lowest} and {heighest}")            
        elif guess < answer:
             print("Too low! Try again.")
        elif guess > answer:           
             print("Too high! Try again.")
        else:
             print(f"CORRECT! the answer was {answer}")
             print(f"Number of gusses {guesses}")
             is_running = False
    else:
         print("Invalid guess!")
         print(f"Select a number between {lowest} and {heighest}")