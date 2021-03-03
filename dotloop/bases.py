from typing import Dict, Optional, Union

import aiohttp
import requests


BASE_API_URL = 'https://api-gateway.dotloop.com/public/v2/'


class RequestableMixin:
    def get_url(self) -> str:
        """Stub function for creating a URL from object's attributes."""
        pass


class AsyncGetAble:
    async def get(self: RequestableMixin, session: aiohttp.ClientSession, params: Optional[Dict[str, str]] = None) -> aiohttp.ClientResponse:
        params = params if params is not None else {}
        return await session.get(self.get_url(), params=params)


class AsyncDeleteAble:
    async def delete(self: RequestableMixin, session: aiohttp.ClientSession) -> aiohttp.ClientResponse:
        return await session.delete(self.get_url())


class AsyncPatchAble:
    async def patch(self: RequestableMixin, session: aiohttp.ClientSession, json: Dict[str, str]) -> aiohttp.ClientResponse:
        return await session.patch(self.get_url(), json=json)


class AsyncPostAble:
    async def post(self: RequestableMixin, session: aiohttp.ClientSession) -> aiohttp.ClientResponse:
        return await session.post(self.get_url())


class SyncGetAble:
    def get(self: RequestableMixin, session: requests.Session, params: Dict[str, str]) -> requests.Response:
        return session.get(self.get_url(), params=params)


class SyncDeleteAble:
    def delete(self: RequestableMixin, session: requests.Session) -> requests.Response:
        return session.delete(self.get_url())


class SyncPatchAble:
    def patch(self: RequestableMixin, session: requests.Session, json: Dict[str, str]) -> requests.Response:
        return session.patch(self.get_url(), json=json)


class SyncPostAble:
    def post(self: RequestableMixin, session: requests.Session, json: Dict[str, str]) -> requests.Response:
        return session.post(self.get_url(), json=json)


def store_access_token(session: Union[requests.Session, aiohttp.ClientSession], access_token: str):
    if isinstance(session, requests.Session):
        session.headers.update({'Authorization': f'Bearer {access_token}'})
    elif isinstance(session, aiohttp.ClientSession):
        session._default_headers.add('Authorization', f'Bearer {access_token}')
    else:
        raise ValueError('`session` must be an instance of either `requests.Session` or `aiohttp.ClientSession`')
