import asyncio
from datetime import datetime

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='n!')

botcolor = 0xffffff

bot.remove_command('help')


class BotOwner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    @commands.is_owner()
    async def remoteleave(self, ctx, id: int):
        if ctx.author.bot is False:
            server = self.bot.get_guild(id)
            await ctx.message.delete()
            await ctx.channel.send("I leave the server {0}".format(server.name))
            await server.leave()

    @bot.command()
    @commands.is_owner()
    async def findserver(self, ctx, serverID: int):
        if ctx.author.bot is False:
            server = self.bot.get_guild(serverID)
            gen = discord.utils.get(server.text_channels, name="general")
            if gen:
                try:
                    server = self.bot.get_server(serverID)
                    channel = discord.utils.get(server.text_channels, name="general")
                    invitelinknew = await channel.create_invite(xkcd=True, max_uses=100)
                    embed = discord.Embed(
                        color=ctx.author.color)
                    embed.add_field(name='__Server Stats__', value='** **', inline=False)
                    embed.add_field(name='Servername:', value='{0.name}'.format(server), inline=True)
                    embed.add_field(name='Server ID:', value='{}'.format(server.id), inline=True)
                    embed.add_field(name='Membercount:', value='{0.member_count} members'.format(server),
                                    inline=False)
                    embed.add_field(name='Serverowner:', value='{}'.format(server.owner.mention), inline=False)
                    embed.add_field(name='Created at:', value='{}'.format(server.created_at))
                    embed.add_field(name="Discord Invite Link", value=invitelinknew)
                    embed.set_thumbnail(url=server.icon_url)
                    author = ctx.author
                    embed.set_footer(text='Message was requested by {}'.format(author))
                    embed.timestamp = datetime.utcnow()
                    await ctx.channel.send(embed=embed)
                except PermissionError:
                    server = self.bot.get_guild(serverID)
                    embed = discord.Embed(
                        color=ctx.author.color)
                    embed.add_field(name='__Server Stats__', value='** **', inline=False)
                    embed.add_field(name='Servername:', value='{0.name}'.format(server), inline=True)
                    embed.add_field(name='Server ID:', value='{}'.format(server.id), inline=True)
                    embed.add_field(name='Membercount:', value='{0.member_count} members'.format(server),
                                    inline=False)
                    embed.add_field(name='Serverowner:', value='{}'.format(server.owner.mention), inline=False)
                    embed.add_field(name='Created at:', value='{}'.format(server.created_at))
                    embed.set_thumbnail(url=server.icon_url)
                    author = ctx.message.author
                    embed.set_footer(text='Message was requested by {}'.format(author))
                    embed.timestamp = datetime.utcnow()
                    await ctx.channel.send(embed=embed)
            else:
                server = self.bot.get_guild(serverID)
                embed = discord.Embed(
                    color=ctx.author.color)
                embed.add_field(name='__Server Stats__', value='** **', inline=False)
                embed.add_field(name='Servername:', value='{0.name}'.format(server), inline=True)
                embed.add_field(name='Server ID:', value='{}'.format(server.id), inline=True)
                embed.add_field(name='Membercount:', value='{0.member_count} members'.format(server), inline=False)
                embed.add_field(name='Serverowner:', value='{}'.format(server.owner.mention), inline=False)
                embed.add_field(name='Created at:', value='{}'.format(server.created_at))
                embed.set_thumbnail(url=server.icon_url)
                author = ctx.message.author
                embed.set_footer(text='Message was requested by {}'.format(author))
                embed.timestamp = datetime.utcnow()
                await ctx.channel.send(embed=embed)

    @bot.command()
    @commands.is_owner()
    async def getinvite(self, ctx, id: int):
        if not ctx.author.bot:
            server = self.bot.get_guild(id)
            inv = await server.invites()
            for invites in inv:
                embed = discord.Embed(title="Invite Info", description="", color=ctx.author.color)
                embed.add_field(name="Creator:", value=invites.inviter, inline=True)
                embed.add_field(name="Channel:", value=invites.channel.mention, inline=True)
                embed.add_field(name="Uses", value=invites.uses, inline=False)
                embed.add_field(name="Invite", value=invites, inline=False)
                embed.set_thumbnail(url=server.icon_url)
                embed.timestamp = datetime.utcnow()
                msg = await ctx.channel.send(embed=embed)
                await msg.add_reaction("🆗")
                await msg.add_reaction("❌")
                await asyncio.sleep(0.5)

                def pred(m):
                    return m.author is ctx.message.author and m.channel is ctx.message.channel

                await self.bot.wait_for('n', check=pred)

    @bot.command()
    @commands.is_owner()
    async def servers(self, ctx):
        s = ""
        for server in self.bot.guilds:
            s += "{} | {}\n".format(server, server.id)
        embed = discord.Embed(title="Bot Servers", description=s)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(BotOwner(bot))
