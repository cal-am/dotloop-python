from urllib.parse import urljoin

from .bases import BASE_API_URL, AsyncGetAble, AsyncPatchAble, RequestableMixin


class Details(RequestableMixin, AsyncGetAble, AsyncPatchAble):
    __slots__ = ['profile_id', 'loop_id']

    def __init__(self, profile_id: int, loop_id: int) -> None:
        self.profile_id = profile_id
        self.loop_id = loop_id

    def get_url(self) -> str:
        endpoint = f'profile/{self.profile_id}/loop/{self.loop_id}/detail'
        return urljoin(BASE_API_URL, endpoint)

    def __str__(self) -> str:
        return '<Details>'