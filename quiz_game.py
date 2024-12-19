#quiz game
questions = ("Which company was the elon musk startup?:", 
"How many elements are in the periodic table?: ",
"Which animal lays the largest egg?: ",
"What is the most abundant gas in Earth's atmosphere?: ", 
                         "How many bones are in the human body?: ",
                          "Which planet in the solar system is the hottest?: ")

options = (("A. Tesla", "B. zip2", "C. space-x", "D. OpenAi"), 
("A. 116", "B. 117", "C. 118", "D. 118"),
("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"), 
("A. 206", "B. 207", "C. 208", "D. 209"), 
("A. Mercury", "B. Venus", "C. earth", "D. Mars"))

answers = ("B", "C", "D", "A", "A", "B")
guesses = []
score = 0
questions_num = 0

for question in questions:
    print("---------------------------------------------------")
    print(question)
    for option in options[questions_num]:
        print(option)
    
    guess = input("Enter (A, B, C, D) Q to quite: ").upper()
    guesses.append(guess)
    if guess == answers[questions_num]:
        print("Corect!")
        score += 1
    elif guess == "Q":
        break
    else:
         print("Uncorect answer!")
         print(f"{answers[questions_num]} is the corect answer!")
        
    questions_num += 1

print("----------------------------------")
print("            Result              ")
print("----------------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

print(f"You got {score} scors out of {len(guesses)} guesses")

score = int(score / len(questions) * 100)
print(f"Your score is {score}%")