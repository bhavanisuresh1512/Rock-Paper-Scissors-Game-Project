import random

choices = ["rock", "paper", "scissors"]

while True:
    user = input("\nEnter rock, paper, or scissors (or 'q' to quit): ").lower()
    
    if user == 'q':
        print("Thanks for playing!")
        break
    
    if user not in choices:
        print("Invalid choice!")
        continue
    
    computer = random.choice(choices)
    
    print(f"You: {user}")
    print(f"Computer: {computer}")
    
    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
