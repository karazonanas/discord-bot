import requests
import discord
import asyncio
from dotenv.main import load_dotenv
import os
from logger import Logger

# load environment variables
load_dotenv()

# get environment variables
urls = os.getenv("URLS")
search_term = os.getenv("SEARCH_TERM")
discord_token = os.getenv("DISCORD_TOKEN")
server_id = os.getenv("DISCORD_SERVER_ID")
channel_id = os.getenv("DISCORD_CHANNEL_ID")
interval = int(os.getenv("INTERVAL"))

# ini discord client
intents = discord.Intents.default()
intents.message_content = True
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


async def send_alert(message, title="Alert", color=discord.Color.red()):
    """
    Send an alert to a discord channel
    :param title: the title of the alert
    :param message: the message to send
    :param color: the color of the alert
    :return: None
    """
    try:
        await client.wait_until_ready()
        server = client.get_guild(int(server_id))
        channel = server.get_channel(int(channel_id))
        embed = discord.Embed(title=title, description=message, color=color)
        await channel.send(embed=embed)
    except Exception as e:
        logger.error(f"Error while sending discord message: {str(e)}")


async def check_website(success_alert=False):
    """
    Check if the website is up and running
    :return: None
    """
    for url in urls.split(','):
        logger.info(f"Checking website {url}")
        try:
            response = requests.get(url)
            if response.status_code != 200:
                await send_alert(f"\u274C Website {url} is down!, status code: {response.status_code}")
                logger.error(f"Website {url} is down!, status code: {response.status_code}")
            else:
                if success_alert:
                    await send_alert(f"\u2705 Website {url} is up and running", title="Success",
                                     color=discord.Color.green())
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
        sleep = 0
        await check_website()
        if os.path.exists("stop.txt"):
            with open("stop.txt", "r") as f:
                sleep = int(f.read()) * 60
            os.remove("stop.txt")
        logger.info(f"Sleeping for {interval + sleep} seconds")
        await asyncio.sleep(interval + sleep)


@client.event
async def on_message(message):
    """
    This function is called when a message is sent to a channel
    :param message: the message sent
    :return: None
    """
    if message.content.startswith("stop"):
        min = message.content.split(" ")[1]
        with open("stop.txt", "w") as f:
            f.write(min)
    if message.content.startswith("check"):
        logger.info(f"Checking website")
        await check_website(True)

client.run(discord_token)
