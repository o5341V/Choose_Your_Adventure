import random

def start_adventure():
    print("You are in a dark forest. Two paths lie before you.")
    choice = input("Do you go left or right? (left/right): ")

    if choice == "left":
        encounter_wolf()
    elif choice == "right":
        find_cottage()

def encounter_wolf():
    print("A wolf appears! Do you fight or flee?")
    choice = input("Choose your action (fight/flee): ")

    if choice == "fight":
        print("You attack.")
    elif choice == "flee":
        print("You run back to the start.")
        
    num = random.randint(1, 2)  # Generate a random number each time
    myChoice = int(input("Enter a number Between 1-2: "))  # Convert input to integer
    if num == myChoice:
        print(f"{num}, You have slain the wolf")
    else: 
        print(f"{num}, Wolf dodges your attack")

def find_cottage():
    print("You find a small cottage. Do you enter or continue walking?")
    choice = input("Choose your action (enter/continue): ")

    if choice == "enter":
        print("You find a treasure chest!")
    elif choice == "continue":
        print("You continue walking and eventually leave the forest.")

start_adventure()  # Call the function only once to start the adventure
