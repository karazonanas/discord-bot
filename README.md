# Discord Bot to monitor websites status
This bot is a simple discord bot that monitors websites status and sends a message to a discord channel when a website is down.

## Prerequisites
- Docker & Docker Compose
- Discord Bot created and added to your server in your channel
  - You can follow this instructions to create your bot and add it to your server: https://discordpy.readthedocs.io/en/stable/discord.html
  - Permissions needed:
    - Send Messages
    - Read Messages/Voice Channels
  - In  https://discord.com/developers/applications/ choose your bot which you've just created and then go to `Bot -> MESSAGE CONTENT INTENT` and enable it

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
     - DISCORD_TOKEN: Discord bot token (you can get it under `Bot -> TOKEN`)
     - DISCORD_SERVER_ID: Server ID where the bot will be running (you can get it by right clicking on the server icon and clicking on `Copy ID`)
     - DISCORD_CHANNEL_ID: Discord Channel ID where the messages will be sent (you can get it by right clicking on the channel and clicking on `Copy ID`)
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