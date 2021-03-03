from urllib.parse import urljoin

from .bases import BASE_API_URL, AsyncGetAble, RequestableMixin


class Activities(RequestableMixin, AsyncGetAble):
    __slots__ = ['profile_id', 'loop_id']

    def __init__(self, profile_id: int, loop_id: int) -> None:
        self.profile_id = profile_id
        self.loop_id = loop_id

    def get_url(self) -> str:
        endpoint = f'profile/{self.profile_id}/loop/{self.loop_id}/activity'
        return urljoin(BASE_API_URL, endpoint)

    def __str__(self) -> str:
        return f'<Activities: profile_id={self.profile_id} loop_id={self.loop_id}>'
