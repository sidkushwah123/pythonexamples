a = [1,2,34,5,6]

def cv(b):
    return b>8

listl = list(map(cv,a))
print(listl)

list2 = list(filter(cv,a))
print(list2)