#Lets List the functions of this to-do list
#1. Add task
#2. Tasks divided based on priorities
#3. Tasks can be marked as done
#4. Tasks can have deadlines too

def add_task():
    task = input("Enter your task: ")
    return task

def remove_task():
    for j in tasks:
        print(j)
    while True:
        task = input("Enter the task to remove: ")
        if task in tasks:
            break
        else:
            print("Invalid Input.")
    return task

tasks = []
while True:
    #exception handling to be done in this block of code
    print("***To Do List Application***")
    print("This is an application where you can set goals, and tasks that you expect to complete in a short time period.")
    print("So choose away between: \n1. Adding a task\n2. Delete a task\n3. Exit")

    while True:
        try:
            choice = int(input("What do you wanna do?: "))
            break
        except ValueError:
            print("Please enter a valid integer between 1-3. ")
    match choice:
        case 1:
            tasks.append(add_task())
            print("The task has been added to the list!")
            for i in tasks:
                print(i)
        case 2: #need to create an exit option when the task list is empty
            tasks.remove(remove_task())
            print("The task has been removed from the list!")
            for i in tasks:
                print(i)
        case 3:
            print("Exiting.....")
            break
        case _:
            print("That is not an appropriate value, the choice is between 1, 2 and 3.")

