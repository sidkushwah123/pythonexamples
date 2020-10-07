'''print("Enter THE NO OF ROWS U want ")
n = int(input())

print("your choice is 1 or 0")
b = int(input())

bolean = bool(b)

if bolean == True :
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end="")
        print("\n")
elif bolean == False :
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print("*",end="")
        print("\n")
else:
    print(" second choice is wrong ")'''

r = int(input("Enter Row: "))
n = int(input("Enter Boolean 1/0 :"))
b = bool(n)
if b:
    for i in range(r+1):
        print("*" * i)
else:
    for j in range(r):
        print((r-j) * "*")

