from discord.ext import commands

from lib.config import UCL_AUTH_URL

# Include setting up of:
# - Roles for on/off campus
# - OAuth verification
# - Opt in/out
# - Manual role override


class Setup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(add_slash_command=True)
    async def verify(self, ctx: commands.Context):
        """Verify yourself using UCL API OAuth"""
        await ctx.send(content=UCL_AUTH_URL)


def setup(bot):
    bot.add_cog(Setup(bot))
