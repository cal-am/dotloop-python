from urllib.parse import urljoin

from .bases import BASE_API_URL, AsyncGetAble, RequestableMixin
from .task import Task, Tasks


class TaskList(RequestableMixin, AsyncGetAble):
    __slots__ = ['profile_id', 'loop_id', 'task_list_id']

    def __init__(self, profile_id: int, loop_id: int, task_list_id: int) -> None:
        self.profile_id = profile_id
        self.loop_id = loop_id
        self.task_list_id = task_list_id

    def get_url(self) -> str:
        endpoint = f'profile/{self.profile_id}/loop/{self.loop_id}/task_list/{self.task_list_id}'
        return urljoin(BASE_API_URL, endpoint)

    def task(self, task_id: int) -> Task:
        return Task(profile_id=self.profile_id, loop_id=self.loop_id, task_list_id=self.task_list_id, task_id=task_id)

    @property
    def tasks(self) -> Tasks:
        return Tasks(profile_id=self.profile_id, loop_id=self.loop_id, task_list_id=self.task_list_id)

    def __str__(self) -> str:
        return f'<TaskList: profile_id={self.profile_id} loop_id={self.loop_id} task_list_id={self.task_list_id}>'


class TaskLists(RequestableMixin, AsyncGetAble):
    __slots__ = ['profile_id', 'loop_id']

    def __init__(self, profile_id: int, loop_id: int) -> None:
        self.profile_id = profile_id
        self.loop_id = loop_id

    def get_url(self) -> str:
        endpoint = f'profile/{self.profile_id}/loop/{self.loop_id}/task_list'
        return urljoin(BASE_API_URL, endpoint)

    def __str__(self) -> str:
        return f'<TaskLists: profile_id={self.profile_id} loop_id={self.loop_id}>'
