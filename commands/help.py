from datetime import datetime

import discord
from discord.ext import commands

from lib.general import prefix

bot = commands.Bot(command_prefix='n!!')

botcolor = 0x00ff06

bot.remove_command('help')

url = 'https://img.neko-dev.de/img/general/Neko_Logo.png'


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            if "<@631149405965385759>" == message.content:
                current = prefix(str(message.guild.id))
                await message.channel.send("My Prefix on this Server is **{}**".format(current))
                return
            elif "<@!631149405965385759>" == message.content:
                current = prefix(str(message.guild.id))
                await message.channel.send("My Prefix on this Server is **{}**".format(current))
                return

    @bot.command()
    async def help(self, ctx):
        if not ctx.author.bot:
            embed = discord.Embed(title="Help Menu",
                                  description="[Commands](https://muffinamor.de/nellie/commands)\n"
                                              "[FAQ](https://muffinamor.de/nellie/FAQ)\n"
                                              "[About](https://muffinamor.de/nellie/about)",
                                  color=ctx.author.color)
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)

    '''@bot.command()
    async def help(self, ctx):
        if ctx.author.bot is False:
            id = str(ctx.author.id)
            data = get_news()
            current = prefix(str(ctx.author.guild.id))
            embed = discord.Embed(
                color=ctx.author.color)
            embed.set_author(name='Nellie Help Menu | Create your own Globalchat!')
            embed.add_field(name='❓', value='Open the Member Help Menu', inline=False)
            embed.add_field(name='📁', value='Open Server Admin Commands', inline=False)
            if roomowner(id):
                embed.add_field(name='🗡', value='Open Chatroom Owner Commands', inline=False)
            if roommod(id):
                embed.add_field(name='🛡', value='Open Chatroom Moderator Commands', inline=False)
            embed.add_field(name='🔙', value='Go back to this site', inline=False)
            embed.set_thumbnail(
                url=url)
            embed.set_footer(text='Do you need help? {}support'.format(current))
            embed.timestamp = datetime.utcnow()
            msg = await ctx.channel.send(embed=embed)
            await msg.add_reaction("❓")
            await msg.add_reaction("📁")
            if roomowner(id):
                await msg.add_reaction("🗡")
            if roommod(id):
                await msg.add_reaction("🛡")
            await msg.add_reaction("🔙")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        id = str(user.id)
        current = prefix(str(user.guild.id))
        data = get_news()
        if reaction.message.author.id is self.bot.user.id:
            if user.bot is False:
                if reaction.emoji == "❓":
                    embed = discord.Embed(
                        color=user.color)
                    embed.set_author(name='Nellie Help Menu | Create your own Globalchat!')
                    embed.add_field(name=f"{current}profile",
                                    value="Shows you the Bot's Profile", inline=False)
                    embed.add_field(name=f"{current}neko",
                                    value="Shows you a Neko Picture!", inline=False)
                    embed.add_field(name='{}namecheck *name*'.format(current),
                                    value='Check if the Groupname is avaible', inline=False)
                    embed.add_field(name='{}roominfo *name*'.format(current),
                                    value='Give you Infos about a Chatroom', inline=False)
                    embed.add_field(name='{}openrooms'.format(current),
                                    value='Shows you all current Public Chatrooms', inline=False)
                    embed.add_field(name='**🔙**', value='Go back to navigation site', inline=False)
                    embed.set_thumbnail(
                        url=url)
                    embed.set_footer(text='Do you need help? {}support'.format(current))
                    await reaction.message.edit(embed=embed)
                    await reaction.message.remove_reaction("❓", user)
                if reaction.emoji == "📁":
                    embed = discord.Embed(
                        color=user.color)
                    embed.set_author(name='Server Admin Help Menu | Create your own Globalchat!')
                    embed.add_field(name='{}prefix *new_prefix*'.format(current),
                                    value='Change the Botprefix for your Server.',
                                    inline=False)
                    embed.add_field(name='{}leave'.format(current), value='The Bot leave your server',
                                    inline=False)
                    embed.add_field(name='{}createroom *name*'.format(current),
                                    value='Create your Chatroom',
                                    inline=False)
                    embed.add_field(name='{}unlink *id*'.format(current),
                                    value='Link the ID Channel from the Chatroom you write', inline=False)
                    embed.add_field(name='{}*chatroom_name* *channel_id*'.format(current),
                                    value='Add the Channel to the Chatroom if the Room is set as Public.',
                                    inline=False)
                    embed.add_field(name='{}setglobal *channel*'.format(current),
                                    value='Set the Main GlobalChat in the Channel',
                                    inline=False)
                    embed.add_field(name='{}clearglobal *channel*'.format(current),
                                    value='Disable the Main GlobalChat in your Server',
                                    inline=False)
                    embed.timestamp = datetime.utcnow()
                    embed.add_field(name='🔙', value='Go back to navigation site', inline=False)
                    embed.set_thumbnail(
                        url=url)
                    embed.set_footer(text='Do you need help? {}support'.format(current))
                    await reaction.message.edit(embed=embed)
                    await reaction.message.remove_reaction("📁", user)
                if reaction.emoji == "🗡":
                    if roomowner(id):
                        embed = discord.Embed(
                            color=user.color)
                        embed.set_author(name='Chatroom Owner Commands | Create your own Globalchat!')
                        embed.add_field(name='{}owner_transfer *name*'.format(current),
                                        value='Transfer the Ownership of your Chatroom',
                                        inline=False)
                        embed.add_field(name='{}create_role *name*'.format(current),
                                        value='Create your own Globalchatrole',
                                        inline=False)
                        embed.add_field(name='{}delete_role *name*'.format(current),
                                        value='Delete a Globalchat Role.',
                                        inline=False)
                        embed.add_field(name='{}add_role *user* *role*'.format(current),
                                        value='Give the user a Customrole.',
                                        inline=False)
                        embed.add_field(name='{}remove_role *user*'.format(current),
                                        value='Remove the Customrole of the User.',
                                        inline=False)
                        embed.add_field(name='{}show_roles'.format(current),
                                        value='Shows your Customroles!',
                                        inline=False)
                        embed.add_field(name='{}delroom *name*'.format(current),
                                        value='Delete your Chatroom',
                                        inline=False)
                        embed.add_field(name='{}*name* *id*'.format(current),
                                        value='Add the Channel to the Chatroom', inline=False)
                        embed.add_field(name='{}add_mod *member* *name*'.format(current),
                                        value='Add a moderator to the Chatroom', inline=False)
                        embed.add_field(name='{}remove_mod *member* *name*'.format(current),
                                        value='Remove a moderator to the Chatroom', inline=False)
                        embed.add_field(name='{}show_mod *name*'.format(current),
                                        value='Shows the Moderators of the Chatroom', inline=False)
                        embed.add_field(name='{}roomsetup *name*'.format(current),
                                        value='Start a setup for your Room.', inline=False)
                        embed.add_field(name='🔙', value='Go back to navigation site', inline=False)
                        embed.set_thumbnail(
                            url=url)
                        embed.set_footer(text='Do you need help? {}support'.format(current))
                        await reaction.message.edit(embed=embed)
                        await reaction.message.remove_reaction("🗡", user)
                if reaction.emoji == "🛡":
                    if roommod(id):
                        embed = discord.Embed(
                            color=user.color)
                        embed.set_author(name='Chatroom Moderator Commands | Create your own Globalchat!')
                        embed.add_field(name='{}ban *id* *name*'.format(current),
                                        value='Ban a user out of this Chatroom', inline=False)
                        embed.add_field(name='{}unban *id* *name*'.format(current),
                                        value='Unban a user in this Chatroom', inline=False)
                        embed.add_field(name='{}del_pic *token*'.format(current),
                                        value='Delete a Picture out of all Chatroom Channels.', inline=False)
                        embed.add_field(name='{}addword *word*, *roomname*'.format(current),
                                        value='Add a Word to the Roomblacklist', inline=False)
                        embed.add_field(name='{}removeword *word*, *roomname*'.format(current),
                                        value='Remove a Word from the Rommblacklist', inline=False)
                        embed.add_field(name='{}blacklist *roomname*'.format(current),
                                        value='Sends you the Roomblacklist via Direct Message', inline=False)
                        embed.add_field(name='{}list_banned *roomname*'.format(current),
                                        value='Sends you the list of banned User via Direct Message', inline=False)
                        embed.add_field(name='{}slowmode *sec* *name*'.format(current),
                                        value='Set the slowmode for your Chatroom.', inline=False)
                        embed.add_field(name='🔙', value='Go back to navigation site', inline=False)
                        embed.set_thumbnail(
                            url=url)
                        embed.set_footer(text='Do you need help? {}support'.format(current))
                        await reaction.message.edit(embed=embed)
                        await reaction.message.remove_reaction("🛡", user)
                if reaction.emoji == "🔙":
                    embed = discord.Embed(
                        color=user.color)
                    embed.set_author(name='Nellie Help Menu | Create your own Globalchat!')
                    embed = discord.Embed(
                        color=user.color)
                    embed.set_author(name='Nellie Help Menu | Create your own Globalchat!')
                    embed.add_field(name='❓', value='Open the Member Help Menu', inline=False)
                    embed.add_field(name='📁', value='Open Server Admin Commands', inline=False)
                    if roomowner(id):
                        embed.add_field(name='🗡', value='Open Chatroom Owner Commands', inline=False)
                    if roommod(id):
                        embed.add_field(name='🛡', value='Open Chatroom Moderator Commands', inline=False)
                    embed.add_field(name='🔙', value='Go back to this site', inline=False)
                    embed.set_thumbnail(
                        url=url)
                    embed.set_footer(text='Do you need help? {}support'.format(current))
                    embed.timestamp = datetime.utcnow()
                    await reaction.message.edit(embed=embed)
                    await reaction.message.remove_reaction("🔙", user)'''


def setup(bot):
    bot.add_cog(help(bot))
