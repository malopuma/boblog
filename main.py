# boblog.py
# manage projects in your terminal

# from task import Task
from ui import UI
# from file_handling import FileHandling

run_main = True
project = None

UI.show_title()

while run_main:
    run_main, project = UI.select_project()
    print(f"The selected projet is '{project}'.")
