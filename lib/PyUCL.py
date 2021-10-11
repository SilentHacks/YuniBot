import asyncio

import aiohttp


class PyUCL:

    client_id: str = None
    client_secret: str = None
    code: str = None
    token: str = None
    session: aiohttp.ClientSession = None
    loop: asyncio.AbstractEventLoop = None

    def __init__(self, token: str):
        """:meta private:"""
        self.token = token

    @classmethod
    async def create(cls, client_id: str, client_secret: str, code: str, session: aiohttp.ClientSession = None):
        cls.loop = asyncio.get_running_loop()
        if session is None:
            cls.session = aiohttp.ClientSession(loop=cls.loop)

        params = {
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code
        }

        async with cls.session.get("https://uclapi.com/oauth/token", params=params) as r:
            resp = await r.json()
            if r.status != 200:
                raise ValueError(resp.get('error'))

        return cls(resp.get('token'))

    async def get_personal_timetable(self, date: str = None) -> dict:
        """
        Fetches the personal timetable for the user
        Args:
            date (str): Optional date arg to filter entries by

        Returns
        --------
        :class:`dict`
            A dict of the response.
        """

        params = {'client_secret': self.token}
        if date:
            params['date'] = date

        async with self.session.get('https://uclapi.com/timetable/personal', params=params) as r:
            if r.status == 200:
                resp = await r.json()
            else:
                raise ValueError('Invalid token passed')

        return resp
