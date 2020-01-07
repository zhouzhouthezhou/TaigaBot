# TaigaBot
Invite Taiga to your discord server for a good time :)

![Taiga](https://vignette.wikia.nocookie.net/tora-dora/images/8/82/E17_-_9.png/revision/latest/scale-to-width-down/340?cb=20160728131220)

# Dependencies
* Python 3
* discord.py

# Setup
Once all the dependecies are installed setting up TaigaBot is fairly trivial.

Fork the repo and follow the following steps:

First, in order to link TaigaBot to your discord bot, you need to create a file named taigaBot.token in the src directory. This is where you will copy your bot's token to link the discord bot to TaigaBot. **Make sure there is only one line in the file**

Finally, to add the custom commands functionality you need to create a file named commands.json in the src directory and TaigaBot should be set up. Note: If you try to add custom commands and the terminal says something to the tune of `Permission Denied` run the command `sudo chmod 666 commands.json`

Run the bot.py script with the command `Python3 bot.py` and TaigaBot should come to life!

# Developer Notes
I'll get back to this

# List of Commands

The following is a list of all of TaigaBot's native 'system' commands
Note: All commands, custom or otherwise, are **not** case sensitive

taiga
---
`.taiga`

The most important command of all. Responds with a picture of the one and only Taiga Aisaka

addCommand
---
`.addCommand [command name] [text/url]`

The addCommand command will add a custom command, `[command name]`, to TaigaBot. This command will make taiga respond with `[text/url]`. This can either be plain text response or an external link to embedd such and a picture or a gif.

editCommand
---
`.editCommand [command name] [text/url]`

The editCommand command will edit the custom command given by `[command name]` to respond with `[text/url]` or, if the inputed command does not exist, it will create the command in accordance with the `.addCommand` command.

deleteCommand
---
`.deleteCommand [command name]`

WIP
The delete command will delete the custom command given by [command name].

help
---
`.help [command name]`

WIP
The help command will display the documentation of the system command given by [command name].

list
---
`.list`

The list command will list all of the system and custom commands the are currently stored by TaigaBot

ping
---
`.ping`

Pong!

kms
---
`.kms`

![kms](https://thumbs.gfycat.com/ApprehensiveJoyfulBonobo-size_restricted.gif)

kys
---
`.kys`

![kys](https://media1.tenor.com/images/7282a0f80bf1744a17295a124d891068/tenor.gif?itemid=9140602)

