"""
A simple command-line to-do list application.
"""

tasks = []


def addtask(task):
    """Add a task to the task list."""
    tasks.append(task)
    print("task added!")


def show_tasks():
    """Display all tasks in the list."""
    if not tasks:
        print("no tasks yet")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def removetask(tasknumber):
    """Remove a task from the list by its number."""
    tasks.pop(tasknumber)
    print("task removed!!")


def main():
    """Main function to run the to-do application."""
    while True:
        print("1 Add Task")
        print("2.Show Tasks")
        print("3.Remove Task")
        print("4- Exit")
        choice = input("enter choice : ")
        if choice == "1":
            task = input("enter task : ")
            addtask(task)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            task_num = int(input("enter task no to remove: "))
            removetask(task_num)
        elif choice == "4":
            break
        else:
            print("wrong choice!!")

if __name__ == "__main__":
    main()