class Task:
    task_to_do = ""

    def __init__(self, task_to_do):
        self.task_to_do = task_to_do

    def print_task(self):
        print(self.task_to_do)
