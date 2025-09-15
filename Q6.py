import random

# Available moves
moves = ["rock", "paper", "scissors"]

print("Welcome to Rock-Paper-Scissors!")
rounds = int(input("How many rounds do you want to play? "))

user_score = 0
computer_score = 0

for r in range(1, rounds + 1):
    print(f"\n--- Round {r} ---")
    user_move = input("Enter your move (rock/paper/scissors): ").lower()
    
    if user_move not in moves:
        print("Invalid move! Try again.")
        continue
    
    computer_move = random.choice(moves)
    print(f"Computer chose: {computer_move}")
    
    if user_move == computer_move:
        print("It's a draw!")
    elif (user_move == "rock" and computer_move == "scissors") or \
         (user_move == "paper" and computer_move == "rock") or \
         (user_move == "scissors" and computer_move == "paper"):
        print("✅ You win this round!")
        user_score += 1
    else:
        print("❌ Computer wins this round!")
        computer_score += 1

# Final Result
print("\n=== Final Score ===")
print(f"You: {user_score} | Computer: {computer_score}")

if user_score > computer_score:
    print("Congratulations! You are the overall winner!")
elif user_score < computer_score:
    print("Computer wins the game! Better luck next time.")
else:
    print("It's an overall draw!")
