import aiohttp
import fake_useragent
from aiohttp import ClientError, ClientResponse, ClientTimeout

"""
Async Get By Session
:param uri uri
:param params params
:param data data
:param headers headers
:param session session
:param timeout timeout
:param attempts attempts
:return: response | None
"""
async def async_get(
        uri: str,
        params: dict,
        data: dict,
        headers: dict | None = None,
        session: aiohttp.ClientSession = None,
        timeout: int = 60,
        attempts: int = 10
) -> ClientResponse | None:
    if headers is None: headers = {"User-Agent": fake_useragent.UserAgent().random}

    if session is not None:
        for attempt in range(attempts):
            try:
                async with session.get(
                        url=uri,
                        params=params,
                        data=data,
                        headers=headers,
                        timeout=ClientTimeout(total=timeout)
                ) as response:
                    response._body = await response.read()
                    response._body_cache = True
                    return response
            except ClientError as clientError:
                if attempt + 1 == attempts:
                    print(f"{clientError}")

    else:
        async with aiohttp.ClientSession() as clientSession:
            for attempt in range(attempts):
                try:
                    async with clientSession.get(
                            url=uri,
                            params=params,
                            data=data,
                            headers=headers,
                            timeout=ClientTimeout(total=timeout)
                    ) as response:
                        response._body = await response.read()
                        response._body_cache = True
                        return response
                except ClientError as clientError:
                    if attempt + 1 == attempts:
                        print(f"{clientError}")

    return None

"""
Async Post By Session
:param uri uri
:param params params
:param data data
:param headers headers
:param session session
:param timeout timeout
:param attempts attempts
:return: response | None
"""
async def async_post(
        uri: str,
        params: dict,
        data: dict,
        headers: dict | None = None,
        session: aiohttp.ClientSession = None,
        timeout: int = 60,
        attempts: int = 10
) -> ClientResponse | None:
    if headers is None: headers = {"User-Agent": fake_useragent.UserAgent().random}

    if session is not None:
        for attempt in range(attempts):
            try:
                async with session.post(
                        url=uri,
                        params=params,
                        data=data,
                        headers=headers,
                        timeout=ClientTimeout(total=timeout)
                ) as response:
                    response._body = await response.read()
                    response._body_cache = True
                    return response
            except ClientError as clientError:
                if attempt + 1 == attempts:
                    print(f"{clientError}")

    else:
        async with aiohttp.ClientSession() as clientSession:
            for attempt in range(attempts):
                try:
                    async with clientSession.post(
                            url=uri,
                            params=params,
                            data=data,
                            headers=headers,
                            timeout=ClientTimeout(total=timeout)
                    ) as response:
                        response._body = await response.read()
                        response._body_cache = True
                        return response
                except ClientError as clientError:
                    if attempt + 1 == attempts:
                        print(f"{clientError}")

    return None