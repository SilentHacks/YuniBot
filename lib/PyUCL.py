import asyncio

import aiohttp


class PyUCL:

    client_id: str = None
    client_secret: str = None
    code: str = None
    session: aiohttp.ClientSession = None

    def __init__(self, client_id: str, client_secret: str, code: str, session: aiohttp.ClientSession = None):
        """:meta private:"""

        self.client_id = client_id
        self.client_secret = client_secret
        self.code = code
        self.loop = asyncio.get_running_loop()
        if session is not None:
            self.session = aiohttp.ClientSession(loop=self.loop)

        self.token = self.loop.run_until_complete(self._get_token())

    async def _get_token(self):
        params = {
            "client_id": self.client_id,
            "client_secret": "secret",
            "code": self.code
        }
        async with self.session.get("https://uclapi.com/oauth/token", params=params) as r:
            resp = await r.json()
            if r.status != 200:
                raise ValueError(resp.get('error'))

        return resp.get('token')

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
