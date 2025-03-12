import random

def intro():
    """Ask for the player's name and explain the game rules."""
    name = input("Enter your name: ")
    print(f"Well {name}, you need to select a number between 1 and 200")
    return name

def runner():
    """Main game loop where the player guesses the number."""
    computer_number = random.randint(1, 200)  # Generate a new random number
    loop_time = 0

    while loop_time < 6:
        try:
            player_num = int(input("Enter your guess: "))  # Get user's guess

            if player_num < 1 or player_num > 200:
                print(f"{player_num} is out of the allowed range (1-200). Try again!")
                continue  # Skip to the next iteration
            
            loop_time += 1  # Count valid attempts

            if player_num < computer_number:
                print(f"{player_num} is too low!")
            elif player_num > computer_number:
                print(f"{player_num} is too high!")
            else:
                print(f"🎉 Congratulations! {player_num} == {computer_number} You WON!")
                return True  # Player won
            
            print(f"Try again! Attempts left: {6 - loop_time}")

        except ValueError:
            print("Invalid input! Please enter a number.")

    print(f"Game over! The correct number was {computer_number}")
    return False  # Player lost

def control_game():
    """Controls the game flow and allows replay."""
    name = intro()  # Get player name
    
    while True:  # Loop for replaying
        print("\nStarting a new game...")
        runner()  # Run the game

        # Ask if the player wants to play again
        user_want = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if user_want not in ["yes", "y"]:
            print(f"Thanks for playing, {name}! Goodbye!")
            break  # Exit the loop if the player says no

control_game()  # Start the game
