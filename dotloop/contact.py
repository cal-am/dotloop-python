from urllib.parse import urljoin

from .bases import (BASE_API_URL, AsyncDeleteAble, AsyncGetAble,
                    AsyncPatchAble, AsyncPostAble, RequestableMixin)


class Contact(RequestableMixin, AsyncGetAble, AsyncPostAble, AsyncPatchAble, AsyncDeleteAble):
    __slots__ = ['contact_id']

    def __init__(self, contact_id: int) -> None:
        self.contact_id = contact_id

    def get_url(self) -> str:
        endpoint = f'contact/{self.contact_id}'
        return urljoin(BASE_API_URL, endpoint)

    def __str__(self) -> str:
        return f'<Contact: contact_id={self.contact_id}>'


class Contacts(RequestableMixin, AsyncGetAble):
    __slots__ = []

    def get_url(self) -> str:
        return urljoin(BASE_API_URL, 'contact')

    def __str__(self) -> str:
        return '<Contacts>'
