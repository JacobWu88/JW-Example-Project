import random
play = "y"
print("Ver 1.0")
while play in ("y", "yes", "start", "play", "continue"):
    user = input("Rock Paper Scissors: ").lower()
    com = random.choice(["rock", "paper", "scissors"])
    if com == user:
        print(f"Computer chose {user}, It is a tie")

    elif user == "paper":
        if com == "scissors":
            print("Computer chose scissors: You lost!")
        else:
            print("Computer chose rock: You Win!")

    elif user == "rock":
        if com == "paper":
            print("Computer chose paper: You lost!")
        else:
            print("Computer chose scissors: You Win!")

    elif user == "scissors":
        if com == "rock":
            print("Computer chose rock: You lost!")
        else:
            print("Computer chose paper: You Win!")

    else:
        print("Invalid Choice")
    play = input("Play again?(Y/N): ").lower()


    if play in ("n", "no", "exit", "quit", "stop", "shut off"):
        print("Shut off")

        #blah blah blah
