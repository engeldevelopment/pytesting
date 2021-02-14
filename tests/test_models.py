import pytest


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


class TestTask:

    def test_can_mark_as_done(self):
        task = Task(name="Dev")

        task.mark_as_done()

        assert task.is_done

    def test_if_it_is_doned_cannot_it_mark_as_done(self):
        task = Task(name="It's not done")

        task.mark_as_done()
        with pytest.raises(TaskWasDoned):
            task.mark_as_done()

