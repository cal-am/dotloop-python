from json import JSONDecodeError
from typing import Dict
from urllib.parse import urljoin


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

    def fetch(self, method, **kwargs) -> Dict:
        endpoint: str = self.endpoint_directory[self.__class__.__name__, method, getattr(self, self.id_field or 'id_field')]
        endpoint = endpoint.format(self)

        if method not in {'delete', 'get', 'patch', 'post'}:
            raise ValueError(f'HTTP allowed methods are ["delete", "get", "patch", "post"], got "{method}".')

        response = getattr(self.session, method)(
            urljoin(self.base_url, endpoint),
            **kwargs
        )
        try:
            return response.json()
        except JSONDecodeError as e:
            return {'error': 'JSONDecodeError', 'message': f'{str(e)}: {response.content.decode()}', 'status': response.status_code}


class NotNoneClass:
    def __eq__(self, other):
        return other is not None

    def __str__(self):
        return 'NotNone'

    def __repr__(self):
        return str(self)


NotNone = NotNoneClass()


class EndpointDirectoryClass:
    @staticmethod
    def first(iterable):
        try:
            return next(iterable)
        except StopIteration:
            raise KeyError(str(iterable))

    items = [
        # [(object, method, id_value), endpointToFormat]
        [('LoopIt', 'post', None), 'loop-it'],
        [('Account', 'get', None), 'account'],
        [('Profile', 'get', None), 'profile'],
        [('Profile', 'get', NotNone), 'profile/{0.profile_id}'],
        [('Profile', 'post', None), 'profile'],
        [('Profile', 'patch', NotNone), 'profile/{0.profile_id}'],
        [('Loop', 'get', None), 'profile/{0.profile_id}/loop'],
        [('Loop', 'get', NotNone), 'profile/{0.profile_id}/loop/{0.loop_id}'],
        [('Loop', 'get', NotNone), 'profile/{0.profile_id}/loop/{0.loop_id}'],
        [('Loop', 'post', None), 'profile/{0.profile_id}/loop'],
        [('Loop', 'patch', NotNone), 'profile/{0.profile_id}/loop/{0.loop_id}'],
        [('Detail', 'get', None), 'profile/{0.profile_id}/loop/{0.loop_id}/detail'],
        [('Detail', 'patch', None), 'profile/{0.profile_id}/loop/{0.loop_id}/detail'],
        [('Folder', 'get', None), 'profile/{0.profile_id}/loop/{0.loop_id}/folder'],
        [('Folder', 'get', NotNone), 'profile/{0.profile_id}/loop/{0.loop_id}/folder/{0.folder_id}'],
        [('Folder', 'patch', NotNone), 'profile/{0.profile_id}/loop/{0.loop_id}/folder/{0.folder_id}'],
        [('Document', 'get', None), 'profile/{0.profile_id}/loop/{0.loop_id}/folder/{0.folder_id}/document'],
        [('Document', 'get', NotNone), 'profile/{0.profile_id}/loop/{0.loop_id}/folder/{0.folder_id}/document/{0.document_id}'],
        [('Document', 'post', None), 'profile/{0.profile_id}/loop/{0.loop_id}/folder/{0.folder_id}/document'],
        [('Participant', 'get', None), 'profile/{0.profile_id}/loop/{0.loop_id}/participant'],
        [('Participant', 'get', NotNone), 'profile/{0.profile_id}/loop/{0.loop_id}/participant/{0.participant_id}'],
        [('Participant', 'post', None), 'profile/{0.profile_id}/loop/{0.loop_id}/participant'],
        [('Participant', 'patch', NotNone), 'profile/{0.profile_id}/loop/{0.loop_id}/participant/{0.participant_id}'],
        [('Participant', 'delete', NotNone), 'profile/{0.profile_id}/loop/{0.loop_id}/participant/{0.participant_id}'],
        [('TaskList', 'get', None), 'profile/{0.profile_id}/loop/{0.loop_id}/tasklist'],
        [('TaskList', 'get', NotNone), 'profile/{0.profile_id}/loop/{0.loop_id}/tasklist/{0.task_list_id}'],
        [('Task', 'get', None), 'profile/{0.profile_id}/loop/{0.loop_id}/tasklist/{0.task_list_id}/task'],
        [('Task', 'get', NotNone), 'profile/{0.profile_id}/loop/{0.loop_id}/tasklist/{0.task_list_id}/task/{0.task_id}'],
        [('Activity', 'get', None), 'profile/{0.profile_id}/loop/{0.loop_id}/activity'],
        [('Contact', 'get', None), 'contact'],
        [('Contact', 'get', NotNone), 'contact/{0.contact_id}'],
        [('Contact', 'post', None), 'contact'],
        [('Contact', 'patch', NotNone), 'contact/{0.contact_id}'],
        [('Contact', 'delete', NotNone), 'contact/{0.contact_id}'],
        [('LoopTemplate', 'get', None), 'profile/{0.profile_id}/loop-template'],
        [('LoopTemplate', 'get', NotNone), 'profile/{0.profile_id}/loop-template/{0.loop_template_id}'],
    ]

    def __getitem__(self, key):
        return self.first(endpoint for loc, endpoint in self.items if loc == key)


EndpointDirectory = EndpointDirectoryClass()
