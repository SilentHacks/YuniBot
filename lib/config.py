import os

from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
UCL_CLIENT_ID = os.getenv('UCL_CLIENT_ID')
UCL_CLIENT_SECRET = os.getenv('CLIENT_SECRET')

DEFAULT_PREFIX = 'y!'
UCL_AUTH_URL = f'https://uclapi.com/oauth/authorise?client_id={UCL_CLIENT_ID}&state=727'
SLASH_GUILD = 706398438937460796
