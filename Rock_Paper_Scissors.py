import random

# this ver of Rock Paper scissors is based on the legend of zelda
print('''Bow beats Bomb (detonates it from afar). 
Bomb beats Sword (explosion damages the sword). 
Sword beats Bow (closes the gap for a strike).''')
print()  
# Added some spacing for readability

# Main game loop
while True:
    # User choice
    user_choice = input("Enter your choice (bow, sword, bomb): ").lower()
    if user_choice not in ["bow", "sword", "bomb"]:
        print("Invalid choice! Please enter 'bow', 'sword', or 'bomb'.")
        continue  # Prompt the user again if input is invalid

    # CPU choice
    cpu_choice = random.choice(["bow", "sword", "bomb"])

    # Game logic
    if user_choice == cpu_choice:
        print("The CPU also picked {cpu_choice}.")
        print("It's a tie! :O")
    elif user_choice == "bow":
        if cpu_choice == "bomb":
            print("The CPU picked bomb.")
            print("YOU WIN!")
        else:
            print("The CPU picked sword.")
            print("YOU LOSE!")
    elif user_choice == "sword":
        if cpu_choice == "bow":
            print("The CPU picked bow.")
            print("YOU WIN!")
        else:
            print("The CPU picked bomb.")
            print("YOU LOSE!")
    elif user_choice == "bomb":
        if cpu_choice == "sword":
            print("The CPU picked sword.")
            print("YOU WIN!")   
        else:
            print("The CPU picked bow.")
            print("YOU LOSE!")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break 
