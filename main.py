# boblog.py
# manage projects in your terminal

# from task import Task
from ui import UI
from file_handling import FileHandling

run_main = True
     
UI.show_title()

while run_main:
    run_main = UI.select_project()
