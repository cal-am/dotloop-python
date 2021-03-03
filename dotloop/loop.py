from urllib.parse import urljoin

from .activity import Activities
from .bases import (BASE_API_URL, AsyncGetAble, AsyncPatchAble, AsyncPostAble,
                    RequestableMixin)
from .detail import Details
from .folder import Folder, Folders
from .participant import Participant, Participants
from .task_list import TaskList, TaskLists


class Loop(RequestableMixin, AsyncGetAble, AsyncPostAble, AsyncPatchAble):
    __slots__ = ['profile_id', 'loop_id']

    def __init__(self, profile_id: int, loop_id: int) -> None:
        self.profile_id = profile_id
        self.loop_id = loop_id

    def get_url(self) -> str:
        endpoint = f'profile/{self.profile_id}/loop/{self.loop_id}'
        return urljoin(BASE_API_URL, endpoint)

    @property
    def activities(self) -> Activities:
        return Activities(profile_id=self.profile_id, loop_id=self.loop_id)

    @property
    def details(self) -> Details:
        return Details(profile_id=self.profile_id, loop_id=self.loop_id)

    def folder(self, folder_id) -> Folder:
        return Folder(profile_id=self.profile_id, loop_id=self.loop_id, folder_id=folder_id)

    @property
    def folders(self) -> Folders:
        return Folders(profile_id=self.profile_id, loop_id=self.loop_id)

    def participant(self, participant_id: int) -> Participant:
        return Participant(profile_id=self.profile_id, loop_id=self.loop_id, participant_id=participant_id)

    @property
    def participants(self) -> Participants:
        return Participants(profile_id=self.profile_id, loop_id=self.loop_id)

    def task_list(self, task_list_id: int) -> TaskList:
        return TaskList(profile_id=self.profile_id, loop_id=self.loop_id, task_list_id=task_list_id)

    @property
    def task_lists(self) -> TaskLists:
        return TaskLists(profile_id=self.profile_id, loop_id=self.loop_id)

    def __str__(self) -> str:
        return f'<Loop: profile_id={self.profile_id} loop_id={self.loop_id}>'


class Loops(RequestableMixin, AsyncGetAble):
    __slots__ = ['profile_id']

    def __init__(self, profile_id: int) -> None:
        self.profile_id = profile_id

    def get_url(self) -> str:
        endpoint = f'profile/{self.profile_id}/loop'
        return urljoin(BASE_API_URL, endpoint)

    def __str__(self) -> str:
        return f'<Loops: profile_id={self.profile_id}>'
