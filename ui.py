from control import Control

class UI:

    @staticmethod
    def show_title():     
        print("boblog - startup!")        
    
    @staticmethod
    def select_project() -> bool :
        selection = 1
        
        print("Select a project:")
        print("")
        print("PLACEHOLDER")
        print("")
        print("q = quit")
        print("")
        selection = input("Input: ")

        if selection == 'q':
            return False

        else:
            return True
    
    @staticmethod
    def main_menu():
        print()
        print("1 - Show Tasks")
        print("2 - Create new task")

    @staticmethod
    def create_new_task():
          Control.create_new_task()
