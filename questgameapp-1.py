import random

# Introduction to the game
def intro():
    print("Welcome to CodeQuest: Python Adventures!")
    print("You are a Code Wizard on a journey to regain your coding powers.")
    print("Each level will present a challenge to test your Python skills.")
    print("Let's begin the adventure!\n")

# Level 1 - Basic Variables and Arithmetic
def level_1():
    print("Level 1: The Basics\n")
    print("Task: Solve the following problem using Python to move forward.")
    print("You need to create a variable called 'magic_number' and set it to 42.")
    print("Then, multiply it by 2 and add 10 to it.\n")

    answer = input("What is the final result? ")

    try:
        if int(answer) == 42 * 2 + 10:
            print("Correct! You've unlocked the next level.\n")
            return True
        else:
            print("Oops! That's not correct. Try again.")
            return False
    except ValueError:
        print("Please enter a number.")
        return False

# Level 2 - If-else Statements
def level_2():
    print("Level 2: Decision Forest\n")
    print("Task: A monster is blocking your path!")
    print("If your magic number is greater than 50, you can scare the monster away.\n")

    magic_number = random.randint(30, 60)
    print(f"Your magic number is: {magic_number}")
    
    if magic_number > 50:
        print("You scared the monster away with your powerful code magic!")
        return True
    else:
        print("Your magic number wasn't strong enough! Try again.")
        return False

# Level 3 - Loops
def level_3():
    print("Level 3: Looping Canyon\n")
    print("Task: Cross the canyon by repeating the magic spell 3 times using a loop.\n")
    
    spell = input("Enter the magic spell to repeat: ")

    for i in range(3):
        print(f"Repeating spell: {spell} ({i+1}/3)")

    print("You successfully crossed the canyon!")
    return True

# Main game loop
def start_game():
    intro()
    
    while not level_1():
        pass

    while not level_2():
        pass

    while not level_3():
        pass

    print("Congratulations! You've completed the Python adventure and regained your coding powers.")

# Start the game
if __name__ == "__main__":
    start_game()
