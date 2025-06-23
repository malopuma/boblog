# ui.py
# ui related stuff, input output ..

from projects_handler import ProjectsHandler as PH
from tasks_handler import TasksHandler
from typing import Tuple

class UI:

    @staticmethod
    def show_title():     
        print("boblog - startup!")
                
    # List all projects in the projects directory
    @staticmethod
    def list_projects():
        PH.list_projects()

    # Lists all the tasks of the given project
    @staticmethod
    def list_tasks(project_path):    
        tasks = TasksHandler._load_tasks_internal(project_path)
        print(f"The current project '{project_path}':")
        for i, task in enumerate(tasks):
                print(f"{i+1} - {task.title}")
                print("")
        
    @staticmethod
    def select_project() -> Tuple[bool, str] :
        
        print("Select a project:")
        UI.list_projects()   
        print("")
        print("c = create new project")
        print("q = quit")
        print("")

        selection = input("Input: ")    
        
        if selection == 'c':
            return True, PH.create_project()
        elif selection == 'q':
            return False, "QUIT"
        else:
            return True, PH.select_project(selection)

    @staticmethod
    def edit_current_project(project_path):
        while True:
            UI.list_tasks(project_path)
            
            print("\n a add task")
            print(" e edit task")
            print(" d delete task")
            print(" q quit project\n")

            choice = input()

            if choice == 'a':
                new_task = input("New task title: ").strip()
                TasksHandler.add_task(new_task, project_path)
            
            elif choice == 'e':
                pass
                
            elif choice == 'd':
                selection_str = input("Enter number of task to delete, or c to cancel").strip().lower()
                if selection_str == 'c':
                    print("Task deletion cancelled.")
                try:
                    tasks = TasksHandler._load_tasks_internal(project_path)
                    task_index = int(selection_str) -1
                    if 0 <= task_index < len(tasks):
                        deleted_task = tasks.pop(task_index)
                        print(f"Task '{deleted_task.title}' has been deleted")
                        TasksHandler._save_tasks_internal(project_path, tasks)
                    else:                         
                        print("Invalid task number. Please enter a number within the list range.")
                except ValueError:
                    print("Invalid input. Please enter a number or 'c' to cancel.")
                except Exception as e:
                    print(f"An unexpected error occurred during deletion: {e}")                  
                
            elif choice == 'q':
                return
            
            else:
                print(f"WARNING: Invalid input '{choice}'. Please select from list")
                input()       
                           
    @staticmethod
    def main_menu():
        print()
        print("1 - Show Tasks")
        print("2 - Create new task")

#   @staticmethod
#  def create_new_task():
#       Control.create_new_task()
