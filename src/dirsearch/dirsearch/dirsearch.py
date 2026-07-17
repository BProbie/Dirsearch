import sys
import asyncio
from src.dirsearch.requests import async_requests

"""
The Class of the Dirsearch
"""
class Dirsearch:

    uri = None

    def init(self, args):
        self.uri = args.uri

    async def run(self):
        response = await async_requests.async_post(uri=self.uri, params={}, data={})
        sys.stdout.write(f"{response}\n")
        sys.stdout.flush()

    def main(self, args):
        self.init(args)
        asyncio.run(self.run())