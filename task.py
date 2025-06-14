class Task:
    title = None
    descryption = None

    def __init__(self, title):
        self.title = title

    def print_task(self):
        print(self.title)
        print()
        print(self.descryption)
        print()
