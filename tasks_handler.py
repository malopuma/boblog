import os
import pickle
from typing import List, Any
from task import Task as TS # Assuming TS is your Task class alias

# Make sure DATA_DIR is defined if project_path is relative
# For example:
# DATA_DIR = "projects" # If project_path is just the filename in this dir

class TasksHandler:
    @staticmethod
    def _load_tasks_internal(project_path: str) -> List[TS]:
        """
        Internal helper method to load tasks.
        Returns a list of Task objects or an empty list if file not found/corrupted.
        """
        if not os.path.exists(project_path):
            print(f"FileManager: No task file found at '{project_path}'. Returning empty list.")
            return []

        if os.path.getsize(project_path) == 0:
            print(f"FileManager: The task file '{project_path}' is empty. Returning empty list.")
            return []

        try:
            with open(project_path, 'rb') as file:
                loaded_data: Any = pickle.load(file)
                # print(f"FileManager: Successfully loaded tasks from '{project_path}'.") # Removed for less verbosity during internal call

                # Perform type validation after successful load
                if not isinstance(loaded_data, list):
                    print(f"WARNING: Loaded data from '{project_path}' is not a list ({type(loaded_data).__name__}). Returning empty list.")
                    return []
                if not all(isinstance(item, TS) for item in loaded_data):
                    print(f"WARNING: Not all items in '{project_path}' are Task objects. Data might be corrupted. Returning empty list.")
                    return []

                return loaded_data
        except (EOFError, pickle.UnpicklingError):
            print(f"ERROR: Ran out of input or corrupted file while reading '{project_path}'. Returning empty list.")
            return []
        except Exception as e:
            print(f"FileManager: An unexpected error occurred while loading '{project_path}': {e}. Returning empty list.")
            return []

    @staticmethod
    def _save_tasks_internal(project_path: str, tasks_list: List[TS]) -> None:
        """
        Internal helper method to save tasks.
        Ensures directory exists and saves the list.
        """
        try:
            target_directory = os.path.dirname(project_path)
            if target_directory:
                os.makedirs(target_directory, exist_ok=True)

            with open(project_path, 'wb') as file:
                pickle.dump(tasks_list, file)
            # print(f"FileManager: Tasks saved successfully to '{project_path}'.") # Removed for less verbosity
        except Exception as e:
            print(f"ERROR: Failed to save tasks to '{project_path}': {e}")

    # Adds a new task to the project
    # No CLI, just logic
    @staticmethod
    def add_task(task_title: str, project_path: str):
        new_task = TS(task_title)
        tasks: List[TS] = TasksHandler._load_tasks_internal(project_path)
        tasks.append(new_task)
        TasksHandler._save_tasks_internal(project_path, tasks)
        return

    # Adds a new task to the project WITH UI
    @staticmethod
    def add_task_cli(project_path: str):
        print(f"task_handler: Current project path is '{project_path}'.")

        title = input("Input new task title: ").strip()
        if not title:
            print("Task title cannot be empty. Task not added.")
            return

        new_task = TS(title)

        # Use the internal load method
        tasks: List[TS] = TasksHandler._load_tasks_internal(project_path)

        tasks.append(new_task)
        print(f"task_handler: Appended new task: '{new_task.title}'.")

        # Use the internal save method
        TasksHandler._save_tasks_internal(project_path, tasks)
        print(f"task_handler: Tasks successfully saved back to '{project_path}'.") # Specific message for add_task
        return


    @staticmethod
    def list_tasks(project_path: str):
        tasks: List[TS] = TasksHandler._load_tasks_internal(project_path)

        if not tasks:
            print("No tasks up to now :D")
            return

        print("\n--- Your Tasks ---")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task.title}") #({'Completed' if task.completed else 'Pending'})") # More detailed print
        print("Printed all the tasks!")


    @staticmethod
    def delete_task(project_path: str):
        print(f"task_handler.py: started: .delete_task for project '{project_path}'")
        tasks: List[TS] = TasksHandler._load_tasks_internal(project_path)

        if not tasks:
            print("No tasks to delete. The list is empty.")
            return

        # Display tasks with numbers for selection
        print("\n--- Current Tasks to Delete ---")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task.title}") #({'Completed' if task.completed else 'Pending'})")
        print("-------------------------------")

        while True:
            selection_str = input("Enter the number of the task to delete (or 'c' to cancel): ").strip().lower()

            if selection_str == 'c':
                print("Task deletion cancelled.")
                return

            try:
                task_index = int(selection_str) - 1 # Convert to 0-based index
                if 0 <= task_index < len(tasks):
                    deleted_task = tasks.pop(task_index) # Remove the task from the list
                    print(f"Task '{deleted_task.title}' has been deleted.")

                    # Save the modified list back to the file
                    TasksHandler._save_tasks_internal(project_path, tasks)
                    print("Updated tasks saved successfully.")
                    return # Exit the loop and method after successful deletion
                else:
                    print("Invalid task number. Please enter a number within the list range.")
            except ValueError:
                print("Invalid input. Please enter a number or 'c' to cancel.")
            except Exception as e:
                print(f"An unexpected error occurred during deletion: {e}")
                return # Exit on unexpected error
