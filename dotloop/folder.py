from urllib.parse import urljoin

from .bases import (BASE_API_URL, AsyncGetAble, AsyncPatchAble, AsyncPostAble,
                    RequestableMixin)
from .document import Document, Documents


class Folder(RequestableMixin, AsyncGetAble, AsyncPostAble, AsyncPatchAble):
    __slots__ = ['profile_id', 'loop_id', 'folder_id']

    def __init__(self, profile_id: int, loop_id: int, folder_id: int) -> None:
        self.profile_id = profile_id
        self.loop_id = loop_id
        self.folder_id = folder_id

    def get_url(self) -> str:
        endpoint = f'profile/{self.profile_id}/loop/{self.loop_id}/folder/{self.folder_id}'
        return urljoin(BASE_API_URL, endpoint)

    def document(self, document_id: int) -> Document:
        return Document(profile_id=self.profile_id, loop_id=self.loop_id, folder_id=self.folder_id, document_id=document_id)

    @property
    def documents(self) -> Documents:
        return Documents(profile_id=self.profile_id, loop_id=self.loop_id, folder_id=self.folder_id)

    def __str__(self) -> str:
        return f'<Folder: profile_id={self.profile_id} loop_id={self.loop_id} folder_id={self.folder_id}>'


class Folders(RequestableMixin, AsyncGetAble):
    __slots__ = ['profile_id', 'loop_id']

    def __init__(self, profile_id: int, loop_id: int) -> None:
        self.profile_id = profile_id
        self.loop_id = loop_id

    def get_url(self) -> str:
        endpoint = f'profile/{self.profile_id}/loop/{self.loop_id}/folder'
        return urljoin(BASE_API_URL, endpoint)

    def __str__(self) -> str:
        return f'<Folder: profile_id={self.profile_id} loop_id={self.loop_id}>'
        