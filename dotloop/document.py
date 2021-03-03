from urllib.parse import urljoin

from .bases import BASE_API_URL, AsyncGetAble, AsyncPostAble, RequestableMixin


class Document(RequestableMixin, AsyncGetAble, AsyncPostAble):
    __slots__ = ['profile_id', 'loop_id', 'folder_id', 'document_id']

    def __init__(self, profile_id: int, loop_id: int, folder_id: int, document_id: int) -> None:
        self.profile_id = profile_id
        self.loop_id = loop_id
        self.folder_id = folder_id
        self.document_id = document_id

    def get_url(self) -> str:
        endpoint = f'profile/{self.profile_id}/loop/{self.loop_id}/folder/{self.folder_id}/document/{self.document_id}'
        return urljoin(BASE_API_URL, endpoint)

    def __str__(self) -> str:
        return f'<Document: profile_id={self.profile_id} loop_id={self.loop_id} folder_id={self.folder_id} document_id={self.document_id}>'


class Documents(RequestableMixin, AsyncGetAble):
    __slots__ = ['profile_id', 'loop_id', 'folder_id']

    def __init__(self, profile_id: int, loop_id: int, folder_id: int) -> None:
        self.profile_id = profile_id
        self.loop_id = loop_id
        self.folder_id = folder_id

    def get_url(self) -> str:
        endpoint = f'profile/{self.profile_id}/loop/{self.loop_id}/folder/{self.folder_id}/document'
        return urljoin(BASE_API_URL, endpoint)

    def __str__(self) -> str:
        return f'<Documents: profile_id={self.profile_id} loop_id={self.loop_id} folder_id={self.folder_id}>'
        