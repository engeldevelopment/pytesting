class TaskWasDoned(Exception):
    pass

class Task:
    def __init__(self, name):
        self.name = name
        self.done = False

    def mark_as_done(self):
        if self.is_done:
            raise TaskWasDoned()
        self.done = True

    @property
    def is_done(self):
        return self.done
