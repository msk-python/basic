import os


tasks = []

def add_task():
    task = input("Enter your task: ")

    new_task = {
        "title": task,
        "completed": False
    }

    tasks.append(new_task)
    print("Task added successfully!")

def view_tasks():
    os.system('cls')
    if len(tasks) == 0: 
        print("No tasks found!")    
    else:
        print('#-------------- All Tasks -----------------#')
        print("All Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']} - {task['completed']}")
        print('#-------------- End All Tasks -----------------#')

def complete_task():

    view_tasks()

    if len(tasks) == 0:
        return

    task_number = int(input("Enter task number: "))

    if 1 <= task_number <= len(tasks):

        tasks[task_number - 1]["completed"] = True

        print("Task marked as completed!")

    else:
        print("Invalid task number!")


while True:

    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        pass

    elif choice == "5":
        pass

    elif choice == "6":
        print("Thank you for using To-Do List Manager!")
        break

    else:
        print("Invalid choice! Please try again.")
