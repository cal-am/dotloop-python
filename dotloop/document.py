from .bases import DotloopObject


class Document(DotloopObject, id_field='document_id'):
    def get(self):
        # Accept: application/json
        return self.fetch('get')

    def post(self):
        return super().post()
