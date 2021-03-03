from urllib.parse import urljoin

from .bases import BASE_API_URL, AsyncGetAble, RequestableMixin


class Task(RequestableMixin, AsyncGetAble):
    __slots__ = ['profile_id', 'loop_id', 'task_list_id', 'task_id']

    def __init__(self, profile_id: int, loop_id: int, task_list_id: int, task_id: int) -> None:
        self.profile_id = profile_id
        self.loop_id = loop_id
        self.task_list_id = task_list_id
        self.task_id = task_id

    def get_url(self) -> str:
        endpoint = f'profile/{self.profile_id}/loop/{self.loop_id}/task_list/{self.task_list_id}/task/{self.task_id}'
        return urljoin(BASE_API_URL, endpoint)

    def __str__(self) -> str:
        return f'<Task: profile_id={self.profile_id} loop_id={self.loop_id} task_list_id={self.task_list_id} task_id={self.task_id}>'


class Tasks(RequestableMixin, AsyncGetAble):
    __slots__ = ['profile_id', 'loop_id', 'task_list_id']

    def __init__(self, profile_id: int, loop_id: int, task_list_id: int) -> None:
        self.profile_id = profile_id
        self.loop_id = loop_id
        self.task_list_id = task_list_id

    def get_url(self) -> str:
        endpoint = f'profile/{self.profile_id}/loop/{self.loop_id}/task_list/{self.task_list_id}/task'
        return urljoin(BASE_API_URL, endpoint)

    def __str__(self) -> str:
        return f'<Tasks: profile_id={self.profile_id} loop_id={self.loop_id} task_list_id={self.task_list_id}>'
