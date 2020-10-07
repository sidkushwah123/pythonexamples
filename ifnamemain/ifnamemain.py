def name(data):
    print(f"hello mr {data}")

def age(data):
    print(f"your age is 55 mr {data}")

def schol(data):
    print(f"your school name is bvn mr {data}")

if __name__ == "__main__":
    a = input("enter your name ")

    print("1\n2\n3\n")

    b = int(input())

    if b==1:
        name(a)
    elif b ==2:
        age(a)
    else:
        schol(a)

if __name__ == "__main__":
    name("raman")


print(f"and the value of name is there {__name__}")
    



