from task import Task

class Control:

    @staticmethod
    def create_new_task():
        new_task_title = input("Input new task: ")
        task1 = Task(new_task_title)
        print("Created new task: ", task1.title)
