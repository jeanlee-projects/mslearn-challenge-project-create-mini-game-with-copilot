import random

VALID_CHOICES = ["rock", "paper", "scissors"]
QUIT_CHOICES = ["quit", "q"]


def get_player_choice():
    while True:
        choice = input("Choose rock, paper, scissors, or quit: ").strip().lower()
        if choice in VALID_CHOICES:
            return choice
        if choice in QUIT_CHOICES:
            return None
        print("Invalid option. Please enter rock, paper, scissors, or quit.")


def get_computer_choice():
    return random.choice(VALID_CHOICES)


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"

    wins_against = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }

    if wins_against[player_choice] == computer_choice:
        return "win"
    return "lose"


def play_round():
    player_choice = get_player_choice()
    if player_choice is None:
        print("\nYou chose to quit the game.")
        return "quit"

    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)

    print(f"\nYou chose {player_choice}. Computer chose {computer_choice}.")
    if result == "tie":
        print("It's a tie!")
    elif result == "win":
        print("You won this round!")
    else:
        print("You lost this round.")

    return result


def ask_play_again():
    while True:
        answer = input("Do you want to play again? (yes/no or quit): ").strip().lower()
        if answer in ["yes", "y"]:
            return True
        if answer in ["no", "n"] or answer in QUIT_CHOICES:
            return False
        print("Please answer yes, no, or quit.")


def main():
    print("Welcome to Rock, Paper, Scissors!")

    score = {
        "wins": 0,
        "losses": 0,
        "ties": 0,
    }

    while True:
        result = play_round()
        if result == "quit":
            break

        if result == "win":
            score["wins"] += 1
        elif result == "lose":
            score["losses"] += 1
        else:
            score["ties"] += 1

        if not ask_play_again():
            break

    print("\nFinal score:")
    print(f"Wins: {score['wins']}")
    print(f"Losses: {score['losses']}")
    print(f"Ties: {score['ties']}")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
