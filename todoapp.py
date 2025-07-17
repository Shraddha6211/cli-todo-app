import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    #Load tasks from the JSON file.
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    #Save tasks to the JSON file.
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task():
    #Add a new task to the to-do list.
    tasks = load_tasks()
    task=input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!!")

def view_tasks():
    # View the tasks in the to-do list.
    tasks = load_tasks()
    if len(tasks)==0:
        print("No tasks due!!")
    else:
        print('List of tasks:')
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def delete_task():
    # Delete a task from the to-do list.
    tasks = load_tasks()
    if len(tasks)==0:
        print('No tasks to delete. Empty list. ')
    else: 
        print('Tasks:')
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        choice=int(input('Enter the task number to delete:'))

        if 0< choice <= len(tasks):
            del tasks[choice-1]
            save_tasks(tasks)
            print('Task deleted successfully.')
        else:
            print('Invalid task number.')

def main():
    #Run the command-line to-do list application
    
    while True:
        print('\n --------- To-Do-List Application ----------')
        print('1. Add a new task')
        print('2. View tasks')
        print('3. Delete a task.')
        print('4. Quit')

        choice=int(input('Enter your choice:'))
        if choice==1:
            add_task()
        elif choice==2:
            view_tasks()
        elif choice==3:
            delete_task()
        elif choice == 4:
            print('Thank you for using our To-Do-List Application.')
            break
        else:
            print('Invalid choice. Please try again')

if __name__ =="__main__":
    main()