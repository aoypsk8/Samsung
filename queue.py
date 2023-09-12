import time
queue = []
    
while True:
    print("\n")
    print("========================")
    print("Manage Queue Program")
    print("1. Enqueue data")
    print("2. Dequeue data")
    print("3. Display the value of queue")
    print("4. Clear queue")
    print("5. Exit the program")
    print("========================")
    c = int(input("Enter the choice:"))
    if c in (1, 2, 3, 4, 5):
        if (c == 5):
            break
        if (c == 1):
            d = int(input("Enter the data:"))
            queue.append(d)
            print("Enqueued element is", d)
            time.sleep(3)
        elif (c == 2):
            if len(queue) >= 1:
                print("Dequeued element is", queue.pop(0))
                time.sleep(3)
            else:
                print("Queue is empty, can not dequeue")
        elif (c == 3):
            print("Queue =", queue)
            time.sleep(3)
        elif (c == 4):
            queue.clear()
            print("Queue cleared")
            time.sleep(3)
    else:
        print("Invalid Choice, please try again")
        time.sleep(3)