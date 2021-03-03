from urllib.parse import urljoin

from .bases import BASE_API_URL, RequestableMixin, AsyncGetAble


class Account(RequestableMixin, AsyncGetAble):
    __slots__ = []

    def get_url(self) -> str:
        return urljoin(BASE_API_URL, 'account')

    def __str__(self) -> str:
        return '<Account>'
