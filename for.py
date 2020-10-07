'''list1 = ["sachin",5,"name",4,"rohit","rama",5,6,8]

for data in list1:
    if str(data).isnumeric() and data>6 :
        print(data,end=" ")'''

# Exercise Question 2: Print the following pattern
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5



'''for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()'''

# Exercise Question 3: Accept number from user and calculate the sum of all number between 1 and given number
#For example user given 10 so the output should be 55

'''print("welcome for easy calculaion")
print("Enter ypur number")
num=int(input())
a=0
for i in range(num,0,-1):
    a=a+i
print(a)'''


# Exercise Question 4: Print multiplication table of given number

print("EMTER THE NUMBER FOR TABLE",end="\n")
num= int(input())

for i in range(1,11):
    result = num*i
    print(result)
    
