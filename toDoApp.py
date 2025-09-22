"""
A simple command-line to-do list application.
"""

tasks = []


def addtask(task):
    
    tasks.append(task)
    print("task added!")


def show_tasks():
    
    if not tasks:
        print("no tasks yet")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def removetask(tasknumber):
    
    tasks.pop(tasknumber)
    print("task removed!!")


def main():
   
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