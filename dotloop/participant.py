from .bases import DotloopObject


class Participant(DotloopObject, id_field='participant_id'):
    def delete(self):
        return self.fetch('delete')

    def get(self):
        return self.fetch('get')

    def patch(self, **kwargs):
        return self.fetch('patch', json=kwargs)

    def post(self, **kwargs):
        return self.fetch('post', json=kwargs)
