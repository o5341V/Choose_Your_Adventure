import random

def start_adventure():
    print("You are in a dark forest. Two paths lie before you.")
    choice = input("Do you go left or right? (left/right): ")

    if choice == "left":
        encounter_wolf()
    elif choice == "right":
        find_cottage()

def encounter_wolf():
    health = 3  # Player starts with 3 HP
    while health > 0:
        print(f"A wolf appears! You have {health} HP left.")
        choice = input("Do you fight or flee? (fight/flee): ")

        if choice == "fight":
            num = random.randint(1, 2)
            myChoice = int(input("Enter a number between 1-2: "))
            if num == myChoice:
                print(f"{num}, You have slain the wolf")
                return  # Player wins, exit the function
            else:
                print(f"{num}, Wolf dodges your attack")
                health -= 1  # Reduce health if the attack fails
        elif choice == "flee":
            print("You run back to the start.")
            return  # Player flees, exit the function

        if health == 0:
            print("You have no health left and succumb to your injuries.")

def find_cottage():
    print("You find a small cottage. Do you enter or continue walking?")
    choice = input("Choose your action (enter/continue): ")

    if choice == "enter":
        print("You find a treasure chest!")
    elif choice == "continue":
        print("You continue walking and eventually leave the forest.")

start_adventure()  # Call the function only once to start the adventure
