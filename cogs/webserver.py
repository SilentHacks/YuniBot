from aiohttp import web
from discord.ext import commands

from lib.config import UCL_CLIENT_ID


class Webserver(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._webserver = None
        self.webhook_path = '/callback'
        self.webhook_port = 5000
        self.webhook_auth = UCL_CLIENT_ID
        self._is_closed = False

        self.webhook_task = self.bot.loop.create_task(self._webhook())

    def cog_unload(self):
        self.bot.loop.run_until_complete(self._close())

    @commands.Cog.listener()
    async def on_callback(self, data):
        print(data)

    async def _webhook(self):
        async def webhook_handler(request):
            print(1, request)
            req_auth = request.headers.get('client_id')
            if self.webhook_auth == req_auth:
                data = await request.json()
                if data.get('result'):
                    event_name = 'callback'
                else:
                    return
                self.bot.dispatch(event_name, data)
                return web.Response(status=200)
            else:
                return web.Response(status=401)

        app = web.Application(loop=self.bot.loop)
        app.router.add_post(self.webhook_path, webhook_handler)
        runner = web.AppRunner(app)
        await runner.setup()
        self._webserver = web.TCPSite(runner, '0.0.0.0', self.webhook_port)
        await self._webserver.start()

    async def _close(self):
        if self._is_closed:
            return
        else:
            await self._webserver.stop()
            self.webhook_task.cancel()
            self._is_closed = True


def setup(bot):
    bot.add_cog(Webserver(bot))
