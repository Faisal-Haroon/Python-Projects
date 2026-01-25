import random

CHOICES = ("rock", "paper", "scissors")

def decide_winner(player, computer):
    if player == computer:
        return "draw"
    wins_against = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }
    return "player" if wins_against[player] == computer else "computer"

def prompt_choice():
    while True:
        choice = input("Choose rock, paper, or scissors (or q to quit): ").strip().lower()
        if choice in CHOICES or choice in ("q", "quit", "exit"):
            return choice
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def main():
    print("=== Rock, Paper, Scissors ===")
    print("Type 'q' to quit.\n")

    score = {"player": 0, "computer": 0, "draw": 0}
    rounds = 0

    while True:
        player = prompt_choice()
        if player in ("q", "quit", "exit"):
            break

        computer = random.choice(CHOICES)
        result = decide_winner(player, computer)
        score[result] += 1
        rounds += 1

        print(f"You chose: {player}")
        print(f"Computer chose: {computer}")

        if result == "draw":
            print("Result: It's a draw.")
        elif result == "player":
            print("Result: You win!")
        else:
            print("Result: Computer wins.")

        print(f"Score — You: {score['player']}, Computer: {score['computer']}, Draws: {score['draw']}\n")

    print("\n=== Game Over ===")
    print(f"Total rounds: {rounds}")
    print(f"Final Score — You: {score['player']}, Computer: {score['computer']}, Draws: {score['draw']}")
    if score["player"] > score["computer"]:
        print("Overall: You won! 🎉")
    elif score["player"] < score["computer"]:
        print("Overall: Computer won. 🤖")
    else:
        print("Overall: It's a tie!")

if __name__ == "__main__":
    main()
