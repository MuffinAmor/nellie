from datetime import datetime

import discord
from discord.ext import commands

from lib.general import prefix

bot = commands.Bot(command_prefix='nl!')

botcolor = 0x00ff06

bot.remove_command('help')

Nellie = "[Nellie](https://discordapp.com/oauth2/authorize?" \
         "client_id=631149405965385759&permissions=388305&redirect_uri=https%3A%2F%2Fdiscord.gg&scope=bot)"

url = 'https://cdn.discordapp.com/attachments/522437022095245313/546359964101509151/Neko_Logo.png'


def current(bot, message):
    current = prefix(str(message.guild.id))
    return current


support = "Do you need help? {}support".format(current)


class nellie(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Nellie = "https://discordapp.com/oauth2/authorize?" \
                      "client_id=631149405965385759&permissions=388305&redirect_uri=https%3A%2F%2Fdiscord.gg&scope=bot"

    ########################################################################################################################

    @commands.command()
    async def invite(self, ctx):
        if ctx.author.bot is False:
            embed = discord.Embed(color=ctx.author.color)
            embed.add_field(
                name=":tools: Nellie Invite Link :tools:",
                value="[Do like invite me? Click me!]({})".format(self.Nellie), inline=False)
            embed.set_footer(text='Message was requested by {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot is False:
            current = prefix(str(message.guild.id))
            support = "Do you need help? {}support".format(current)
        if message.content.startswith("n!cmdhelp"):
            if "createroom" in message.content:
                embed = discord.Embed(title="Command Help: createroom", description="Command Number 201",
                                      color=message.author.color)
                embed.add_field(name='Bot:', value=Nellie, inline=True)
                embed.add_field(name='Command', value='createroom *id* *name*', inline=True)
                embed.add_field(name='Example:',
                                value='{}createroom 636702313758851102² #Neko Dev. Army³\n'
                                      '*² the ID of a Channel from the other Server, *³Your choosen name.'.format(
                                    current), inline=False)
                embed.add_field(name='Description',
                                value='The Command **createroom** make possible to create your personal Globalchatroom '
                                      'beetween two different Servers.\n'
                                      'It create a connection beetween the Command and the ID-Channel.',
                                inline=False)
                embed.add_field(name='Argument fields:',
                                value='__**id**__:\n'
                                      'In this field you put in the Channel-id of the Channel which you like create '
                                      'the Chatroom in the other Server.\n'
                                      '\n'
                                      '__**name**__:\n'
                                      'In the name field you put in your own choosen name, '
                                      'how you like name your personal Chatgroup. '
                                      'This name can not be changed after the Command excecute.',
                                inline=False)
                embed.add_field(name='Required Permissions:',
                                value='__**Bot**__:\n'
                                      '-Manage Channels\n'
                                      '-Embed Links\n'
                                      '-Message send\n'
                                      '-Manage Messages\n'
                                      '-Message read\n'
                                      '\n'
                                      '__**Command Excecuter**__:\n'
                                      'Administrator in both Server',
                                inline=False)
                embed.set_thumbnail(url=url)
                embed.set_footer(text=support)
                embed.timestamp = datetime.utcnow()
                await message.channel.send(embed=embed)
            elif "unlink" in message.content:
                embed = discord.Embed(title="Command Help: unlink", description="Command Number 202",
                                      color=message.author.color)
                embed.add_field(name='Bot:', value=Nellie, inline=True)
                embed.add_field(name='Command', value='unlink *id* *name*', inline=True)
                embed.add_field(name='Example:',
                                value='{}unlink 636702313758851102² #Neko Dev. Army³\n'
                                      '*² the ID of the Channel you like unlink, *³The Chatroom name.'.format(
                                    current), inline=False)
                embed.add_field(name='Description',
                                value='The Command **unlink** cut the connection beetween the ID-Channel '
                                      'and the Chatroom.',
                                inline=False)
                embed.add_field(name='Argument fields:',
                                value='__**id**__:\nIn this field you put in the Channel-id of the Channel which you '
                                      'like disconnect from the Chatroom.\n'
                                      '\n'
                                      '__**name**__:\n'
                                      'In the **name** field you put in, from which Chatroom do you like disconnect '
                                      'the ID-Channel.',
                                inline=False)
                embed.add_field(name='Required Permissions:',
                                value='__**Bot**__:\n'
                                      '-Manage Channels\n'
                                      '-Embed Links\n'
                                      '-Message send\n'
                                      '-Manage Messages\n'
                                      '-Message read\n'
                                      '\n'
                                      '__**Command Excecuter**__:\n'
                                      'Administrator in the Server of the ID-Channel',
                                inline=False)
                embed.set_thumbnail(url=url)
                embed.set_footer(text=support)
                embed.timestamp = datetime.utcnow()
                msg = await message.channel.send(embed=embed)
            #################################################################
            elif "roominfo" in message.content:
                embed = discord.Embed(title="Command Help: roominfo", description="Command Number 203",
                                      color=message.author.color)
                embed.add_field(name='Bot:', value=Nellie, inline=True)
                embed.add_field(name='Command', value='roominfo *name*', inline=True)
                embed.add_field(name='Example:',
                                value='{}roominfo #Neko Dev. Army³\n*³The Chatroom name.'.format(current), inline=False)
                embed.add_field(name='Description',
                                value='The Command **roominfo** gives you infos about the named room.', inline=False)
                embed.add_field(name='Argument fields:',
                                value='__**name**__:\nIn the **name** field you put in, from which Chatroom do you like have Infos.',
                                inline=False)
                embed.add_field(name='Required Permissions:',
                                value='__**Bot**__:\n-Embed Links\n-Send Messages\n-Read Messages\n\n__**Command Excecuter**__:\n-Send Messages\n-Read Messages\n',
                                inline=False)
                embed.set_thumbnail(url=url)
                embed.set_footer(text=support)
                embed.timestamp = datetime.utcnow()
                msg = await message.channel.send(embed=embed)
            #################################################################
            elif "namecheck" in message.content:
                embed = discord.Embed(title="Command Help: namecheck", description="Command Number 204",
                                      color=message.author.color)
                embed.add_field(name='Bot:', value=Nellie, inline=True)
                embed.add_field(name='Command', value='namecheck *name*', inline=True)
                embed.add_field(name='Example:',
                                value='{}namecheck #Neko Dev. Army³\n*³The checked name.'.format(current), inline=False)
                embed.add_field(name='Description',
                                value='The Command **namecheck** tells you, if this Chatroomname is allready given or avaible.',
                                inline=False)
                embed.add_field(name='Argument fields:',
                                value='__**name**__:\nIn the **name** field you put in, which name do you like check.',
                                inline=False)
                embed.add_field(name='Required Permissions:',
                                value='__**Bot**__:\n-Embed Links\n-Send Messages\n-Read Messages\n\n__**Command Excecuter**__:\n-Send Messages\n-Read Messages\n',
                                inline=False)
                embed.set_thumbnail(url=url)
                embed.set_footer(text=support)
                embed.timestamp = datetime.utcnow()
                msg = await message.channel.send(embed=embed)
            #################################################################
            if "delroom" in message.content:
                embed = discord.Embed(title="Command Help: delroom", description="Command Number 205",
                                      color=message.author.color)
                embed.add_field(name='Bot:', value=Nellie, inline=True)
                embed.add_field(name='Command', value='delroom *name*', inline=True)
                embed.add_field(name='Example:',
                                value='{}delroom #Neko Dev. Army³\n*³The Name of the Chatroom that you like delete.'.format(
                                    current), inline=False)
                embed.add_field(name='Description',
                                value='The Command **delroom** delete the named Chatroom, if you owns them.',
                                inline=False)
                embed.add_field(name='Argument fields:',
                                value='__**name**__:\nIn the **name** field you put in, which Chatroom do you like delete.',
                                inline=False)
                embed.add_field(name='Required Permissions:',
                                value='__**Bot**__:\n-Embed Links\n-Send Messages\n-Read Messages\n\n__**Command Excecuter**__:\nNeed to be the Owner of the named Chatroom.',
                                inline=False)
                embed.set_thumbnail(url=url)
                embed.set_footer(text=support)
                embed.timestamp = datetime.utcnow()
                msg = await message.channel.send(embed=embed)
            #################################################################
            elif "addmod" in message.content:
                embed = discord.Embed(title="Command Help: addmod", description="Command Number 206",
                                      color=message.author.color)
                embed.add_field(name='Bot:', value=Nellie, inline=True)
                embed.add_field(name='Command', value='addmod *member* *name*', inline=True)
                embed.add_field(name='Example:',
                                value='{}addmod <@474947907913515019>² #Neko Dev. Army³\n*² the User that you would like add, *³The Name of the Chatroom in which you like add the Mod.'.format(
                                    current), inline=False)
                embed.add_field(name='Description',
                                value='The Command **addmod** add the mentioned Member as Mod to your Chatroom.',
                                inline=False)
                embed.add_field(name='Argument fields:',
                                value='__**member**__:\nThis field you mention the member that you like add as Mod to your Chatroom.\n\n__**name**__:\nIn the **name** field you put in, in which Chatroom do you like add the Mod.',
                                inline=False)
                embed.add_field(name='Required Permissions:',
                                value='__**Bot**__:\n-Manage Channels\n-Embed Links\n-Message send\n-Manage Messages\n-Message read\n\n__**Command Excecuter**__:\n-Need to be the Owner of the named Chatroom.',
                                inline=False)
                embed.set_thumbnail(url=url)
                embed.set_footer(text=support)
                embed.timestamp = datetime.utcnow()
                msg = await message.channel.send(embed=embed)
            #################################################################
            elif "add" in message.content:
                embed = discord.Embed(title="Command Help: add", description="Command Number 207",
                                      color=message.author.color)
                embed.add_field(name='Bot:', value=Nellie, inline=True)
                embed.add_field(name='Command', value='add *id* *name*', inline=True)
                embed.add_field(name='Example:',
                                value='{}add 636702313758851102² #Neko Dev. Army³\n*² the ID of the Channel which you would like add, *³The Name of the Chatroom that you like add the Channel.'.format(
                                    current), inline=False)
                embed.add_field(name='Description',
                                value='The Command **add** connect the ID-Channel with your Chatroom.', inline=False)
                embed.add_field(name='Argument fields:',
                                value='__**id**__:\nIn this field you put in the Channel-id of the Channel which you like connect with the named Chatroom.\n\n__**name**__:\nIn the **name** field you put in, in which Chatroom do you like add the ID-Channel.',
                                inline=False)
                embed.add_field(name='Required Permissions:',
                                value='__**Bot**__:\n-Manage Channels\n-Embed Links\n-Message send\n-Manage Messages\n-Message read\n\n__**Command Excecuter**__:\n-Need to be the Owner of the named Chatroom or the Chatroom need to set as Public.\n-You need to have administrator permissions of the ID-Channel Server',
                                inline=False)
                embed.set_thumbnail(url=url)
                embed.set_footer(text=support)
                embed.timestamp = datetime.utcnow()
                msg = await message.channel.send(embed=embed)
            #################################################################
            elif "removemod" in message.content:
                embed = discord.Embed(title="Command Help: removemod", description="Command Number 208",
                                      color=message.author.color)
                embed.add_field(name='Bot:', value=Nellie, inline=True)
                embed.add_field(name='Command', value='removemod *member* *name*', inline=True)
                embed.add_field(name='Example:',
                                value='{}removemod <@474947907913515019>² #Neko Dev. Army³\n*² the Member which you like remove as Mod, *³The Name of the Chatroom in which you like remove the Mod.'.format(
                                    current), inline=False)
                embed.add_field(name='Description',
                                value='The Command **removemod** remove the mentioned Member as Mod from your Chatroom.',
                                inline=False)
                embed.add_field(name='Argument fields:',
                                value='__**member**__:\nThis field you mention the member that you like remove the Mod from your Chatroom.\n\n__**name**__:\nIn the **name** field you put in, from which Chatroom do you like remove the Mod.',
                                inline=False)
                embed.add_field(name='Required Permissions:',
                                value='__**Bot**__:\n-Embed Links\n-Message send\n-Message read\n\n__**Command Excecuter**__:\n-Need to be the Owner of the named Chatroom.',
                                inline=False)
                embed.set_thumbnail(url=url)
                embed.set_footer(text=support)
                embed.timestamp = datetime.utcnow()
                msg = await message.channel.send(embed=embed)
            #################################################################
            elif "showmod" in message.content:
                embed = discord.Embed(title="Command Help: showmod", description="Command Number 209",
                                      color=message.author.color)
                embed.add_field(name='Bot:', value=Nellie, inline=True)
                embed.add_field(name='Command', value='showmod *name*', inline=True)
                embed.add_field(name='Example:',
                                value='{}showmod #Neko Dev. Army³\n*³The Name of the Chatroom from which you like see the Mods.'.format(
                                    current), inline=False)
                embed.add_field(name='Description',
                                value='The Command **showmod** shows you the current Mods of the named Chatgroup.',
                                inline=False)
                embed.add_field(name='Argument fields:',
                                value='__**name**__:\nIn the **name** field you put in, from which Chatroom do you like see the Mods.',
                                inline=False)
                embed.add_field(name='Required Permissions:',
                                value='__**Bot**__:\n-Embed Links\n-Message send\n-Message read\n\n__**Command Excecuter**__:\n-Need to be the Owner of the named Chatroom.',
                                inline=False)
                embed.set_thumbnail(url=url)
                embed.set_footer(text=support)
                embed.timestamp = datetime.utcnow()
                msg = await message.channel.send(embed=embed)
            #################################################################
            elif "unban" in message.content:
                embed = discord.Embed(title="Command Help: unban", description="Command Number 210",
                                      color=message.author.color)
                embed.add_field(name='Bot:', value=Nellie, inline=True)
                embed.add_field(name='Command', value='unban *id* *name*', inline=True)
                embed.add_field(name='Example:',
                                value='{}unban 474947907913515019² #Neko Dev. Army³\n*² the ID of the User that you would unban *³The Name of the Chatroom from which you like unban the User.'.format(
                                    current), inline=False)
                embed.add_field(name='Description',
                                value='The Command **unban** allows you to unban a user from the named Chatgroup.',
                                inline=False)
                embed.add_field(name='Argument fields:',
                                value='__**id**__:\nIn the field **id** you put in the ID of the User who you like unban the the named Chatroom.\n\n__**name**__:\nIn the **name** field you put in, from which Chatroom you like unban the User.',
                                inline=False)
                embed.add_field(name='Required Permissions:',
                                value='__**Bot**__:\n-Manage Channels\n-Embed Links\n-Message send\n-Manage Messages\n-Message read\n\n__**Command Excecuter**__:\n-Need to be a Moderator of the named Chatroom.',
                                inline=False)
                embed.set_thumbnail(url=url)
                embed.set_footer(text=support)
                embed.timestamp = datetime.utcnow()
                msg = await message.channel.send(embed=embed)
            #################################################################
            elif "ban" in message.content:
                embed = discord.Embed(title="Command Help: ban", description="Command Number 211",
                                      color=message.author.color)
                embed.add_field(name='Bot:', value=Nellie, inline=True)
                embed.add_field(name='Command', value='ban *id* *name*', inline=True)
                embed.add_field(name='Example:',
                                value='{}ban 474947907913515019 #Neko Dev. Army³\n*² the ID of the User that you would ban, *³The Name of the Chatroom from which you like ban the User.'.format(
                                    current), inline=False)
                embed.add_field(name='Description',
                                value='The Command **ban** allows you to ban a user out of the named Chatgroup.',
                                inline=False)
                embed.add_field(name='Argument fields:',
                                value='__**id**__:\nIn the field **id** you put in the ID of the User who you like ban out of the named Chatroom.\n\n__**name**__:\nIn the **name** field you put in, from which Chatroom you like ban the User.',
                                inline=False)
                embed.add_field(name='Required Permissions:',
                                value='__**Bot**__:\n-Manage Channels\n-Embed Links\n-Message send\n-Manage Messages\n-Message read\n\n__**Command Excecuter**__:\n-Need to be a Moderator of the named Chatroom.',
                                inline=False)
                embed.set_thumbnail(url=url)
                embed.set_footer(text=support)
                embed.timestamp = datetime.utcnow()
                msg = await message.channel.send(embed=embed)
            #################################################################
            elif "slowmode" in message.content:
                embed = discord.Embed(title="Command Help: slowmode", description="Command Number 212",
                                      color=message.author.color)
                embed.add_field(name='Bot:', value=Nellie, inline=True)
                embed.add_field(name='Command', value='slowmode *sec* *name*', inline=True)
                embed.add_field(name='Example:',
                                value='{}slowmode 3² #Neko Dev. Army³\n*² the seconds beetween the messages, *³The Name of the Chatroom in which you like set the slowmode.'.format(
                                    current), inline=False)
                embed.add_field(name='Description',
                                value='The Command **slowmode** allows you to set the slowmode for your Chatroom.',
                                inline=False)
                embed.add_field(name='Argument fields:',
                                value='__**sec**__:\nIn the field **sec** you put in, the difference time beetween two messages from the same user.\n\n__**name**__:\nIn the **name** field you put in, from which Chatroom you like set the slowmode.',
                                inline=False)
                embed.add_field(name='Required Permissions:',
                                value='__**Bot**__:\n-Manage Channels\n-Embed Links\n-Message send\n-Manage Messages\n-Message read\n\n__**Command Excecuter**__:\n-Need to be the Owner of the named Chatroom.',
                                inline=False)
                embed.set_thumbnail(url=url)
                embed.set_footer(text=support)
                embed.timestamp = datetime.utcnow()
                msg = await message.channel.send(embed=embed)
            #################################################################
            elif "openrooms" in message.content:
                embed = discord.Embed(title="Command Help: openrooms", description="Command Number 213",
                                      color=message.author.color)
                embed.add_field(name='Bot:', value=Nellie, inline=True)
                embed.add_field(name='Command', value='openrooms', inline=True)
                embed.add_field(name='Example:', value='{}openroom'.format(current), inline=False)
                embed.add_field(name='Description', value='The Command **openroom** shows you all Public Chatrooms.',
                                inline=False)
                embed.add_field(name='Argument fields:', value='No argument fields.', inline=False)
                embed.add_field(name='Required Permissions:',
                                value='__**Bot**__:\n-Embed Links\n-Message send\n-Message read\n\n__**Command Excecuter**__:\n-Send Messages\n-Read Messages',
                                inline=False)
                embed.set_thumbnail(url=url)
                embed.set_footer(text=support)
                embed.timestamp = datetime.utcnow()
                msg = await message.channel.send(embed=embed)
            #################################################################
            elif "roomsetup" in message.content:
                embed = discord.Embed(title="Command Help: roomsetup", description="Command Number 215",
                                      color=message.author.color)
                embed.add_field(name='Bot:', value=Nellie, inline=True)
                embed.add_field(name='Command', value='roomsetup *name*', inline=True)
                embed.add_field(name='Example:',
                                value='{}roomsetup #Neko Dev. Army³\n*³The name of the room which you like setup.'.format(
                                    current), inline=False)
                embed.add_field(name='Description',
                                value='The Command **roomsetup** starts a setup with your Chatroom.', inline=False)
                embed.add_field(name='Argument fields:',
                                value='__**name**__:\nIn the **name** field you put in, which Chatroom do you like setup.',
                                inline=False)
                embed.add_field(name='Required Permissions:',
                                value='__**Bot**__:\n-Embed Links\n-Message send\n-Message read\n\n__**Command Excecuter**__:\n-Need to be the Owner of the named Chatroom.',
                                inline=False)
                embed.set_thumbnail(url=url)
                embed.set_footer(text=support)
                embed.timestamp = datetime.utcnow()
                msg = await message.channel.send(embed=embed)


#################################################################


def setup(bot):
    bot.add_cog(nellie(bot))
