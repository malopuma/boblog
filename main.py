# boblog.py
# manage projects in your terminal

from ui import UI
from tasks_handler import TasksHandler as TH

run_main = True
project_path = None

UI.show_title()

while run_main:
    run_main, project_path = UI.select_project()
    if run_main:
        UI.show_current_project(project_path)


    
