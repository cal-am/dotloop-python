from urllib.parse import urljoin

from .bases import BASE_API_URL, AsyncGetAble, RequestableMixin


class LoopTemplate(RequestableMixin, AsyncGetAble):
    __slots__ = ['profile_id', 'loop_template_id']

    def __init__(self, profile_id: int, loop_template_id: int) -> None:
        self.profile_id = profile_id
        self.loop_template_id = loop_template_id

    def get_url(self) -> str:
        endpoint = f'profile/{self.profile_id}/loop_template/{self.loop_template_id}'
        return urljoin(BASE_API_URL, endpoint)

    def __str__(self) -> str:
        return f'<LoopTemplate: profile_id={self.profile_id} loop_template_id={self.loop_template_id}>'


class LoopTemplates(RequestableMixin, AsyncGetAble):
    __slots__ = ['profile_id']

    def __init__(self, profile_id: int) -> None:
        self.profile_id = profile_id

    def get_url(self) -> str:
        endpoint = f'profile/{self.profile_id}/loop_template'
        return urljoin(BASE_API_URL, endpoint)

    def __str__(self) -> str:
        return f'<LoopTemplates: profile_id={self.profile_id}>'
