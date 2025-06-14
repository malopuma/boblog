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

        
        
