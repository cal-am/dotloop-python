from .bases import DotloopObject


class Account(DotloopObject):
    def get(self):
        return self.fetch('get')
