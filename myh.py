# '''print("hello kushwah ji kaise ho ")

# a = int(input(" ENTER FIRST NO "))
# b = int(input(" enter second number "))

# c = a+b
# print("addition is ", c)

# z= "my name is sachin"

# print(z[::-1])'''

# d = {"b":{"m":"b","b":"l"}}
# # print(type(d))
# d["sachin"] = "burger"
# # d["kajal"] = "burger"
# # del d["kajal"]

# print(d["b"]["m"])

# a = input("enter")
# a.lower()
# a = 1,2,3
# print(len(a))

# stg='ABCD'
# len(stg)

# print(len(stg))

'''def pyfunc(r):
    for x in range(r):
        print(' '*(r-x-1)+'*'*(2*x+1))    
pyfunc(9)

a = 2*0+1
print(a)'''

# Enter number of terms needed                   #0,1,1,2,3,5....
a=int(input("Enter the terms"))
f=0                                         #first element of series
s=1                                         #second element of series
if a<=0:
    print("The requested series is",f)
else:
    print(f,s,end=" ")
    for x in range(2,a):
        next=f+s                           
        print(next,end=" ")
        f=s
        s=next