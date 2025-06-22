# ui.py
# ui related stuff, input output ..

from projects_handler import ProjectsHandler as PH
from tasks_handler import TasksHandler
from typing import Tuple

class UI:

    @staticmethod
    def _input_menu_validation(input):
        pass

    @staticmethod
    def show_title():     
        print("boblog - startup!")        
    
    @staticmethod
    def select_project() -> Tuple[bool, str] :
        
        print("Select a project:")
        PH.list_projects()   
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
    def show_current_project(project_path):
        while True:
            tasks = TasksHandler._load_tasks_internal(project_path)
            print(f"The current project '{project_path}':")
        
            for i, task in enumerate(tasks):
                print(f"{i+1} - {task.title}")
        
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
                pass
            elif choice == 'q':
                return
            else:
                print(f"WARNING: Invalid input '{choice}'. Please select from list")
        
                           
    @staticmethod
    def main_menu():
        print()
        print("1 - Show Tasks")
        print("2 - Create new task")

#   @staticmethod
#  def create_new_task():
#       Control.create_new_task()
