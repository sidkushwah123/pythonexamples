print("Enter your age :")
age = int(input())

if age>7 and age<100:
    if age>18 :
        print("YOU CAN DRIVE")

    elif age==18 :
        print("WE CANT DETERMINE COME AND WE CHEAK U THEN GIVE DECISION")
    else:
        print("YOU CANT DRIVE ")
else:
    print("invalid age ")