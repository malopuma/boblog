from control import Control

class UI:
    
    @staticmethod
    def main_menu():
        print()
        print("1 - Show Tasks")
        print("2 - Create new task")

    @staticmethod
    def create_new_task():
          Control.create_new_task()
