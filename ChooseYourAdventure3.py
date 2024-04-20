import random

def start_adventure():
    xp = 0  # Initialize experience points
    print("You are in a dark forest. Two paths lie before you.")
    choice = input("Do you go left or right? (left/right): ")

    if choice == "left":
        xp += encounter_wolf()  # Add XP gained from the encounter
    elif choice == "right":
        xp += find_cottage()  # Add XP gained from the encounter, if any

    print(f"Adventure ends. You earned {xp} XP.")  # Display total XP earned

def encounter_wolf():
    health = 3
    xp_gain = 0  # XP gained from this encounter

    while health > 0:
        print(f"A wolf appears! You have {health} HP left.")
        choice = input("Do you fight or flee? (fight/flee): ")

        if choice == "fight":
            num = random.randint(1, 2)
            myChoice = int(input("Enter a number between 1-2: "))
            if num == myChoice:
                print(f"{num}, You have slain the wolf.")
                xp_gain = 50  # Set XP gain for defeating the wolf
                break  # Exit the loop after defeating the wolf
            else:
                print(f"{num}, Wolf dodges your attack.")
                health -= 1
        elif choice == "flee":
            print("You run back to the start.")
            break

        if health == 0:
            print("You have no health left and succumb to your injuries.")

    return xp_gain  # Return the XP gained from this encounter

def find_cottage():
    print("You find a small cottage. Do you enter or continue walking?")
    choice = input("Choose your action (enter/continue): ")

    if choice == "enter":
        print("You find a treasure chest! Inside is a magical amulet worth 30 XP.")
        return 30  # XP gain for finding the treasure
    elif choice == "continue":
        print("You continue walking and eventually leave the forest.")
        return 0  # No XP gain

    return 0  # Default return if no XP actions are taken

start_adventure()  # Start the adventure
