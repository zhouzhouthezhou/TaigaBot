#complex commands
from __future__ import unicode_literals
import discord
import json
import time
import youtube_dl

async def getPCommand(message):
    try:
        params = message.content[(message.content.index(' ') + 1):].split(' ', 1)
    except (ValueError):
        return None
    print(params)
    return params

async def _mutatecommand(message):
    params = await getPCommand(message)
    
    params[0] = params[0].casefold()

    print(params)

    if params[1][0] == '.' or params[0][0] == '.':
        await message.channel.send('Invalid location for character \'.\'')
        return False

    if params[0][0] == '_':
        await message.channel.send('Invalid location for character \'_\'')
        return False

    if '`' in params[0][0]:
        await message.channel.send('Invalid location for character \'`\'')
        return False

    if '\n' in params[0][0] or '\r' in params[0][0]:
        await message.channel.send('Invalid use of newline')
        return False

    with open('sysCmds.json', 'r') as f:
        sysCommands = json.load(f)
        if params[0] in sysCommands:
            await message.channel.send('Immutable Command')
            return False

    with open('commands.json', 'r+') as f:
        commandList = json.load(f)
        if 'https://' in params[1]:
            commandList[params[0]] = {"type" : 1, "url" : params[1]}
        else:
            commandList[params[0]] = {"type" : 0, "text" : params[1]}
        f.seek(0)
        json.dump(commandList, f, indent=4)
        f.truncate()
    
    return True

async def addcommand_(message):
    params = await getPCommand(message)
    if params == None:
        await message.channel.send('Invalid form, should take form .addCommand [command name] [text/url]')
        return
    
    if len(params) != 2:
        await message.channel.send('Invalid form, should take form .addCommand [command name] [text/url]')
        return

    if await _mutatecommand(message):
        await message.channel.send(f'Added command {params[0]}')
 

async def editcommand_(message):
    params = await getPCommand(message)
    if params == None:
        await message.channel.send('Invalid form, should take form .editCommand [command name] [text/url]')
        return
    
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
    params = await getPCommand(message)
    if params == None:
        await message.channel.send('Invalid form, should take form .deleteCommand [command name]')
        return

    params[0] = params[0].casefold()

    commandList = dict()
    with open('commands.json', 'r+') as f:
        commandList = json.load(f)

        if params[0] in commandList.keys():
            del commandList[params[0]]
        else:
            await message.channel.send(f'Custom command {params[0]} not found')
            return
            
        f.seek(0)
        json.dump(commandList, f, indent=4)
        f.truncate()


    await message.channel.send(f'Custom command {params[0]} deleted')

async def help_(message):
    params = await getPCommand(message)
    if params == None or len(params) != 1:
        await message.channel.send('Invalid form, should take form .help [command name]')
        return
    
    params[0] = params[0].casefold()

    with open('sysCmds.json', 'r') as f:
        sysCommandList = json.load(f)
        if not params[0] in sysCommandList.keys():
            await message.channel.send('Command not found, help is only available for system commands')
        else:
            await message.channel.send(sysCommandList[params[0]]["help"])

async def list_(message):
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

async def togglesimpdetector_(message):
    with open('simpvar', 'r') as f:
        simpVar = f.read()
    f = open('simpvar', 'w')
    if simpVar == 'true':
        if message.author.name == 'Neuro':
            f.write('true')
            e = discord.Embed()
            e.set_image(url='https://ih0.redbubble.net/image.1008996081.6402/st,small,507x507-pad,600x600,f8f8f8.jpg')
            await message.channel.send(content='By order of the Simp Patrol you are not allowed to use this command', embed=e)
        else:
            f.write('false')
            await message.channel.send('Simp Detector disabled')
        f.close()
    else:
        f.write('true')
        f.close()
        await message.channel.send('Simp Detector enabled')
#####################################################################################

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


voiceConnection = None

async def join_(message):
    global voiceConnection
    if(message.author.voice != None):
        voiceConnection = await message.author.voice.channel.connect()
        await message.channel.send('Connected to voice')
    else:
        await message.channel.send('You must be in a voice channel for me to connect')

async def leave_(message):
    global voiceConnection
    if(voiceConnection != None):
        voiceConnection.stop()
        voiceConnection.play(discord.FFmpegPCMAudio('audioSamples/taiga_baka.opus'), after=lambda e: print(e))
        time.sleep(2.1)
        await voiceConnection.disconnect()
        voiceConnection = None
        await message.channel.send('Disconnected from voice')
    else:
        await message.channel.send('I am not currently in a voice channel')

def _youtubeHook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

async def play_(message):
    params = await getPCommand(message)
    if params == None or len(params) != 1:
        await message.channel.send('Invalid form, should take form .play [url/playlist]')
        return

    params[0] = params[0].casefold()

    if not 'https://' in params[0] or not ('youtube' in params[0] or 'youtu.be' in params[0]):
        await message.channel.send('Command input must be a valid youtube url')
        return
    

    if voiceConnection == None:
        await message.channel.send('I need to be in a voice channel to play anything, try using the .join command')
        return
    else:
        #voiceConnection.play(discord.FFmpegPCMAudio('audioSamples/pitd.opus'), after=lambda e: print(e))
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'logger': MyLogger(),
            'progress_hooks': [_youtubeHook],
        }
        ytest = {}
        with youtube_dl.YoutubeDL(ytest) as ydl:
            ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc']) 
    




async def pause_(message):
    pass

async def stop_(message):
    pass

async def playlist_(message):
    pass
