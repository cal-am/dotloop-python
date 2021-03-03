from typing import Optional
from urllib.parse import urljoin

import aiohttp

from .bases import (BASE_API_URL, AsyncGetAble, AsyncPatchAble, AsyncPostAble,
                    RequestableMixin)
from .loop import Loop, Loops
from .loop_template import LoopTemplate, LoopTemplates


class Profile(RequestableMixin, AsyncGetAble, AsyncPostAble, AsyncPatchAble):
    __slots__ = ['profile_id']

    def __init__(self, profile_id: int) -> None:
        self.profile_id = profile_id

    def get_url(self) -> str:
        endpoint = f'profile/{self.profile_id}'
        return urljoin(BASE_API_URL, endpoint)

    def loop(self, loop_id: int) -> Loop:
        return Loop(profile_id=self.profile_id, loop_id=loop_id)

    @property
    def loops(self) -> Loops:
        return Loops(profile_id=self.profile_id)

    def loop_template(self, loop_template_id: int) -> LoopTemplate:
        return LoopTemplate(profile_id=self.profile_id, loop_template_id=loop_template_id)

    @property
    def loop_templates(self) -> LoopTemplates:
        return LoopTemplates(profile_id=self.profile_id)

    @staticmethod
    async def get_default(session: aiohttp.ClientSession) -> int:
        response = await Profiles().get(session)
        data = await response.json()
        if not 'data' in data:
            raise ValueError(f'Error when fetching profiles: {data}')
        for profile in data['data']:
            if profile.get('default', False):
                return profile['id']
        else:
            if len(data['data']) > 0:
                return data['data'][0]['id']
            else:
                raise IndexError(f'User has no profiles: {data}')

    def __str__(self) -> str:
        return f'<Profile: profile_id={self.profile_id}>'


class Profiles(RequestableMixin, AsyncGetAble):
    __slots__ = []

    def get_url(self) -> str:
        endpoint = f'profile'
        return urljoin(BASE_API_URL, endpoint)

    def __str__(self) -> str:
        return f'<Profiles>'
