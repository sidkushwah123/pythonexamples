#using enumrate function 
# take list of vegitable and try to acess odd product of that list 

li = ["bhindi","aloo","gobi","shimla"]

#without enumrate function

i = 1
for item in li:
    if i%2 != 0:
        print(item)
    i += 1

#with enumrate function

print(f"\nsecond result start here\n")

for index, item in enumerate(li):
    if index%2 == 0:
        print(item)