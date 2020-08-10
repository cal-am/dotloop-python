from urllib.parse import urljoin

from .bases import DotloopObject


class Contact(DotloopObject, id_field='contact_id'):
    def delete(self):
        return self.fetch('delete')

    def get(self, **kwargs):
        return self.fetch('get', params=kwargs)

    def patch(self, **kwargs):
        return self.fetch('patch', json=kwargs)

    def post(self, **kwargs):
        return self.fetch('post', json=kwargs)
