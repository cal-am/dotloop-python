from .bases import DotloopObject, DotloopError
from .loop import Loop
from .loop_it import LoopIt
from .loop_template import LoopTemplate

from urllib.parse import urljoin


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
        endpoint = 'profile'
        if (id_ := getattr(self, self.id_field, None)) is not None:
            endpoint += f'/{id_}'

        return self.fetch(endpoint, 'get')

    def post(self, **kwargs):
        return self.fetch('profile', 'post', json=kwargs)

    def patch(self, **kwargs):
        if (attr := getattr(self, self.id_field, None)) is None:
            raise ValueError(f'{self.id_field} is required')

        return self.fetch(f'profile/{attr}', 'patch', json=kwargs)