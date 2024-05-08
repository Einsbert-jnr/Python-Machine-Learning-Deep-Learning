import random

condition = True

while condition:
    choices = ["scissors", "rock", "paper"]

    computer = random.choice(choices)

    player = None
    if player not in choices:
        player = input("Enter a choice:>> ").lower()
        if player == computer:
            print(f"""Player's choice:> {player} \nComputer's choice:> {computer}""")
            print("There's a TIE")
            print()
            print()
        else:
            if player == "scissors":
                if computer == "paper":
                    print(f"""Player's choice:> {player} \nComputer's choice:> {computer}""")
                    print("You won")
                    print()
                    print()
                elif computer == "rock":
                    print(f"""Player's choice:> {player} \nComputer's choice:> {computer}""")
                    print("Computer won")
                    print()
                    print()
            elif player == "rock":
                if computer == "paper":
                    print(f"""Player's choice:> {player} \nComputer's choice:> {computer}""")
                    print("Computer won")
                    print()
                    print()
                elif computer == "scissors":
                    print(f"""Player's choice:> {player} \nComputer's choice:> {computer}""")
                    print("Player won")
                    print()
                    print()
            elif player == "paper":
                if computer == "rock":
                    print(f"""Player's choice:> {player} \nComputer's choice:> {computer}""")
                    print("Player won")
                    print()
                    print()
                elif computer == "scissors":
                    print(f"""Player's choice:> {player} \nComputer's choice:> {computer}""")
                    print("Computer won")
                    print()
                    print()
            else:
                print(choices)
                print("Choose from the choices above or enter quit or q: to exit or c: to continue playing")
                out = input("quit or c >>>")
                if out.lower() == "quit" or out.lower() == "q":
                    exit()
                elif out.lower() == 'c':
                    condition = True
                else:
                    print(choices)
                    print("Choose from the choices above or enter quit or q: to exit or c: to continue playing")
                    print("Follow the above prompt carefully!!!")
                    print()
                    print()