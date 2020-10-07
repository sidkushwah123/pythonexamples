f = open("py.txt")

content = f.read()

print(content)

f.close()

# if we want read by single line by line 

f = open("py.txt")

print(f.readline())

f.close()

# if we want all lines in a list

f = open("py.txt")

print(f.readlines())

f.close()

