import time
from datetime import datetime

import aiohttp
import discord
from discord.ext import commands

from commands.nellie import current
from lib.general import prefix
from lib.room import name_check, function_room, is_public, is_owner

bot = commands.Bot(command_prefix='n!')

inv = "https://discord.com/api/oauth2/authorize?client_id=631149405965385759&permissions=537193520&redirect_uri=https%3A%2F%2Flucys-dungeon.de%2Fserver&scope=bot"

botcolor = 0x00ff06

bot.remove_command('help')


class cmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)

    @commands.command()
    async def support(self, ctx):
        if not ctx.author.bot:
            channel = self.bot.get_channel(780064329256271875)
            invitelinknew = await channel.create_invite(xkcd=True, max_age=600, reason="Support")
            embed = discord.Embed(color=ctx.author.color)
            embed.add_field(name="Support Server Invite Link",
                            value="[Do you need help? Click me!]({})".format(invitelinknew))
            embed.set_footer(text='Message was requested by {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            await ctx.channel.send(embed=embed)

    @commands.command()
    async def profile(self, ctx):
        if not ctx.author.bot:
            embed = discord.Embed(title="Nellie's Profile", color=ctx.author.color)
            embed.add_field(name="Age:", value="6 Years old", inline=True)
            embed.add_field(name="Height:", value="150cm", inline=True)
            embed.add_field(name="** **", value="** **", inline=False)
            embed.add_field(name="Hobby's:", value="- Chat with you\n"
                                                   "- Communicate with the Community\n"
                                                   "- Play with her Wool ball\n"
                                                   "- Drinking Tea", inline=False)
            embed.add_field(name="Tasks:", value="- The big Sister of Lucy, Lilli and Timmy\n"
                                                 "- Helps cooking\n"
                                                 "- Connects you with the Rest of the World\n"
                                                 "- Planning Birthday Party's.")
            embed.set_thumbnail(url="https://img.neko-dev.de/img/general/nellie.jpeg")
            embed.set_footer(icon_url=ctx.author.avatar_url, text="Nellie's Profile")
            await ctx.send(embed=embed)

    @commands.command()
    async def neko(self, ctx):
        """nekos\o/"""
        async with self.session.get("https://nekos.life/api/neko") as resp:
            nekos = await resp.json()

        embed = discord.Embed(colour=discord.Colour.blue())
        embed.set_image(url=nekos['neko'])
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        if ctx.author.bot is False:
            start = time.time()
            async with self.session.get("https://nekos.life/api/neko"):
                duration = time.time() - start
            start = time.time()
            async with self.session.get("https://discord.com"):
                duration2 = time.time() - start
            start = time.time()
            async with self.session.get("https://www.neko-dev.de"):
                duration3 = time.time() - start
            await ctx.send(
                'The Bot Latency is **{}** ms.\n'
                'The Ping to nekos.life is **{}** ms.\n'
                'The Ping to Discord is **{}** ms.\n'
                'The Ping to Neko Dev is **{}** ms.'.format(
                    round(self.bot.latency * 1000), round(duration * 1000), round(duration2 * 1000),
                    round(duration3 * 1000)))

    @commands.command()
    async def namecheck(self, ctx, *args: str):
        if ctx.author.bot is False:
            name = '_'.join(args)
            if name_check(name) is True:
                avi = "not avaible"
                avi_url = "https://img.neko-dev.de/img/global/uncheck.png"
            else:
                avi = "avaible"
                avi_url = "https://img.neko-dev.de/img/global/check.png"
            embed = discord.Embed(title="Chatroom name check:",
                                  description=f"This name is {avi}")
            embed.set_footer(icon_url=self.bot.user.avatar_url, text="Name request")
            embed.set_thumbnail(url=avi_url)
            await ctx.send(embed=embed)

    @commands.command()
    async def openrooms(self, ctx):
        if ctx.author.bot is False:
            name = ""
            liste = is_public()
            for i in liste:
                desc = function_room(i.replace(".json", ""), 'request', 'desc')
                print(desc)

                lang = function_room(i.replace(".json", ""), 'request', 'lang')
                print(lang)

                name += "__**Name:**__ {}\n" \
                        "__**Language:**__ {}\n" \
                        "__**Short Description:**__\n" \
                        "{}\n" \
                        "\n".format(
                    ''.join(i.replace(".json", "")), ''.join(lang), ''.join(desc))
            if name == "":
                opens = "Ops there are no Public Chatrooms this time."
            else:
                opens = name
            embed = discord.Embed(color=ctx.author.color)
            embed.add_field(name='Public Chatrooms:', value=opens, inline=False)
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.set_footer(text="Public Chatrooms", icon_url=ctx.guild.icon_url)
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)

    @commands.command()
    async def roominfo(self, ctx, *args: str):
        if ctx.author.bot is False:
            mods = ""
            name = '_'.join(args)
            if name == "":
                name = is_owner(ctx.author.id)
                if not name:
                    await ctx.send(
                        "Please try again and write the name of the Chatgroup from that you like get infos.\
                        nHow to use roominfo 101:\n"
                        "``{}roominfo name``".format(prefix(str(ctx.guild.id))))
                    return
            if name_check(name):
                topic = function_room(name, 'request', 'topic')
                lang = function_room(name, 'request', 'lang')
                desc = function_room(name, 'request', 'desc')
                oid = str(function_room(name, 'request', 'owner'))
                channel = function_room(name, 'request', 'cid')
                for y in function_room(name, 'request', 'mods'):
                    user = self.bot.get_user(y)
                    if user:
                        mods += "{} | {}\n".format(user.name, user.id)
                    else:
                        mods += "{}\n".format(user)
                if channel is []:
                    embed = discord.Embed(title="Room Info", description="Here are your requested infos:",
                                          color=ctx.author.color)
                    embed.add_field(name='Name:', value='{}'.format(name), inline=False)
                    embed.add_field(name='Owner:', value='{}'.format(oid), inline=False)
                    embed.add_field(name='Topic:', value='{}'.format(topic), inline=False)
                    embed.add_field(name='Language:', value='{}'.format(lang), inline=False)
                    embed.add_field(name='Description:', value='{}'.format(desc), inline=False)
                    if not mods:
                        embed.add_field(name='Moderators:', value='Bully´s Playground (Not moderated)',
                                        inline=False)
                    else:
                        embed.add_field(name='Moderators:', value='{}'.format(mods), inline=False)
                    embed.add_field(name='Connected Server:',
                                    value="No activ linked Channels.\n"
                                          "As Roomowner you can use:\n"
                                          "**{}add *channelid* *{}***\n"
                                          "to add channels to this Room\n"
                                          "or delete it with:\n"
                                          "**nl!delroom *{}***".format(
                                        name, name, prefix(str(ctx.guild.id))), inline=False)
                    embed.set_thumbnail(url=ctx.guild.icon_url)
                    embed.set_footer(text=ctx.guild.name, icon_url=ctx.author.avatar_url)
                    embed.timestamp = datetime.utcnow()
                    await ctx.send(embed=embed)
                else:
                    if not mods:
                        embed = discord.Embed(title="Room Info", description="Here are your requested infos:",
                                              color=ctx.author.color)
                        embed.add_field(name='Name:', value='{}'.format(name), inline=False)
                        embed.add_field(name='Owner:', value='{}'.format(oid), inline=False)
                        embed.add_field(name='Topic:', value='{}'.format(topic), inline=False)
                        embed.add_field(name='Language:', value='{}'.format(lang), inline=False)
                        embed.add_field(name='Description:', value='{}'.format(desc), inline=False)
                        embed.add_field(name='Moderators:', value='Bully´s Playground (Not moderated)',
                                        inline=False)
                        embed.add_field(name="Connected Channels:", value=str(len(channel)), inline=False)
                        await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(title="Room Info", description="Here are your requested infos:",
                                              color=ctx.author.color)
                        embed.add_field(name='Name:', value='{}'.format(name), inline=False)
                        embed.add_field(name='Owner:', value='{}'.format(oid), inline=False)
                        embed.add_field(name='Topic:', value='{}'.format(topic), inline=False)
                        embed.add_field(name='Language:', value='{}'.format(lang), inline=False)
                        embed.add_field(name='Description:', value='{}'.format(desc), inline=False)
                        embed.add_field(name='Moderators:', value='{}'.format(mods), inline=False)
                        embed.add_field(name="Connected Channels:", value=str(len(channel)), inline=False)
                        await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Oh, i am sorry.",
                                      description="Your written Group is not found",
                                      color=ctx.author.color)
                embed.add_field(name='A Chatgroup with this name not exist',
                                value='Please check the spelling and try it again', inline=False)
                embed.set_thumbnail(url=self.bot.user.avatar_url)
                embed.set_footer(text=ctx.guild.name, icon_url=ctx.author.avatar_url)
                embed.timestamp = datetime.utcnow()
                await ctx.send(embed=embed)

    @bot.command()
    async def invite(self, ctx):
        if not ctx.author.bot:
            embed = discord.Embed(color=ctx.author.color)
            embed.add_field(name="{} Invite link".format(self.bot.user.name),
                            value="[Do you like invite me? Click here!]({})".format(inv))
            embed.set_footer(text=f'Do you need help? {current}support', icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(cmd(bot))
