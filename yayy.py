tasks=[]

running=True

while running:
    print("/n 1.Add a Task.")
    print("2.View Task.")
    print("3.Remove Task.")
    print("4.Exit.")

    user=int(input("Enter your choice(1/2/3/4):"))

    if user==1:
        task=input("Enter tasks:")
        tasks.append(task)
        print("Task successfully added !")

    elif user==2:
        if not tasks:
            print("No task to view.")
        else:
            for task in tasks:
                print(task)

    elif user==3:
        if not tasks:
            print("No task to remove.")
        else:
            for task in tasks:
                print(task)

            num=int(input("Which task number to remove?"))
            tasks.remove(tasks[num-1])
            print("Task removed!") 

    elif user==4:
        running=False
        print("Thankyou !")

    else:
        print("Invalid choice")

    

    