num1=input("enter num 1 - \n")
num2=input("enter num 2 - \n")
try:
    print("the two number sum is",int(num1)+int(num2))
except Exception as e: 
    print(e)
    print("this line is inpprtnt")