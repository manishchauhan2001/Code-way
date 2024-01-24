#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("Tasks in the to-do list:")
            for index, task_info in enumerate(self.tasks, start=1):
                status = "[X]" if task_info["completed"] else "[ ]"
                print(f"{index}. {status} {task_info['task']}")

    def complete_task(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1]["completed"] = True
            print(f"Task {index} marked as completed.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            deleted_task = self.tasks.pop(index - 1)
            print(f"Task {index} ('{deleted_task['task']}') deleted successfully.")
        else:
            print("Invalid task index.")


def main():
    todo_list = ToDoList()

    while True:
        print("\n=== To-Do List Application ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)

        elif choice == '2':
            todo_list.view_tasks()

        elif choice == '3':
            index = int(input("Enter the task index to mark as completed: "))
            todo_list.complete_task(index)

        elif choice == '4':
            index = int(input("Enter the task index to delete: "))
            todo_list.delete_task(index)

        elif choice == '5':
            print("Exiting the To-Do List Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()


# In[ ]:




