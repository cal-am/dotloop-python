from dotloop.authenticate import url_for_authentication, BASE_AUTH_URL
from . import Test

def test_url_for_authentication():
    url = url_for_authentication('client-id', redirect_uri='http://example.com/redirect/')
    assert url == 'https://auth.dotloop.com/oauth/authorize?client_id=client-id&redirect_uri=http%3A%2F%2Fexample.com%2Fredirect%2F&redirect_on_deny=false', f'URL ({url}) is not correct.'


tests = [
    Test(func=test_url_for_authentication),
]
