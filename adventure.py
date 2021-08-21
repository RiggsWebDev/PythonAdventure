answer = input("Would you like to play? (Yes/No)")

if answer.lower().strip() == "yes":

    answer = input("You reach a crossroads, would you like to go left or right? (left/right)").lower().strip()
    if answer == "left":
        answer = input("You see a huge dragon, as a lowly adventurer would you choose to attack or run?")

        if answer == "attack":
            print("You obviously died, you should really work on your ability to infer information...")
        
        if answer == "run":
            print("Good choice! The dragon was much faster and you've now died!")
    if answer == "right":
        print("You walk around aimlessly in a forest eventually falling into a snake pit and dying!")

else:
    print("Goodbye!")
