#!/usr/bin/python3


# todo list app


is_running = True



class TaskModel:
  def __init__(self, id, name):
    self.id = id
    self.name = name

  def toString(self):
    return f"Task(id={id}, name={name})"
    
  def show(self):
    print(self.toString())



tasks:list[TaskModel] = [
  TaskModel(1, "Read Social Engineering Book"),
  TaskModel(2, "Read Social Engineering Book"),
  TaskModel(3, "Read Social Engineering Book"),
  TaskModel(4, "Read Social Engineering Book"),
  TaskModel(40, "Read Social Engineering Book"),
  TaskModel(140, "Read Social Engineering Book"),
]


def showNTasks():
  print("Viewing tasks...")
  n = input("How many tasks do you want to show? ")
  n = int(n)
  print(f"Viewing first {n} tasks!")
  print("Tasks:")
  print("ID", " " *2, "Name")
  
  for task in tasks[:n]:
    print(f'{"0" * int(4-len(str(task.id)))}{task.id}', "", task.name)
  print("Finished!")

  
  # 4-positions
  
def findTask(id):
  match = [(index, value) for index, value in enumerate(tasks) if value.id == id]

  return match if match else None


def addTask():
  print("Adding a new task...")
  id = int(input("What is task id? "))
  name = input("What is task name? ")

  task = TaskModel(id=id, name=name)
  match = [x for x in tasks if x.id == id]
  
  if len(match) > 0:
    print("Sorry! Task id already exists!")
    return
  
  tasks.append(task)
  print(f"Task(id={id}) added successfully!")

def removeTask():
  print("Removing a Task...")
  id = int(input("What is task id? "))
  
  match = [(index, value) for index, value in enumerate(tasks) if value.id == id]

  if len(match) <= 0:
    print(f"Sorry! Task {id} not found!")
    return

  # remove task at index
  tasks.pop(match[0][0])

  print(f"Task {id} removed successfully!")



def updateTask():
  print("Updating Task...")
  task_id = int(input("What is task id? "))
  
  match = findTask(task_id)
  if match == None:
    print(f"Task {task_id} not found!")
    return
  match = match[0]
  
  # print(match, type(match), match[0], match[1])
  
  new_task_name = input("What is NEW task name? ")
  match[1].name = new_task_name

  # update task in database
  tasks[match[0]] = match[1]
  
  print(f"Task {task_id} UPDATED successfully")
  
def help():
  text = """
    Usage: 
      Prompt> show    # will show n-tasks
      Prompt> remove  # will remove tasks by id
      Prompt> add     # will add task
      Prompt> edit    # will edit task by id  
  """
  print(text)

def exitApp():
  print("Thank you for using out ToSo list app")
  exit(0)
  


def controller(command):
  command = command.lower()
  commands = [
    [help, "h", "help"],
    [showNTasks, "s", "show", "view", "lst", "list"],
    [addTask, "a", "add", "insert", "append"],
    [removeTask, "r", "d", "remove", "delete"],
    [updateTask, "u", "e", "update", "edit"],
    [exitApp, "z", "x", "exit", "close", "fi", "finish"],
  ]


  for fun in commands:
    if command in fun:
      fun[0]()
      return

  print("[-] Sorry! Command", command, "not found!")
  


def main():
  help()
  while is_running:
    user_input = input("ToDo> ")
    controller(user_input)




# run
if __name__ == "__main__":
  try:
    main()
  except Exception as Error:
    print(Error)



