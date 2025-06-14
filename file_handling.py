import pickle

class FileHandling:

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
                            
