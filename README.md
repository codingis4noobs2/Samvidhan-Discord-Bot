# Samvidhan Bot

## Introduction
Samvidhan Bot is a Discord bot designed to make the Indian Constitution accessible and understandable to everyone on Discord. It provides users with the ability to fetch articles, search by description, view amendment history, and much more.

## Features
- Display summaries of all articles in the Indian Constitution.
- Provide details and summaries of different parts of the Constitution.
- Search for specific articles by number.

## Invite Samvidhan Bot to Your Server
You can add Samvidhan Bot to your Discord server using the following invite link:
[Invite Samvidhan Bot](https://discord.com/api/oauth2/authorize?client_id=1200061602213404672&permissions=277025508352&scope=bot+applications.commands) (Yet to be hosted)

## Commands Available
- `/help`: Displays all the available commands and their descriptions.
- `/about`: Displays information about the bot.
- `/all_articles`: Displays all articles with a summary table and pagination.
- `/part_details`: Provides details and summary of different parts of the Indian Constitution with pagination.
- `/search_article <article_number>`: Searches for an article by its number and displays the information.

## Installation on Local Device
To install and run Samvidhan Bot on your local device, follow these steps:

### Prerequisites
- Python 3.8 or higher
- `nextcord` library
- A Discord bot token

### Steps
1. Install the `nextcord` library using pip:
```
pip install -U nextcord
```

2. Create a new Discord bot on the [Discord Developer Portal](https://discord.com/developers/applications) and obtain your bot token and invite the bot in your server.

3. Enable the necessary intents for your bot in the Discord Developer Portal. Samvidhan Bot requires the `GUILDS` and `MESSAGE_CONTENT` intents to be enabled.

4. Clone the repository to your local machine:
```
git clone https://github.com/your_github/samvidhan-bot.git
```

5. Create a `.env` file in the root directory of the project and add your Discord bot token:
```
DISCORD_TOKEN=your_bot_token_here
```

6. Run the bot with the following command:
```
python bot.py
```

## Screenshots
![s111](https://github.com/codingis4noobs2/Samvidhan-Discord-Bot/assets/87560178/c05d2cf8-81a2-410a-9473-de2e5b2d51fd)
![s222](https://github.com/codingis4noobs2/Samvidhan-Discord-Bot/assets/87560178/ccb23853-3142-45c2-aba2-f5f740a18543)
![s333](https://github.com/codingis4noobs2/Samvidhan-Discord-Bot/assets/87560178/06841891-fb77-4d01-9df5-13544d601137)
![s444](https://github.com/codingis4noobs2/Samvidhan-Discord-Bot/assets/87560178/5ecfd733-491a-4ee4-94ed-78569b1cd12e)

![s555](https://github.com/codingis4noobs2/Samvidhan-Discord-Bot/assets/87560178/686b7ab7-0f44-4fb0-a11f-380bc2f2a7b9)
