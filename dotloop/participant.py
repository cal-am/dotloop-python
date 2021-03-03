from urllib.parse import urljoin

from .bases import (BASE_API_URL, AsyncDeleteAble, AsyncGetAble,
                    AsyncPatchAble, AsyncPostAble, RequestableMixin)


class Participant(RequestableMixin, AsyncGetAble, AsyncPostAble, AsyncPatchAble, AsyncDeleteAble):
    __slots__ = ['profile_id', 'loop_id', 'participant_id']

    def __init__(self, profile_id: int, loop_id: int, participant_id: int) -> None:
        self.profile_id = profile_id
        self.loop_id = loop_id
        self.participant_id = participant_id

    def get_url(self) -> str:
        endpoint = f'profile/{self.profile_id}/loop/{self.loop_id}/participant/{self.participant_id}'
        return urljoin(BASE_API_URL, endpoint)

    def __str__(self) -> str:
        return f'<Participant: profile_id={self.profile_id} loop_id={self.loop_id} participant_id={self.participant_id}>'


class Participants(RequestableMixin, AsyncGetAble):
    __slots__ = ['profile_id', 'loop_id']

    def __init__(self, profile_id: int, loop_id: int) -> None:
        self.profile_id = profile_id
        self.loop_id = loop_id

    def get_url(self) -> str:
        endpoint = f'profile/{self.profile_id}/loop/{self.loop_id}/participant'
        return urljoin(BASE_API_URL, endpoint)

    def __str__(self) -> str:
        return f'<Participants: profile_id={self.profile_id} loop_id={self.loop_id}>'
