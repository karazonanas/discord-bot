# Discord Bot to monitor websites status
This bot is a simple discord bot that monitors websites status and sends a message to a discord channel when a website is down.

## Prerequisites
- Docker & Docker Compose
- Discord Bot created and added to your server in your channel
  - You can follow this instructions to create your bot and add it to your server: https://discordpy.readthedocs.io/en/stable/discord.html
  - Permissions needed:
    - Send Messages
    - Read Messages/Voice Channels
- Server ID where the bot will be running
- Discord Channel ID where the messages will be sent

## How to use
1. Clone this repository
2. Create a `.env` file in the root of the project with the following variables:
    ```
    DISCORD_TOKEN = 
    DISCORD_SERVER_ID = 
    DISCORD_CHANNEL_ID = 
    URLS = 
    INTERVAL = 
    ```
   - env variables explanation:
     - DISCORD_TOKEN: Discord bot token
     - DISCORD_SERVER_ID: Discord server ID where the bot will be running
     - DISCORD_CHANNEL_ID: Discord channel ID where the messages will be sent
     - URLS: comma separated list of urls to monitor
     - INTERVAL: interval in seconds to check the urls
3. Run `docker-compose up -d` to start the bot
4. Done! The bot will send a message to the channel when a website returns a status code different than 200

## Commands

- `stop <time>`: stop the bot for the specified time in minutes
- `check`: Fires a check of the urls and sends a message to the channel

## Example:
![image](/Images/example.png)

## Troubleshooting
- If you have any problem with the bot, you can check the logs with `docker logs <container_name>`