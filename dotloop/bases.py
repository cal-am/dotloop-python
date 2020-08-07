from typing import Dict


class DotloopError(Exception):
    pass


class DotloopObject:
    base_url = 'https://api-gateway.dotloop.com/public/v2/'

    def __init__(self, parent=None):
        self.parent = parent
        if self.id_field is not None:
            setattr(self, self.id_field, None)

    def __init_subclass__(cls, id_field=None, **kwargs):
        cls.id_field = id_field
        super().__init_subclass__(**kwargs)

    def __call__(self, id_value):
        new_obj = self.__class__(parent=self.parent)
        attr = getattr(self.__class__, 'id_field')
        if attr is not None:
            setattr(new_obj, attr, id_value)
        return new_obj

    def __str__(self):
        try:
            if self.id_field is not None:
                return f"<{self.__class__.__name__}({self.id_field}={getattr(self, self.id_field)})>"
            else:
                return f"<{self.__class__.__name__}>"
        except AttributeError:
            return '<DotloopObject>'

    def __repr__(self):
        return str(self)

    def __getattr__(self, name: str):
        if self.parent is not None:
            return getattr(self.parent, name)
        else:
            raise AttributeError

    def delete(self, *args, **kwargs) -> Dict:
        return NotImplemented

    def get(self, *args, **kwargs) -> Dict:
        return NotImplemented

    def patch(self, *args, **kwargs) -> Dict:
        return NotImplemented

    def post(self, *args, **kwargs) -> Dict:
        return NotImplemented

    def fetch(self, endpoint, method, **kwargs) -> Dict:
        response = getattr(self.session, method)(
            urljoin(self.base_url, endpoint),
            **kwargs
        )
        
        if response.ok:
            return response.json()
        else:
            raise DotloopError(response.status_code, response.content.decode())
