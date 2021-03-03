from urllib.parse import urljoin

from .bases import DotloopObject
from .loop import Loop
from .loop_it import LoopIt
from .loop_template import LoopTemplate


class Profile(DotloopObject, id_field='profile_id'):
    @property
    def loop(self):
        return Loop(parent=self)

    @property
    def loop_it(self):
        return LoopIt(parent=self)

    @property
    def loop_template(self):
        return LoopTemplate(parent=self)

    def get(self):
        return self.fetch('get')

    def post(self, **kwargs):
        return self.fetch('post', json=kwargs)

    def patch(self, **kwargs):
        return self.fetch('patch', json=kwargs)
