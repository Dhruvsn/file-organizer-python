def show_tasks():
    print("\nYour Tasks:")
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
            if not tasks:
                print("  (No tasks yet!)")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("  (tasks.txt not found!)")

def add_task():
    task = input("Enter a new task: ")
    with open('tasks.txt', 'a') as file:
        file.write(task + '\n')
    print("Task added!")

def delete_task():
    show_tasks()
    try:
        number = int(input("\nEnter the number of the task to delete: "))
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            with open('tasks.txt', 'w') as file:
                file.writelines(tasks)
            print(f"Deleted: {removed.strip()}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    except FileNotFoundError:
        print("tasks.txt not found")

# MENU
while True:
    print("\nWhat do you want to do?")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Choose an option: ")
    

    if choice == '1':
        add_task()
    elif choice == '2':
        delete_task()
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        name = input("Enter your name: ")
        print("Bye " + name)
        break
    else:
        print("Invalid choice.")

