tasks = []
def take_task():
    name = input("Enter the task name: ").capitalize()
    tasks.append(name)
    print(f"You have Successfully added '{name}' task.")

def view_the_task():
    if not tasks:
        print("You have not added any task.")
    else:
        print("\n Task List")
        for i, task in enumerate(tasks):
            print(i, task)

def delete_the_task():
    print(" Here is your to-do-task")
    view_the_task()
    task_number = int(input("Enter the task number: "))
    removed_task = tasks.pop(task_number - 1)
    try:
        print(f"You have Successfully removed '{removed_task-1}' task.")
    except (IndexError, ValueError):
        print("Please enter a valid task number.")

def main():
    while True:
        print("\n 1. TO ADD TASK\n 2. TO VIEW THE TASKS\n 3. TO DELETE THE TASKS\n 4. EXIT")

        try:
            user_input_choice = int(input("Enter your choice: "))

            if user_input_choice == 1:
                take_task()
            elif user_input_choice == 2:
                view_the_task()
            elif user_input_choice == 3:
                delete_the_task()
            elif user_input_choice == 4:
                print("Exiting...")
                break
            else:
                print("Please enter a number between 1 and 4.")

        except ValueError:
            print("Invalid input. Please enter a number.")


main()