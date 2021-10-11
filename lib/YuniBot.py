from discord.ext import commands


class YuniBot(commands.Bot):

    def __init__(self, *args, **kwargs):
        self.slash_guild = kwargs.pop('slash_guild')
        super().__init__(*args, **kwargs)

    async def start(self, token: str, *, reconnect: bool = True) -> None:
        await super().start(token=token, reconnect=reconnect)
