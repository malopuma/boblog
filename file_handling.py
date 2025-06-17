import os
import pickle


class FileHandling:

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

    # To select a project from the projects directory. Returns filename
    # string
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
                project = projects[selection-1]
                return project
            else:
                return "Invalid project number"
            
        except:
            return (f"'{selection}' is not a valid number!")

    # Create a new project in the projects directory                   
    @staticmethod
    def create_project(title: str):
        print("Started 'FH.create_project(title: str)'")
    
    @staticmethod
    def open_file(filename: str) -> list :
        try:
            with open(filename, 'rb') as file:
                print(f"opened file: '{filename}'")
                tasks = pickle.load(file)
                return tasks

        except FileNotFoundError:
            print(f"Error: File '{filename}' not found")
            return []

        except Exception as e:
            print(f"Something went wrong when trying to open '{filename}': '{e}'!!")
            return []

    @staticmethod
    def save_file(filename : str, data_to_save: list):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(data_to_save, file)
                print(f"Sucessfully saved '{data_to_save}' to '{filename}'.")

        except Exception as e:
            print(f"Something went wrong when saving '{data_to_save}' to '{file}'!!.")
                            
