import json
File_Name="task.json"
# Load task from file
def load_tasks():
    try:
        with open(File_Name,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
# Save task
def save_tasks(tasks):
    with open(File_Name,"w")as file:
        json.dump(tasks,file,indent=4 )
#Display tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo task found\n")
        return
    print("\nyour tasks")
    for index, task in enumerate(tasks,start=1):
        status ="[@]" if task["completed"] else "[ ]"
        print(f"{index}.{status} {task["title"]}")
        print()
# Add new tasks
def add_task(tasks):
    title =input("Enter task ")
    tasks.append({"title":title,"completed":False})
    save_tasks(tasks)
    print("Task added!")
# Mark task as completed
def complete_task(tasks):
    show_tasks(tasks)
    try:
        task_num=int(input("Enter task's number to mark as completed. ")) -1
        if 0<= task_num<len(tasks):
            tasks[task_num]["completed"] =True
            save_tasks(tasks)
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number!")
# Delete tasks
def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_num=int(input("Enter task number to delete: ")) -1
        if 0<= task_num<len(tasks):
            del tasks[task_num]
            save_tasks(tasks)
            print("Task deleted!")
    except ValueError:
        print("Please enter a valid number!")
# main loop
def main():
    task = load_tasks()
    while True:
        print("\nTOo_Do List")
        print("1.View task")
        print("2.Add task")
        print("3.Mark task as completed")
        print("4.Delete task")
        print("5.Exit")
        choice = input("Enter your choice: ")
        if choice=="1":
            show_tasks(task)
        elif choice=="2":
            add_task(task)
        elif choice=="3":
            complete_task(task)
        elif choice=="4":
            delete_task(task)
        elif choice=="5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please choose between 1 to 5.")
if __name__ == "__main__":
    main()