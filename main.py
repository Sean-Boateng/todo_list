tasks = []
if __name__ == "__main__":
    def addTask():
        task = input("Please enter a task: ")
        tasks.append(task)
        print(f"Task '{task}' add to the list")


    def listTasks():
        if not tasks:
            print("---------------------------------------------------")
            print("There are no tasks currently.")
        else:
            print("---------------------------------------------------")
            print("Current tasks: ")
            for index,task in enumerate(tasks):
                print(f"Task #{index}. {task}")



    def deleteTask():
        listTasks()
        try:
            taskToDelete = int(input("Enter task number "))
            if taskToDelete >= 0 and taskToDelete < len(tasks):
                tasks.pop(taskToDelete)
                print(f"Task # {taskToDelete} has been removed")
                print("Here is update list: ")
                listTasks()
            else:
                print(f"Task # '{taskToDelete}' was not found")
        except:
            print("Invalid input.")




    # Create a loop to run app
    print('Welcome to the todo list app')
    while True:
        print("\n")
        print("Please select one of the following options")
        print("---------------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")
        

        choice = input("Enter your choice: ")

        if(choice == "1"):
            addTask()
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
            listTasks()
        elif(choice == "4"):
            break
        else:
            print("Invalid response")
    print("Goodbye!!")