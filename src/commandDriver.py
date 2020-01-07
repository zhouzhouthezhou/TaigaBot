#complex commands
import discord
import json

async def addcommand(message):
    try:
        params = message.content[(message.content.index(' ') + 1):].split(' ', 1)
    except (ValueError):
        await message.channel.send('Invalid form, should take form .addCommand [command name] [text/url]')
        return
    
    params[0] = params[0].casefold()

    print(params)

    if len(params) != 2:
        await message.channel.send('Invalid form, should take form .addCommand [command name] [text/url]')
        return
    
    if params[1][0] == '.' or params[0][0] == '.':
        await message.channel.send('Invalid location for character \'.\'')
        return

    with open('sysCmds.json', 'r') as f:
        sysCommands = json.load(f)
        if params[0] in sysCommands:
            await message.channel.send('Immutable Command')
            return

    with open('commands.json', 'r+') as f:
        commandList = json.load(f)
        if 'https://' in params[1]:
            commandList[params[0]] = {"type" : 1, "url" : params[1]}
        else:
            commandList[params[0]] = {"type" : 0, "text" : params[1]}
        f.seek(0)
        json.dump(commandList, f, indent=4)
        f.truncate()
        await message.channel.send(f'Added command {params[0]}')