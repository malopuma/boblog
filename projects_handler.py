# file_handling.py
# for managing the projects (project.pkl files)

import os

class ProjectsHandler:

    # Show all projects in the current directory
    @staticmethod
    def list_projects() -> None:
        try:
            i = 1
            projects = os.listdir("projects")
            for project in projects:
                print(f"{i} - {project}")
                i = i+1
                
        except Exception as e:
            print(f"ERROR when trying list_projects: '{e}'.")
        
        return 

    # To select a project from the projects directory. Returns filename string
    # Has to be reworkes to take projects directory and then return relitve path
    
    @staticmethod
    def select_project(selection) -> str:
        try:
            # Create a list of projects from the directory
            projects = os.listdir("projects")
            
        except Exception as e:
            print(f"ERROR when trying list_projects: '{e}'.")
            return ""
                
        try:
            selection = int(selection)
            if 0 << selection <= len(projects):
                project_filename_str = projects[selection-1]
                # temp fix returns project path instead of filename
                project_path = "projects/" + project_filename_str
                return project_path
            else:
                return "Invalid project number"
            
        except:
            return (f"'{selection}' is not a valid number!")

    # Create a new project in the projects directory                   
    @staticmethod
    def create_project() -> str :
        print("Started 'FH.create_project(title: str)'")

        new_project_title = input("Title: ")
        new_project_filename = new_project_title + ".pkl"
        new_project_path = "projects/" + new_project_title +".pkl"
        
        try:
            with open(new_project_path, 'wb'):
                return new_project_filename
        except Exception as e:
            print(f"ERROR when creating file '{new_project_path}': {e}")
            return "ERROR"
            
