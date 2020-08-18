from .bases import DotloopObject


class Detail(DotloopObject):
    def get(self):
        return self.fetch('get')

    def patch(self, **kwargs):
        return self.fetch('patch', json=kwargs)
