# stone paper seaser game 

import random

option = ["STONE","PAPER","SISER"]

user_score = 0
computer_score = 0
turn = 0

print("Let's play STONE PAPER SISER")


k="y"
while(k !="n"):

    user_score = 0
    computer_score = 0
         
    for i in range(3):
        
        if i != 2:
            print("\n"+"*"*15+"Round"+str(i+1)+"*"*15)
        else:
            print("\n"+"*"*15+"FinalRound"+"*"*15)

        turn += 1
        print("\nSelect your choice:          For quit press q")
        for key in option:
            print(key)
        print()
        user = input()
        user_choice = user.upper()
        computer_choice = random.choice(option)
        if user_choice == "STONE" or user_choice == "PAPER" or user_choice == "SISER" :
            print("\nYour choice is "+user_choice+" MY choice is "+computer_choice)

        if user_choice == "STONE" :
            if computer_choice == "STONE":
                print("Ohhh its A tie")
            elif computer_choice == "PAPER":
                computer_score += 1
                print("Yeaaa you lose")
            else :
                user_score += 1
                print("aHH You win this time....")

        elif user_choice == "PAPER":
            if computer_choice == "STONE":
                user_score += 1
                print("aHH You win this time....")
            elif computer_choice == "PAPER":
                print("Ohhh its A tie")
            else :
                computer_score += 1
                print("Yeaaa you lose")

        elif user_choice == "SISER":
            if computer_choice == "STONE":
                computer_score += 1
                print("Yeaaa you lose")
            elif computer_choice == "PAPER":
                user_score += 1
                print("aHH You win this time....")
            else :
                print("Ohhh its A tie")
                

        elif user_choice == "Q":
            print("O shit You quit the game ")
            break
        else:
            print("\nWrong input..! Try entering from the given option")
            continue
        print("\nYour score: " + str(user_score) +"\nMy score: " + str(computer_score) +"\n")
    
    print("*"*40+"\n")

    if user_score > computer_score:
        print("Ohh.. Shits.. You WIN...but i bet you will not win again")
    elif user_score < computer_score:
        print("LOSER....I win and you LOSE")
    else:
        print("I am Shocked.. Ahhh... it's a TIE")
    print("\nYour score: " + str(user_score) +"\nMy score: " + str(computer_score))
    if user_choice != "Q" :
        a = input("\nWant you play again? y/n\n")
    else:
        break
    k=a