from .bases import DotloopObject
from .task import Task


class TaskList(DotloopObject, id_field='task_list_id'):
    @property
    def task(self):
        return Task(parent=self)

    def get(self):
        return self.fetch('get')
