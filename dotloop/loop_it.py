from .bases import DotloopObject


class LoopIt(DotloopObject):
    def post(self, **kwargs):
        return self.fetch('post', json=kwargs, params={
            'profile_id': self.profile_id
        })
