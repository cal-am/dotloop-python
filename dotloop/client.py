import requests

from .account import Account
from .bases import DotloopObject, EndpointDirectory
from .contact import Contact
from .profile import Profile


class Client:
    endpoint_directory = EndpointDirectory
    
    def __init__(self, access_token):
        self.session = requests.Session()
        self.access_token = access_token

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
        self.session.headers.update(self.headers)

    @property
    def headers(self):
        return {
            'Authorization': f'Bearer {self.access_token}'
        }

    @property
    def account(self):
        return Account(parent=self)

    @property
    def profile(self):
        return Profile(parent=self)

    @property
    def contact(self):
        return Contact(parent=self)
