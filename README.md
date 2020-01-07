# TaigaBot
Invite Taiga to your discord server for a good time :)

# Dependencies
* Python 3
* discord.py

# Setup
Once all the dependecies are installed setting up TaigaBot is fairly trivial.

Fork the repo and follow the following steps:

First, in order to link TaigaBot to your discord bot, you need to create a file named taigaBot.token in the src directory. This is where you will copy your bot's token to link the discord bot to TaigaBot. **Make sure there is only one line in the file**

Finally, to add the custom commands functionality you need to create a file named commands.json in the src directory and TaigaBot should be set up.

Run the bot.py script with the command `Python3 bot.py` and TaigaBot should come to life!

# List of Commands

taiga
---
`.taiga`

The most important command of all. Responds with a picture of the one and only Taiga Aisaka

addCommand
---
`.addCommand [command name] [text/url]`

The addCommand functionality will add a custom command, `[command name]`, to TaigaBot. This command can either be a text response to the command or an external link to embedd such and a picture or a gif.

ping
---
`.ping`

Pong!

