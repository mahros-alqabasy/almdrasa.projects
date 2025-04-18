#!/usr/bin/python3

# Enhanced ToDo List App

is_running = True

class TaskModel:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Task(id={self.id}, name={self.name})"

    def show(self):
        print(self)


class TaskManager:
    def __init__(self):
        self.tasks: list[TaskModel] = [
            TaskModel(1, "Read Social Engineering Book"),
            TaskModel(2, "Write notes on Chapter 1"),
            TaskModel(3, "Research Social Proof tactics"),
            TaskModel(4, "Practice phishing simulation"),
            TaskModel(40, "Summarize Chapter 4"),
            TaskModel(140, "Plan next reading session"),
        ]

    def showNTasks(self):
        print("\nViewing tasks...")
        try:
            n = int(input("How many tasks do you want to show? "))
        except ValueError:
            print("Invalid number!")
            return

        print(f"\nViewing first {n} tasks!")
        print("\nTasks:")
        print("ID".ljust(6), "Name")
        for task in sorted(self.tasks[:n], key=lambda x: x.id):
            print(str(task.id).zfill(4), "", task.name)
        print("Finished!\n")

    def findTask(self, id):
        return [(i, t) for i, t in enumerate(self.tasks) if t.id == id]

    def addTask(self):
        print("\nAdding a new task...")
        try:
            id = int(input("Enter task ID: "))
        except ValueError:
            print("Invalid ID format!")
            return
        name = input("Enter task name: ")

        if any(t.id == id for t in self.tasks):
            print("Task ID already exists!")
            return

        self.tasks.append(TaskModel(id=id, name=name))
        print(f"Task(id={id}) added successfully!\n")

    def removeTask(self):
        print("\nRemoving a task...")
        try:
            id = int(input("Enter task ID to remove: "))
        except ValueError:
            print("Invalid ID format!")
            return

        match = self.findTask(id)
        if not match:
            print(f"Task {id} not found!")
            return

        confirm = input(f"Are you sure you want to delete Task {id}? (y/n): ").lower()
        if confirm != "y":
            print("Deletion canceled.")
            return

        self.tasks.pop(match[0][0])
        print(f"Task {id} removed successfully!\n")

    def updateTask(self):
        print("\nUpdating a task...")
        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Invalid ID format!")
            return

        match = self.findTask(task_id)
        match = match[0]
        if not match:
            print(f"Task {task_id} not found!")
            return

        new_name = input("Enter NEW task name: ")
        match[1].name = new_name
        self.tasks[match[0]] = match[1]

        print(f"Task {task_id} updated successfully!\n")

    def help(self):
        print("""
Usage: 
  ToDo> show    # Show tasks
  ToDo> remove  # Remove task by ID
  ToDo> add     # Add a new task
  ToDo> edit    # Edit task by ID
  ToDo> help    # Show help menu
  ToDo> exit    # Exit the app
""")


def controller(manager: TaskManager, command: str):
    command = command.lower()
    commands = [
        [manager.help, "h", "help"],
        [manager.showNTasks, "s", "show", "view", "lst", "list"],
        [manager.addTask, "a", "add", "insert", "append"],
        [manager.removeTask, "r", "d", "remove", "delete"],
        [manager.updateTask, "u", "e", "update", "edit"],
    ]

    for func in commands:
        if command in func[1:]:
            func[0]()
            return

    print("[-] Sorry! Command", command, "not recognized.\n")


def main():
    manager = TaskManager()
    manager.help()

    while is_running:
        user_input = input("ToDo> ").strip().lower()
        if user_input in ["exit", "quit", "q"]:
            print("Exiting... Goodbye!")
            break
        controller(manager, user_input)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("An error occurred:", error)
