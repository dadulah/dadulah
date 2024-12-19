import random
# Rock Paper Scissors game 
options = ("rock", "paper", "scissors")
wins = 0 
loses = 0
ties = 0
playing = True

while playing:

  player = None
  computer = random.choice(options)

  while player not in options:
    player = input("Enter a choice (rock, paper, scissors): ")

  print(f"Player: {player}")
  print(f"computer: {computer}")

  if player == computer:
    print("It's a tie!")
    ties += 1
  elif player == "rock" and computer == "scissors":
    print("It's win!")
    wins += 1
  elif player == "paper" and computer == "rock":
    print("It's win!")
    wins += 1
  elif player == "scissors" and computer == "paper":
    print("It's win!")
    wins += 1
  else:
    print("You lose!")
    loses += 1

  if not input("Play again? (y/n): ").lower() == "y":
    playing = False

print(f"Wins: {wins}, Loses: {loses}, Ties: {ties}")
print("Thank's for playing.")