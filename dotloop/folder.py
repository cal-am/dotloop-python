from .bases import DotloopObject
from .document import Document


class Folder(DotloopObject, id_field='folder_id'):
    @property
    def document(self):
        return Document(parent=self)

    def get(self, **kwargs):
        return self.fetch('get', params=kwargs)

    def patch(self, **kwargs):
        return self.fetch('patch', json=kwargs)

    def post(self, **kwargs):
        return self.fetch('post', json=kwargs)
