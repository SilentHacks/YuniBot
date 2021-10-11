import asyncio

import aiohttp


class PyUCL:

    token: str = None
    session: aiohttp.ClientSession = None

    def __init__(self, token: str, session: aiohttp.ClientSession = None):
        """:meta private:"""

        self.token = token
        self.loop = asyncio.get_running_loop()
        if session is not None:
            self.session = aiohttp.ClientSession(loop=self.loop)

    def get_personal_timetable(self, date: str = None) -> dict:
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
