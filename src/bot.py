import discord
import json
import commandDriver

simpArr = []
with open('simpeFile.txt', 'r') as simpFile:
    simpArr.append(simpFile.read())
with open('taigaBot.token', 'r') as f:
    token = f.read()

class TaigaClient(discord.Client):
    commandList = dict()
    sysCommandList = dict()
    async def refreshCommands(self):
        with open('commands.json', 'r') as f:
            self.commandList = json.load(f)
        with open('sysCmds.json', 'r') as f:
            self.sysCommandList = json.load(f)
        self.commandList.update(self.sysCommandList)
        
    async def on_ready(self):
        print(f'{self.user} has connected to Discord')

    async def mentions(self, message):
        #@mention handling
        for u in message.mentions:
            author = message.author.name if message.author.nick == None else message.author.nick
            user = u.name if u.nick == None else u.nick
            await message.channel.send(content=f'UwU {author} needs your bulgy wolgy {user}', tts=True)
       
        #@role handling
        for r in message.role_mentions:
            author = message.author.name if message.author.nick == None else message.author.nick
            await message.channel.send(content=f'UwU {author} needs your bulgy wolgy {r.name}', tts=True)

    async def catchSimps(self, message):
        if 'togglesimpdetector' in message.content:
            return
        with open('simpvar', 'r') as f:
            simpVar = f.read()
        if simpVar == 'true' and message.author.name in simpArr:
            e = discord.Embed()
            e.set_image(url='https://i.kym-cdn.com/photos/images/newsfeed/001/709/184/73a.jpg')
            await message.channel.send(content=None, embed=e)


    async def on_message(self, message):
        await self.refreshCommands()
        await self.mentions(message)

        if len(message.content) > 0 and message.content[0] == '.':
            c = message.content[1:].split(' ', 1)
            if c[0] == '':
                await self.catchSimps(message)
                return
            try:
                command = self.commandList[c[0].casefold()]
            except (KeyError):
                #await message.channel.send(f'Unrecognized Command: {c[0]}')
                await self.catchSimps(message)
                return

            print(c)

            if command["type"] == 0:
                await message.channel.send(command["text"])
            elif command["type"] == 1:
                e = discord.Embed()
                e.set_image(url=command["url"])
                await message.channel.send(content=None, embed=e)
            elif command["type"] == 10:
                await getattr(commandDriver, f'{c[0].casefold()}_')(message)
            else:
                await message.channel.send('Undefined Command')

        await self.catchSimps(message)


client = TaigaClient()
client.run(token)
