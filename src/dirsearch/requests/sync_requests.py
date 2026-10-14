import fake_useragent
import requests
from requests import Response

request = requests
session = requests.Session()

"""
Sync Get By Request
:param uri uri
:param params params
:param data data
:param headers headers
:return response | None
"""
def getByRequests(
        uri: str,
        params: dict | None = None,
        data: dict | None = None,
        headers = None
) -> Response:
    if headers is None: headers = {"User-Agent": fake_useragent.UserAgent().random}
    return request.get(
        url=uri,
        headers=headers,
        params=params,
        data=data
    )

"""
Sync Post By Request
:param uri uri
:param params params
:param data data
:param headers headers
:return response | None
"""
def postByRequests(
        uri: str,
        data: dict | None = None,
        params: dict | None = None,
        headers = None
) -> Response:
    if headers is None: headers = {"User-Agent": fake_useragent.UserAgent().random}
    return request.post(
        url=uri,
        headers=headers,
        params=params,
        data=data
    )

"""
Sync Get By Session
:param uri uri
:param params params
:param data data
:param headers headers
:return response | None
"""
def getBySession(
        uri: str,
        params: dict | None = None,
        data: dict | None = None,
        headers = None
) -> Response:
    if headers is None: headers = {"User-Agent": fake_useragent.UserAgent().random}
    return session.get(
        url=uri,
        headers=headers,
        params=params,
        data=data
    )

"""
Sync Post By Session
:param uri uri
:param params params
:param data data
:param headers headers
:return response | None
"""
def postBySession(
        uri: str,
        data: dict | None = None,
        params: dict | None = None,
        headers = None
) -> Response:
    if headers is None: headers = {"User-Agent": fake_useragent.UserAgent().random}
    return session.post(
        url=uri,
        headers=headers,
        params=params,
        data=data
    )