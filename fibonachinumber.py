def fibonachi(n):

    a = 0
    b = 1
    print(a,b,end=" ")
    for i in range (n):
        c = a+b
        print(c,end=" ")
        a = b
        b = c
        
a = int(input("enter the number how many step u want"))
fibonachi(a)
