client_list = {1:"Harry",2:"Rohan",3:"Sachin"}
loG_list = {1:"Excercise",2:"Diet"}

def getdate():
    import datetime
    return datetime.datetime.now()

try:
    print("Select the client:")
    for key,value in client_list.items():
        print("Press",key,"for",value,"\n",end="")
    client_name = int(input())

    print("Selected client :",client_list[client_name])

    print("Press 1 for Log data")
    print("Press 2 for Retrive data")

    op = int(input())

    if op == 1:
        for key,value in loG_list.items():
            print("press",key,"for",value,"\n",end="")
        
        log_name = int(input())

        print("Selected job :",loG_list[log_name])

        k="y"
        while(k != "n"):
            with open(client_list[client_name]+"_"+loG_list[log_name]+".txt","a") as file:
                print("type :")
                log_data = input()
                file.write("[ " + str(getdate()) + " ] : " + log_data + "\n")
                print("Data log sucesfully!")
            choice_for_again = input("ADD more log? y/n:")
            k = choice_for_again
            continue

    elif op == 2:
        for key,value in loG_list.items():
            print("press",key,"to retrive",value,"\n",end="")

        retrive_choice = int(input())
        print(client_list[client_name],"-",loG_list[retrive_choice],"Report :")

        with open(client_list[client_name]+"_"+loG_list[retrive_choice]+".txt") as file:
            data = file.read()
            print(data)

    else:
        print("invalid input !!!")
    
except Exception as e:
    print("Wrong input!!!")