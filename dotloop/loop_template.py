from .bases import DotloopObject


class LoopTemplate(DotloopObject, id_field='loop_template_id'):
    def get(self):
        return self.fetch('get')
