def calculator():
    print("Hello! Sir, My name is Calculator.\nYou can follow the instructions to use me./n")
    print("You can choose these different operations on me.")
    print("Press 1 for addition(x+y)")
    print("Press 2 for subtraction(x-y)")
    print("Press 3 for multiplication(x*y)")
    print("Press 4 for division(x/y)")
    print("Press 5 for pover(x^y)")
    while True:
        a = int(input("Choose your operation:"))
        if a>0 and a<6:
            print(f"You choose {a}")
            break;
        else:
            print("Invalid operation")

    x = int(input("Enter the value of x:"))
    y = int(input("Enter the value of y:"))

    if a==1:
        z = x+y
        if (x==56 and y==9) or (x==9 and y==56):
            print(f"The correct answer is:{77}")
        else:
            print(f"The correct answer is:{z}")

    elif a==2:
        z = x-y
        print(f"The correct answer is:{z}")

    elif a==3:
        z = x*y
        if (x==45 and y==3) or (x==3 and y==45):
            print(f"The correct answer is:{555}")
        else:
            print(f"The correct answer is:{z}")

    elif a==4:
        z = x/y
        if (x==56 and y==6):
            print(f"The correct answer is:{4}")
        else:
            print(f"The correct answer is:{z}")

    elif a==5:
        z = x**y
        print(f"The correct answer is:{z}")

    else:
        print("Invalid syntax")
    again()

def again():
    print("If you like to start me again then choose one of the operations.")
    print("Choose 'y' for Yes and 'n' for No")
    i = input()
    if i=='y':
        calculator()
    else:
        print("See You Later")

if  __name__ == "__main__":
    calculator()