class ToDoList:
    def __init__(self):
        self.tasks=[]
        
    def add_task(self,task):
        self.tasks.append(task)
        print("Task added: ", task)
        
    def remove_task(self,task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed: ", task)
        else:
            print("Task not found: ", task)
            
    def dispaly_tasks(self):
        if self.tasks:
            print("Task: ")
            for index, task in enumerate(self.tasks,start=1):
                print(f"{index}.{task}")
        else:
            print("No tasks in the list")
        
def main():
    todo_list = ToDoList()
    
    while True:
        print("\nOption")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Quit")
        
        choice = input("enter your choice:")
        
        if choice =="1":
            task= input("Enter the task:")
            todo_list.add_task(task)
        elif choice=="2":
            task=input("Enter the task to remove:")
            todo_list.remove_task(task)
        elif choice=="3":
            todo_list.dispaly_tasks()
        elif choice=="4":
            print("goodbye!")
            break
        else:
            print("Invalid choice. Please choose agian")
            
if __name__== "__main__":
    main()
    
        