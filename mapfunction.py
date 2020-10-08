# #if we apply any thing whole list we use he map function so it do our work easy

# #simple example of map function
# # if there is no list of string and we want to typecast in int then

number = ["1","2","3","4","5","6"]

# #if do with without map 

for i in range(len(number)):
    number[i] = int(number[i])

number[2] = number[2]+1

print(number[2])
print(number)

# # if we want do same with map()

print("\nsecond method result start here \n")

number1 = ["1","2","3","4","5","6"]

number1 = list(map(int,number1))
number1[2] = number1[2]+1

print(number1[2])
print(number1)

#function  example of map function
# if there is no function we want to apply to any numbers for that without lambda


print("\nthird method result start here \n")

def sqr(a):
    return a*a

def cube(a):
    return a*a*a

func = [sqr,cube]

def x(a):
    return a(i)

for i in range(5):
    var = list(map(x,func))
    print(var)

# if there is no function we want to apply to any numbers for that with lambda

print("\nforth method result start here \n")

def sqr(a):
    return a*a

def cube(a):
    return a*a*a

func = [sqr,cube]

for i in range(5):
    var = list(map(lambda x:x(i),func))
    print(var)

