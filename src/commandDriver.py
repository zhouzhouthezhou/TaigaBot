#complex commands
import discord
import json

async def getPCommand(message):
    try:
        params = message.content[(message.content.index(' ') + 1):].split(' ', 1)
    except (ValueError):
        return None
    return params

async def _mutatecommand(message):
    params = await getPCommand(message)
    
    params[0] = params[0].casefold()

    print(params)

    
    if params[1][0] == '.' or params[0][0] == '.':
        await message.channel.send('Invalid location for character \'.\'')
        return

    if params[0][0] == '_':
        await message.channel.send('Invalid location for character \'_\'')
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

async def addcommand_(message):
    params = await getPCommand(message)
    if params == None:
        await message.channel.send('Invalid form, should take form .addCommand [command name] [text/url]')
        return
    
    if len(params) != 2:
        await message.channel.send('Invalid form, should take form .addCommand [command name] [text/url]')
        return

    await _mutatecommand(message)
    await message.channel.send(f'Added command {params[0]}')
 

async def editcommand_(message):
    params = await getPCommand(message)
    if params == None:
        await message.channel.send('Invalid form, should take form .editCommand [command name] [text/url]')
    
    if len(params) != 2:
        await message.channel.send('Invalid form, should take form .editCommand [command name] [text/url]')
        return

    params[0] = params[0].casefold()

    commandList = dict()
    sysCommandList = dict()
    with open('commands.json', 'r') as f:
        commandList = json.load(f)
    with open('sysCmds.json', 'r') as f:
        sysCommandList = json.load(f)
        commandList.update(sysCommandList)
    
    added = False
    if not params[0] in commandList:
        await message.channel.send(f'Command not found, creating new command {params[0]}')
        added = True
    
    await _mutatecommand(message)
    if(not added):
        await message.channel.send(f'Edited command {params[0]}')
    else:
        await message.channel.send(f'Added command {params[0]}')
     
async def deletecommand_(message):
    pass

async def help_(message):
    pass

async def list_(message):
    commandList = dict()
    sysCommandList = dict()
    with open('commands.json', 'r') as f:
        commandList = json.load(f)
    with open('sysCmds.json', 'r') as f:
        sysCommandList = json.load(f)
    
    s = '```System Commands:\n---------------------\n'
    for key in sysCommandList.keys():
        s = s + key + '\n'
    
    s = s + '\nCustom Commands:\n---------------------\n'
    for key in commandList.keys():
        s = s + key + '\n'
    
    s = s + '```'
    await message.channel.send(s)

