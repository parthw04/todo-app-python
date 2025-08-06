# ================================== Task 2: To-Do List Application ==========================

def show_menu():
     print("\n Welcome to the TO-DO LIST APP")
     print("====== Menu ======")
     print("1) View Task")
     print("2) Add Task")
     print("3) Remove Task")
     print("4) Exit")

def load_tasks():
     try:
          with open("tasks.txt", "r") as f:
               return f.read().splitlines()
          
     except FileNotFoundError:
          return []
     
def save_task(tasks):
     with open("tasks.txt", "w") as f:
          for task in tasks:
               f.write(task + "\n")

def main():
     tasks = load_tasks()

     while True:
          show_menu()
          choice = input("Choose an Option, What you want to do? ")

          if choice == "1":
               if not tasks:
                    print("Unfortunately, No tasks yet...")
               
               else:
                    for i, task in enumerate(tasks):
                         print(f"{i + 1}. {task}")

          elif choice == "2":
               task = input("Please enter the task in the list: ")
               tasks.append(task)
               save_task(tasks)
               print("Task has been added successfully!")


          elif choice == "3":
               for i,task in  enumerate(tasks):
                    print(f"{i + 1}. {task}")

               try:
                    task_to_rem = int(input("Enter task number to delete: "))
                    tasks.pop(task_to_rem - 1)
                    save_task(tasks)
                    print("Task has been removed!")

               except:
                    print("Please enter a valid input")

          elif choice == "4":
               print("Thank You, Goodbye!!")
               break

          else:
               print("Invaid choice ")
          

if __name__ =="__main__":
     main()