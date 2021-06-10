

# 1. Vytvořte hru „kámen nůžky papír teď“ tak aby:
# a). Byl od uživatele získán vstup.
# b). Počítač vygeneroval vlastní tah.
# c). Byl vyhodnocen a zobrazen výsledek (tzn. Kdo co táhl a kdo vyhrál) – stačí výstup do konzole

import random

def RSP():
    choices  = { "1": "rock", "2": "scissors", "3":"paper"}
    choice = input("Choose one of following: 1 -> rock, 2-> scissors or 3-> paper:")

    try:
        choice_int = int(choice)
        if (choice_int < 1) or (choice_int > 3):
            print("Your choice was wrong, enter number between 1-3!!")
        else:
            print("You choosed: "+ choices.get(str(choice_int)))
            AI = random.randrange(1,4)
            print("AI's turn: "+choices.get(str(AI)))
            if(AI == 1 and choice_int == 3) or (AI == 2 and choice_int == 1) or (AI == 3 and choice_int == 2):
                print("CONGRATS, YOU WON!")
            elif (AI == 3 and choice_int == 1) or (AI == 1 and choice_int == 2) or (AI == 2 and choice_int == 3):
                print("AI WON, gl next time")
            else:
                print("IT'S A DRAW !!")
    except ValueError:
        print("Enter number between 1-3!!")
