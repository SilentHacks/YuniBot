import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

DEFAULT_PREFIX = 'y!'
UCL_AUTH_URL = f'https://uclapi.com/oauth/authorise?client_id={CLIENT_ID}&state=727'
SLASH_GUILD = 706398438937460796
