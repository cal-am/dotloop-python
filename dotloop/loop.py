from urllib.parse import urljoin

from .activity import Activity
from .bases import DotloopObject
from .detail import Detail
from .folder import Folder
from .participant import Participant
from .task_list import TaskList


class Loop(DotloopObject, id_field='loop_id'):
    @property
    def activity(self):
        return Activity(parent=self)

    @property
    def detail(self):
        return Detail(parent=self)

    @property
    def folder(self):
        return Folder(parent=self)

    @property
    def participant(self):
        return Participant(parent=self)

    @property
    def task_list(self):
        return TaskList(parent=self)

    def get(self, **kwargs):
        return self.fetch('get', params=kwargs)

    def post(self, **kwargs):
        return self.fetch('post', json=kwargs)

    def patch(self, **kwargs):
        return self.fetch('patch', json=kwargs)
