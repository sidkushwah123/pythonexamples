print("ENTER FIRST VALUE")
v1 = int(input())

print("ENTER SECOND VALUE")
v2 = int(input())

print("enter the choice opration u want from below")
print("ADD","SUB","MUL","DIV",sep='\n')
choice = input()
choice2 =choice.upper()

if choice2 == "ADD":
    if v1 == 56 and v2 == 9:
        print("ANS IS 77")
    else:
       v3 = v1+v2
       print("ANS IS ",v3)
elif choice2 =="SUB" :
    if v1 == 56 and v2 == 9:
        print("ANS IS 75")
    else:
        v3 = v1-v2
        print("ANS IS ",v3)
elif choice2 == "MUL":
    if v1 == 45 and v2 == 3:
        print("ANS IS 555")
    else:
        v3 = v1*v2
        print("ANS IS ",v3)
elif choice2 == "DIV":
    if v1 == 56 and v2 == 6:
        print("ANS IS 4")
    else:
        v3 = v1/v2
        print("ANS IS ",v3)
else :
    print("wrong choice:")
