from .bases import DotloopObject


class Task(DotloopObject, id_field='task_id'):
    def get(self):
        return self.fetch('get')
