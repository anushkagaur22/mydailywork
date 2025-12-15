tasks = []

def show_menu():
    print("\n-- TO DO LIST MENU --")
    print("1. ADD TASK")
    print("2. VIEW TASKS")
    print("3. UPDATE TASK")
    print("4. DELETE TASK")
    print("5. EXIT")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == '1':
        task_name = input("Enter task name: ")
        tasks.append(task_name)
        print(f'Task "{task_name}" added.')

    elif choice == '2':
        print("\n-- TASK LIST --")
        if not tasks:
            print("No tasks available.")
        else:
            for idx, t in enumerate(tasks, start=1):
                print(f"{idx}. {t}")

    elif choice == '3':
        task_index = int(input("Enter task number to update: ")) - 1
        if 0 <= task_index < len(tasks):
            new_task_name = input("Enter new task name: ")
            tasks[task_index] = new_task_name
            print("Task updated successfully.")
        else:
            print("Invalid task number.")

    elif choice == '4':
        task_index = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f'Task "{removed_task}" deleted.')
        else:
            print("Invalid task number.")

    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
