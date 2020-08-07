from .bases import DotloopObject


class LoopTemplate(DotloopObject, id_field='loop_template_id'):
    def get(self):
        endpoint = f'profile/{self.profile_id}/loop-template'
        if self.loop_template_id is not None:
            endpoint += f'/{self.loop_template_id}'
        return self.fetch(endpoint, 'get')