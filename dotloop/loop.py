from .bases import DotloopObject
from .activity import Activity
from .detail import Detail
from .folder import Folder
from .participant import Participant
from .task_list import TaskList
from urllib.parse import urljoin


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

    def get(self):
        endpoint = f'profile/{self.profile_id}/loop'
        if self.loop_id is not None:
            endpoint += f'/{self.loop_id}'

        return self.fetch(endpoint, 'get')

    def post(self, **kwargs):
        endpoint = f'profile/{self.profile_id}/loop'
        return self.fetch(endpoint, 'post', json=kwargs)

    def patch(self, **kwargs):
        endpoint = f'profile/{self.profile_id}/loop/{self.loop_id}'
        return self.fetch(endpoint, 'patch', json=kwargs)