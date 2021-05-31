import random
Cwins=0
Pwins=0
while True:

    Playerchoice = input("choose one from rock, paper, scissors: ")
    options = ["r", "p", "s"]
    Caction = random.choice(options)
    print(f"\nYou chose {Playerchoice}, computer chose {Caction}.\n")

    if Playerchoice == Caction:
        print(f"Both  selected {Playerchoice}. It's a tie!")
    elif Playerchoice == "r":
        if Caction == "s":
            print("Rock powerful than scissors! You win!")
            Pwins+=1
        else:
            print("Paper covers  rock! You lose.")
            Cwins+=1
    elif Playerchoice == "p":
        if Caction == "r":
            print("Paper powerful than rock! You win!")
            Pwins+=1
        else:
            print("Scissors less powerful than paper! You lose.")
            Cwins+=1
    elif Playerchoice== "s":
        if Caction == "p":
            print("Scissors powerful than paper! You win!")
            Pwins+=1
        else:
            print("Rock less powerful than scissors! You lose.")
            Cwins+=1
    print("Player wins: "+str(Pwins))
    print("Computer wins: " + str(Cwins))
    play_again = input("Play again? (yes/no):\n ")
    if play_again in ["y","Y"]:
        pass
    elif play_again in ["n","N"]:
        print("Thank u for playing")
        break
    else:
        break
