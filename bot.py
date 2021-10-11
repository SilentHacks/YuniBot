import asyncio

import discord
from discord.ext import commands

from lib.config import DEFAULT_PREFIX, DISCORD_TOKEN, SLASH_GUILD
from lib.YuniBot import YuniBot

# Handling intents
intents = discord.Intents.default()

default_prefixes = [DEFAULT_PREFIX, DEFAULT_PREFIX.upper()]

cog_extensions = ['setup', 'webserver']


def determine_prefix(discord_bot, message):
    return commands.when_mentioned_or(*default_prefixes)(discord_bot, message)


bot = YuniBot(command_prefix=determine_prefix, case_insensitive=True, intents=intents, slash_guild=SLASH_GUILD)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.__version__)
    print('------')

    guild = bot.get_guild(SLASH_GUILD)
    await bot.register_application_commands(guild=guild)


@bot.event
async def on_command_error(error):
    error = getattr(error, "original", error)
    if isinstance(error, commands.CommandNotFound):
        pass
    elif isinstance(error, commands.MissingRequiredArgument):
        pass
    elif isinstance(error, commands.BadArgument):
        pass
    elif isinstance(error, commands.BadUnionArgument):
        pass
    elif isinstance(error, discord.Forbidden):
        pass
    elif isinstance(error, commands.MissingRole):
        pass
    elif isinstance(error, commands.MissingPermissions):
        pass
    elif isinstance(error, TimeoutError):
        pass
    elif isinstance(error, asyncio.TimeoutError):
        pass
    elif isinstance(error, commands.errors.NoPrivateMessage):
        pass


@bot.command(aliases=['reload'])
@commands.is_owner()
async def reload_cog(ctx, cog: str):
    try:
        bot.reload_extension(f'cogs.{cog}')
    except Exception as e:
        await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
    else:
        await ctx.send('**`SUCCESS`**')


if __name__ == '__main__':
    for extension in cog_extensions:
        bot.load_extension(f'cogs.{extension}')

    try:
        bot.loop.run_until_complete(bot.start(DISCORD_TOKEN))
    except KeyboardInterrupt:
        for task in asyncio.all_tasks(loop=bot.loop):
            print(task.__repr__())
            task.cancel()
        bot.loop.run_until_complete(bot.close())
    finally:
        bot.loop.close()
