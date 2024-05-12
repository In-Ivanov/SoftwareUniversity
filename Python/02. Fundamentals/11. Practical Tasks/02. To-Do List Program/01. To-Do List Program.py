def show_menu():
    print('\n===== To-Do-List Menu =====')
    print('1. Add Task')
    print('2. Mark Task as Completed')
    print('3. View Tasks')
    print('4. Quit')


def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfuly!")


def mark_completed(todo_list):
    print("===== Tasks =====")
    display_tasks(todo_list)

    index = int(input("Enter the index of the task to mark as completed: "))

    if 0 <= index < len(todo_list):
        todo_list[index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid index. Please enter a valid index.")


def display_tasks(todo_list):
    print("===== Tasks =====")
    for i, task in enumerate(todo_list):
        status = "[X]" if task["completed"] else "[ ]"
        print(f"Index {i}. {status} {task["task"]}")


def todo_list_program():
    todo_list = []

    while True:
        show_menu()
        choise = input('Enter your chois (1-4): ')

        if choise == "1":
            add_task(todo_list)

        elif choise == "2":
            mark_completed(todo_list)

        elif choise == "3":
            display_tasks(todo_list)

        elif choise == "4":
            print("Exiting the program. Goodbay!!!")
            break

        else:
            print("Invalid choise. Please enter a number between 1 and 4.")


todo_list_program()
