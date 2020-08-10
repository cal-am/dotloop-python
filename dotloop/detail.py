from .bases import DotloopObject


class Detail(DotloopObject):
    def get(self, **kwargs):
        return self.fetch('get', json=kwargs)

    def patch(self, **kwargs):
        return self.fetch('patch', json=kwargs)