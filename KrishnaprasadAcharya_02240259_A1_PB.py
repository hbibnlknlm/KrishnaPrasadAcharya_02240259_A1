import random

# Function for Guess the Number Game
def guess_number_game():
    print("Welcome to the Guess the Number game!")
    number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0
    while True:
        try:
            user_guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Function for Rock Paper Scissors Game
def rock_paper_scissors_game():
    print("Welcome to Rock Paper Scissors game!")
    options = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice not in options:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

# Main menu for selecting a game
def main():
    while True:
        print("\nSelect a function (1-3):")
        print("1. Guess Number game")
        print("2. Rock Paper Scissors game")
        print("3. Exit program")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                guess_number_game()
            elif choice == 2:
                rock_paper_scissors_game()
            elif choice == 3:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
