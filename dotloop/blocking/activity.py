from .bases import DotloopObject


class Activity(DotloopObject, id_field='activity_id'):
    def get(self, **kwargs):
        return self.fetch('get', params=kwargs)
