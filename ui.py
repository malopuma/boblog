from control import Control
from file_handling import FileHandling as FH
from typing import Tuple

class UI:

    @staticmethod
    def show_title():     
        print("boblog - startup!")        
    
    @staticmethod
    def select_project() -> Tuple[bool, str] :
        
        print("Select a project:")
        FH.list_projects()   
        print("")
        print("c = create new project")
        print("q = quit")
        print("")

        selection = input("Input: ")    
        if selection == 'c':
            FH.create_project("test")
            return True, ""
        elif selection == 'q':
            return False, ""
        else:
            return True, FH.select_project(selection)
                           
    @staticmethod
    def main_menu():
        print()
        print("1 - Show Tasks")
        print("2 - Create new task")

    @staticmethod
    def create_new_task():
          Control.create_new_task()
