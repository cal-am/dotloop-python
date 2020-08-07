from .bases import DotloopObject
from .document import Document


class Folder(DotloopObject, id_field='folder_id'):
    @property
    def document(self):
        return Document(parent=self)
