from base64 import b64encode
from typing import Optional
from urllib.parse import urlencode, urljoin

import aiohttp


__all__ = [
    'url_for_authentication',
    'acquire_access_and_refresh_tokens',
    'refresh_access_token',
    'revoke_access'
]

# Constants
BASE_AUTH_URL = 'https://auth.dotloop.com/oauth/'


def url_for_authentication(client_id: str, redirect_uri: str, state: Optional[str] = None, redirect_on_deny: bool = False) -> str:
    params = {
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'redirect_on_deny': 'true' if redirect_on_deny else 'false'
    }

    if state is not None:
        params['state'] = state

    return urljoin(BASE_AUTH_URL, 'authorize?' + urlencode(params))

async def acquire_access_and_refresh_tokens(client: aiohttp.ClientSession, client_id: str, client_secret: str, code: str, redirect_uri: str, state: Optional[str] = None) -> aiohttp.ClientResponse:
    params = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'state': state
    }

    headers = {
        'Authorization': 'Basic ' + b64encode(f'{client_id}:{client_secret}'.encode()).decode()
    }

    url = urljoin(BASE_AUTH_URL, 'token')

    return await client.post(url, params=params, headers=headers)

async def refresh_access_token(client: aiohttp.ClientSession, client_id: str, client_secret: str, refresh_token: str) -> aiohttp.ClientResponse:
    params = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }

    headers = {
        'Authorization': 'Basic ' + b64encode(f'{client_id}:{client_secret}'.encode()).decode()
    }

    url = urljoin(BASE_AUTH_URL, 'token')

    return await client.post(url, params=params, headers=headers)

async def revoke_access(client: aiohttp.ClientSession, access_token: str) -> aiohttp.ClientResponse:
    params = {
        'token': access_token
    }

    url = urljoin(BASE_AUTH_URL, 'token/revoke')

    return await client.post(url, params=params)
