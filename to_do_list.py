class TodoList:
    def __init__(self):
        self.tasks = []

    # Add a new todo item to the list
    def add(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' has been added to the list.")

    # Update a new todo item in the list
    def update(self, task_number, update_task):
        if task_number > 0 and task_number < len(self.tasks):
            self.tasks[task_number-1] = update_task
            print(f"The task has been updated")
        else:
            print("The task is not present in the list")

    # Viewing the to_do_list
    def view(self):
        if not self.tasks:
            print("No task has been added in the list.")
        else:
            print("Tasks in your to-do-list:")
            for index, tasks in enumerate(self.tasks, start=1):
                print(f"{index}. {tasks}")

    # Delete a task from the list
    def delete(self, task_number):
        if task_number > 0 and task_number < len(self.tasks):
            self.tasks.remove(self.tasks[task_number - 1])
            print(f"The task {task_number} has been removed from the list.")
        else:
            print(f"The task number {task_number} does not exist in the list.")

    # Marking as done
    def mark(self, task_number):
        if task_number <= 0 or task_number > len(self.tasks):
            print('Invalid Task Number')
        else:
            self.tasks[task_number - 1] += '✅'
            print(f"Task {task_number} has been marked as done")


# Usage
todo = TodoList()
while True:
    print("\nSelect an option:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Update Task")
    print("5. Mark Task")
    print("6. Quit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        task = input("Enter the task: ")
        todo.add(task)
    elif choice == 2:
        todo.view()
    elif choice == 3:
        todo.view()
        num = int(input("Which task do you want to remove? "))
        todo.delete(num)
    elif choice == 4:
        todo.view()
        num = int(input("Which task do you want to update? "))
        task = input("Enter the updated task:")
        todo.update(num, task)
    elif choice == 5:
        todo.view()
        num = int(input("Which task do you want to mark as done? "))
        todo.mark(num)
    elif choice == 6:
        print("Exiting the to-do-list")
        break
    else:
        print("Invalid Option! Please enter a valid option.")
