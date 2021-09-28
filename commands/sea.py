from datetime import datetime

import discord
from discord.ext import commands

from lib.general import prefix
from lib.ranks import roomowner
from lib.room import is_connected, name_check, function_room


class ServerAdmin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.allowed = False

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def createroom(self, ctx, *args: str):
        if ctx.message.author.bot is False:
            current = prefix(str(ctx.author.guild.id))
            name = '_'.join(args)
            user_id = str(ctx.author.id)
            if name == "":
                await ctx.send(
                    "Please try again and choose a fancy name for your Chatgroup.\nHow to use createroom 101:\n"
                    "`{}createroom #Neko Dev. Army³\n"
                    "*³Your choosen name.`".format(current))
            else:
                n = name_check(name)
                request_owner = roomowner(user_id)
                if request_owner is True:
                    embed = discord.Embed(title="I am sorry.",
                                          description="You already own a Chatroom. :eyes:",
                                          color=ctx.author.color)
                    embed.set_thumbnail(url=self.bot.user.avatar_url)
                    embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
                    embed.timestamp = datetime.utcnow()
                    await ctx.send(embed=embed)
                elif n:
                    embed = discord.Embed(title="I am sorry.", description="This Name is unavaible allready.",
                                          color=ctx.author.color)
                    embed.add_field(name='This Name is not avaible anymore.',
                                    value='Please choose a other name for your Chatgroup.', inline=False)
                    embed.set_thumbnail(url=self.bot.user.avatar_url)
                    embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
                    embed.timestamp = datetime.utcnow()
                    await ctx.send(embed=embed)
                elif str(name) in list(self.bot.all_commands):
                    await ctx.send("Is a Command")
                else:
                    function_room(name, 'create', int(user_id))
                    await ctx.send("Congrats to your Chatroom :D.")

    @commands.command()
    async def unlink(self, ctx, number: int):
        if ctx.message.author.bot is False:
            current = prefix(str(ctx.author.guild.id))

            if number is None:
                await ctx.send(
                    "Heyo, i see you have forgot to insert the "
                    "Channel Id with the channel do you like leave :eyes: ...\n"
                    "Please try again and insert one.\n"
                    "How to use unlink 101:\n"
                    "`{}unlink 636702313758851102² #Neko Dev. Army³\n"
                    "*² the ID of the Channel you like unlink,\n*³The Chatroom name.`".format(current))
                return
            try:
                int(number)
            except TypeError:
                await ctx.send(
                    "Heyo, i see you have forgot to insert the Channel"
                    " Id with the channel do you like leave :eyes: ...\n"
                    "Please try again and insert one.\n"
                    "How to use unlink 101:\n"
                    "`{}unlink 636702313758851102² #Neko Dev. Army³\n"
                    "*² the ID of the Channel you like unlink,\n"
                    "*³The Chatroom name.`".format(current))
                return

            else:
                if not len(str(number)) == 18:
                    await ctx.send(
                        "Heyo, i see you have forgot to insert"
                        " the channelid with the channel do you like leave :eyes: ...\n"
                        "Please try again and insert one.\n"
                        "How to use unlink 101:\n"
                        "`{}unlink 636702313758851102² #Neko Dev. Army³\n"
                        "*² the ID of the Channel you like unlink,\n"
                        "*³The Chatroom name.`".format(current))
                    return

                else:
                    name = is_connected(number, 'cid')
                    emote = self.bot.get_emoji(709414815130452028)
                    msg = await ctx.send(f"{emote} Please give me a moment, i will check something...")
                    if name is False or None:
                        await ctx.send("This Channel is not connected to a Chatroom.")

                    else:
                        owner = function_room(name, 'request', 'owner')

                        if ctx.author.id == 474947907913515019:
                            self.allowed = True
                        elif ctx.author.id == owner:
                            self.allowed = True
                        elif ctx.author.guild_permissions.administrator is True:
                            self.allowed = True

                    if self.allowed is True:
                        channel = self.bot.get_channel(number)
                        if channel and channel in ctx.guild.channels:
                            function_room(name, 'remove', number)
                            await msg.edit(content=f"The Channel {number} has been unlinked from {name}")
                        else:
                            embed = discord.Embed(title="I am sorry.",
                                                  description="This Channel is not on this Server or not even exist.",
                                                  color=ctx.author.color)
                            embed.set_thumbnail(url=self.bot.user.avatar_url)
                            embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
                            embed.timestamp = datetime.utcnow()
                            await msg.edit(embed=embed)

                    else:
                        await msg.edit(
                            content="Ohaa, it looks like you haven´t enough permissions to unlink to this Channel\n"
                                    "You need Administrator Permissions on all Channel Server that you like unlink. ^^")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setglobal(self, ctx, setchannel: discord.TextChannel = None):
        if ctx.message.author.bot is False:
            function_room('global', 'create', '474947907913515019')
            channel = setchannel or ctx.message.channel
            if is_connected(channel.id, 'cid'):
                embed = discord.Embed(title="I am sorry.",
                                      description="The Command channel is allready linked with a other Chat.",
                                      color=ctx.author.color)
                embed.add_field(name='This Channel is allready linked.',
                                value='You can´t set here the Globalchannel',
                                inline=False)
                embed.set_thumbnail(url=self.bot.user.avatar_url)
                embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.timestamp = datetime.utcnow()
                await ctx.send(embed=embed)
                return
            else:
                function_room('global', 'append', channel.id)
                topic = function_room('global', 'request', 'topic')
                try:
                    if topic is None:
                        await channel.edit(
                            topic="Chatgroup: {} | powered by: {}".format('global', self.bot.user.mention))
                    elif topic:
                        await channel.edit(topic="Chatgroup: {} | {}".format('global', topic))
                except PermissionError:
                    pass
                embed = discord.Embed(title="Welcome in the Global Network",
                                      description='The Channel {} has been set as Globalchat'.format(
                                          channel.mention),
                                      color=ctx.author.color)
                embed.add_field(name='Happy to chat with you', value='Hello and Welcome. Have a great time with us',
                                inline=False)
                embed.set_thumbnail(url=ctx.guild.icon_url)
                embed.set_footer(text=ctx.guild.id, icon_url=ctx.guild.icon_url)
                embed.timestamp = datetime.utcnow()
                await ctx.channel.send(embed=embed)
                return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clearglobal(self, ctx, setchannel: discord.TextChannel = None):
        if not ctx.message.author.bot:
            channel = setchannel or ctx.message.channel
            if is_connected(channel.id, 'cid'):
                function_room('global', 'remove', channel.id)
                await ctx.channel.send("The Globalchannel has been resetted")
            else:
                await ctx.channel.send("This channel is not set. Please choose another one.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def leave(self, ctx):
        if ctx.author.bot is False:
            await ctx.send("Imma get out!")
            await ctx.guild.leave()


def setup(bot):
    bot.add_cog(ServerAdmin(bot))
