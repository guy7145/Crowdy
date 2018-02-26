import urllib
from urllib.request import urlopen, Request

friendly_user_agent = \
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'


def make_safe_url(url):
    return urllib.parse.quote(url, safe='$-_.+!*\'(),;/?:@=&%')


def make_headers_with_user_agent(headers):
    if headers is None:
        headers = dict()
    headers['User-Agent'] = friendly_user_agent
    return headers


def fetch_url(url, headers=None, return_bytes=False):
    # log('fetching {}'.format(url))
    headers = make_headers_with_user_agent(headers)
    req = Request(url, headers=headers)
    with urlopen(req) as page:
        response = page.read()
    if return_bytes:
        return response
    else:
        return str(response)
