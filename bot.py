import requests
import discord
import asyncio
from dotenv.main import load_dotenv
import os
from logger import Logger

# load environment variables
load_dotenv()

# get environment variables
url = os.getenv("URL")
search_term = os.getenv("SEARCH_TERM")
discord_token = os.getenv("DISCORD_TOKEN")
server_id = os.getenv("DISCORD_SERVER_ID")
channel_id = os.getenv("DISCORD_CHANNEL_ID")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

# ini logger
logger = Logger(__file__, __name__).get_logger()


async def send_discord_message(message):
    """
    Send a message to a discord channel
    :param message: the message to send
    :return: None
    """
    try:
        await client.wait_until_ready()
        server = client.get_guild(int(server_id))
        channel = server.get_channel(int(channel_id))
        await channel.send(message)
    except Exception as e:
        logger.error(f"Error while sending discord message: {str(e)}")


async def check_website():
    """
    Check if the website is up and running
    :return: None
    """
    try:
        response = requests.get(url)
        if response.status_code != 200:
            await send_discord_message(f"Website {url} is down!, status code: {response.status_code},"
                                       f" reason: {response.reason}")
        else:
            logger.info(f"Website {url} is up and running")

    except Exception as e:
        logger.error(f"Error while checking website: {str(e)}")


@client.event
async def on_ready():
    """
    This function is called when the bot is ready to start
    It will check the website every INTERVAL seconds
    :return: None
    """
    logger.info(f"Logged in as {client.user.name} (ID: {client.user.id})")
    while True:
        await check_website()
        await asyncio.sleep(int(os.getenv("INTERVAL")))


client.run(discord_token)
