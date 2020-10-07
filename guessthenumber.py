#no of gaueses 

gn = 18
chance = 5

print("ENTER YOUR NO FOR GUESS")
print("NO OF GUESS U have ",chance)

while(True):

    cn = int(input())
    chance = chance - 1

    if cn == gn:
        print("hurre YOUR GUESS ",cn,"IS PERFECT YOU WIN THE GAME ")
        print("NO OF GUESS taked by you",5-chance)
        break
    elif cn>gn:
        print("YOUR GUESS ",cn,"IS WRONG YOUR NUMBER IS GREATER THAN ACTUAL NO")
    else:
        print("YOUR GUESS ",cn,"IS WRONG YOUR NUMBER IS LEASER THAN ACTUAL NO")

    print("NO OF GUESS LEFT",chance)

    if chance == 0:
        print("GAME OVER")
        break
    
