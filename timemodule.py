import time

a = time.time()
k=0
while(k!=45):
    print(f"while")
    k+=1
print(f"while is taking{time.time()-a}")

b = time.time()
for i in range(45):
    print(f"while")
print(f"for is taking{time.time()-b}")
