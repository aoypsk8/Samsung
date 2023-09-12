import time

#create a stack List
stackl = []
    
while True:
    print("\n")
    print("========================")
    print("Manage Stack Program")
    print("1. Push data")
    print("2. Pop data")
    print("3. Display the value of stack")
    print("4. Clear stack")
    print("5. Exit the program")
    print("========================")
    c = int(input("Enter the choice:"))
    if c in (1, 2, 3, 4,5):
        if (c == 5):
            break
        if (c==1):
            if(len(stackl)>5):
                print("stack had full already!")
                time.sleep(3)
            else:
                d = int(input("Enter the data:"))
                stackl.append(d)
        elif (c==2):
            if(len(stackl)>=1):
                print("Pop element is",stackl.pop())
                time.sleep(3)
            else:
                print("stack is empty can not pop")
        elif (c==3):
            print("Stack =",stackl)
            time.sleep(3)
        elif (c==4):
            stackl.clear()
            print("Stack cleared")
            time.sleep(3)
    else:
        print("Invalid Choice, please try again")
        time.sleep(3)
