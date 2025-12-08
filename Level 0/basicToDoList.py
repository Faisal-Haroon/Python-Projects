print("Basic To-Do-List")

tasks = []

while True:
    print("\n===Main Menu===")
    print("1.Add Task\n2. View Tasks\n3. Remove Task\n4.Exit")

    choice = input("Enter Your Choice (1-4)")

    if choice == "1":
        print("\n---- ADD NEW TASK ----")
        addTask = input("Enter a Task: ")
        tasks.append(addTask)
        print(f"Task {addTask} Added Successfully!")

    elif choice == "2":
        if not tasks:
            print("List is empty")
        else:
            print("\n---- TASK LIST----")
            for idx,task in enumerate(tasks,start=1):
                print(f"{idx}. {task}")

    elif choice == "3":
        if not tasks:
            print("List is Empty")
        else:
            print("\n---- TASK LIST ----")
            for idx,task in enumerate(tasks,start=1):
                print(f"{idx}. {task}")

            userChoice = input("Enter a Task Number to Remove from List")
            if userChoice.isdigit() and 1 <= int(userChoice) <= len(tasks):
                removeTask = tasks.pop(int(userChoice)-1)
                print(f"Task {removeTask} removed!")
            else:
                print("Invalid Task Number Entered")

    elif choice == "4":
        print("Exiting Program...")  
        break
    
    else:
        print("Invalid Choice. Please Enter (1-4)")