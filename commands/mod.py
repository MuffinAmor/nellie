import os
import sys
from datetime import datetime

import discord
from discord.ext import commands

from lib.general import prefix
from lib.ranks import mod_right_here
from lib.room import function_blacklist, function_room, function_pic, is_connected


class RoomMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add_rank(self, ctx, user: discord.User):
        if not ctx.author.bot:
            pass

    @commands.command()
    async def remove_rank(self, ctx, user: discord.User):
        if not ctx.author.bot:
            pass

    @commands.command()
    async def slowmode(self, ctx, number: int, *args: str):
        if not ctx.author.bot:
            try:
                name = '_'.join(args)
                current = prefix(str(ctx.author.guild.id))
                is_mod = mod_right_here(name, str(ctx.author.id))
                if not number:
                    await ctx.send("Heyo, you need insert the amount of seconds for the slowmode.\n"
                                   "How to use slowmode 101:\n"
                                   "`{}slowmode 3²\n"
                                   "*² the seconds beetween the messages".format(current))
                    return
                try:
                    int(number)
                except TypeError:
                    await ctx.send("Heyo, you need insert the amount of seconds for the slowmode.\n"
                                   "How to use slowmode 101:\n"
                                   "`{}slowmode 3²\n"
                                   "*² the seconds beetween the messages".format(current))
                    return
                if not is_mod:
                    await ctx.send("It seems that you are not a moderator of this Chatroom.")
                else:
                    sek = int(number)
                    function_room(name, 'edit', 'spam', sek)
                    await ctx.send("The slowmode from **{}** has been setted to **{}** seconds.".format(name, sek))
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno, e)

    @commands.command()
    async def addword(self, ctx, *args: str):
        if not ctx.author.bot:
            current = prefix(str(ctx.author.guild.id))
            InputContent = ' '.join(args)
            AuthorId = str(ctx.author.id)
            if InputContent:
                argsword, argsroom = InputContent.split(", ")
                word = ''.join(argsword)
                room = ''.join(argsroom)
                if not word or not room:
                    await ctx.send("Please provide the Word and the Chatroomname.\n"
                                   "How to use addword 101:\n"
                                   "`{}addword EvilBot², #Neko Dev. Army³\n"
                                   "*² the Word that you would like add to the Blacklist,\n"
                                   "*³ the name of the Chatroom.".format(current))
                elif not mod_right_here(room, AuthorId):
                    await ctx.send("Ops, you are not a Moderator of this Chatroom.")
                else:
                    await ctx.send(function_blacklist(room, 'add', word))
            else:
                await ctx.send("Please provide the Word and the Chatroomname.\n"
                               "How to use addword 101:\n"
                               "`{}addword EvilBot² #Neko Dev. Army³\n"
                               "*² the Word that you would like add to the Blacklist,\n"
                               "*³ the name of the Chatroom.".format(current))

    @commands.command()
    async def removeword(self, ctx, *args: str):
        if not ctx.author.bot:
            current = prefix(str(ctx.author.guild.id))
            InputContent = ' '.join(args)
            AuthorId = str(ctx.author.id)
            if InputContent:
                argsword, argsroom = InputContent.split(", ")
                word = ''.join(argsword)
                room = ''.join(argsroom)
                if not word or not room:
                    await ctx.send("Please provide the Word and the Chatroomname.\n"
                                   "How to use removeword 101:\n"
                                   "`{}addword EvilBot², #Neko Dev. Army³\n"
                                   "*² the Word that you would like remove from the Blacklist,\n"
                                   "*³ the name of the Chatroom.".format(current))
                elif not mod_right_here(room, AuthorId):
                    await ctx.send("Ops, you are not a Moderator of this Chatroom.")
                else:
                    await ctx.send(function_blacklist(room, 'remove', word))
            else:
                await ctx.send("Please provide the Word and the Chatroomname.\n"
                               "How to use removeword 101:\n"
                               "`{}addword EvilBot², #Neko Dev. Army³\n"
                               "*² the Word that you would like remove from the Blacklist,\n"
                               "*³ the name of the Chatroom.".format(current))

    @commands.command()
    async def blacklist(self, ctx, *args: str):
        if not ctx.author.bot:
            room = ' '.join(args)
            AuthorId = str(ctx.author.id)
            if not room:
                await ctx.send("Please provide the Chatroom.")
            elif not mod_right_here(room, AuthorId):
                await ctx.send("Ops, you are not a Moderator of this Chatroom.")
            else:
                liste = function_room(room, 'request', 'blacklist')
                BlackList = ""
                for i in liste:
                    BlackList += "{}\n".format(i)
                embed = discord.Embed(title="Wordblacklist", description=BlackList, color=ctx.author.color)
                embed.timestamp = datetime.utcnow()
                embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                embed.set_thumbnail(url=self.bot.user.avatar_url)
                try:
                    await ctx.author.send(embed=embed)
                    await ctx.send("You have recieve a mail")
                except PermissionError:
                    await ctx.send(
                        "Ops, it looks like you have close your Direct messages.\n"
                        "Please open it, to recieve the List")

    @commands.command()
    async def ban(self, ctx, number: int, *args: str):
        if not ctx.author.bot:
            current = prefix(str(ctx.author.guild.id))
            name = '_'.join(args)
            banned = function_room(name, 'request', 'banned')
            AuthorId = ctx.author.id
            try:
                if not number:
                    await ctx.send("Ops please insert the id of the User that would you like ban.\n"
                                   "How to use ban 101:\n"
                                   "`{}ban 474947907913515019² #Neko Dev. Army³\n"
                                   "*²the ID of the User that you would ban,\n"
                                   "*³The Name of the Chatroom from which you like ban the User.`".format(current))
                    return
                try:
                    int(number)
                except TypeError:
                    await ctx.send("Ops please insert the id of the User that would you like ban.\n"
                                   "How to use ban 101:\n"
                                   "`{}ban 474947907913515019² #Neko Dev. Army³\n"
                                   "*²the ID of the User that you would ban,\n"
                                   "*³The Name of the Chatroom from which you like ban the User.`".format(current))
                    return
                if not number:
                    await ctx.send("Ops, please choose a user that you like ban from the Chatgroup.\n"
                                   "How to use ban 101:\n"
                                   "`{}ban 474947907913515019² #Neko Dev. Army³\n"
                                   "*²the ID of the User that you would ban,\n"
                                   "*³The Name of the Chatroom from which you like ban the User.`".format(current))
                    return
                elif name == "":
                    await ctx.send("Please try again and write a valid Groupname in that you like ban a user.\n"
                                   "How to use ban 101:\n"
                                   "`{}ban 474947907913515019² #Neko Dev. Army³\n"
                                   "*² the ID of the User that you would ban,\n"
                                   "*³The Name of the Chatroom from which you like ban the User.`".format(current))
                elif not mod_right_here(name, AuthorId):
                    await ctx.send("You are not a Moderator of this Chatgroup")
                elif int(number) in banned:
                    await ctx.send("This Person is banned already.")
                else:
                    function_room(name, 'append_ban', number)
                    await ctx.send("{} has been banned.".format(number))
            except Exception as error:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno, error)

    @commands.command()
    async def unban(self, ctx, number = None, *args: str):
        if not ctx.author.bot:
            current = prefix(str(ctx.author.guild.id))
            name = '_'.join(args)
            banned = function_room(name, 'request', 'banned')
            AuthorId = str(ctx.author.id)
            if number is None:
                await ctx.send("Ops, please choose a user that you like unban from the Chatgroup.\n"
                               "How to use unban 101:\n"
                               "`{}unban 474947907913515019² #Neko Dev. Army³\n"
                               "*² the ID of the User that you would unban.\n"
                               "*³The Name of the Chatroom from which you like unban the User.`".format(current))
                return
            try:
                int(number)
            except TypeError:
                await ctx.send("Ops, please choose a user that you like unban from the Chatgroup.\n"
                               "How to use unban 101:\n"
                               "`{}unban 474947907913515019² #Neko Dev. Army³\n"
                               "*² the ID of the User that you would unban.\n"
                               "*³The Name of the Chatroom from which you like unban the User.`".format(current))
            if name == "":
                await ctx.send("Please try again and write a valid Groupname in that you like unban a user.\n"
                               "How to use unban 101:\n"
                               "`{}unban 474947907913515019² #Neko Dev. Army³\n"
                               "*² the ID of the User that you would unban.\n"
                               "*³The Name of the Chatroom from which you like unban the User.`".format(current))
                return
            elif not mod_right_here(name, AuthorId):
                await ctx.send("Ops, you are not a Moderator of this Chatroom.")
            elif int(number) not in banned:
                await ctx.send("This Person is not banned.")
            else:
                function_room(name, 'remove_ban', number)
                await ctx.send("{} has been unbanned.".format(number))

    @commands.command()
    async def del_pic(self, ctx, *args):
        if not ctx.author.bot:
            try:
                token = ' '.join(args)

                AuthorId = str(ctx.author.id)
                emote = self.bot.get_emoji(746375196486664303)
                msg = await ctx.send("{} Deleting in process...".format(emote))
                if token == "":
                    await msg.edit("Please insert the Picture Token, which you can find under the Picture.")
                else:
                    room = is_connected(token, 'pics')
                    if room is False:
                        await msg.edit("Ops, invalid Token")
                    else:
                        msgs = function_pic(room, 'request', token)['channel']
                        if not mod_right_here(room, AuthorId):
                            await msg.edit(content="Ops, you are not a Moderator of this Chatroom.")
                        elif msgs:
                            for i in msgs:
                                print(i)
                                channel = self.bot.get_channel(int(i))
                                if channel:
                                    message = await channel.fetch_message(msgs[i])
                                    if message:
                                        try:
                                            embed = discord.Embed(title="System Overwrite")
                                            embed.set_image(url="https://img.neko-dev.de/img/global/deleted.jpg")
                                            embed.timestamp = datetime.utcnow()
                                            await message.edit(embed=embed)
                                        except PermissionError:
                                            await ctx.send(
                                                "I can't overwrite the Picture in {} .".format(channel.name))
                                            pass
                                    else:
                                        await ctx.send(
                                            "I can't overwrite the Picture in {} .".format(channel.name))
                                else:
                                    await ctx.send(
                                        "I can't overwrite the Picture in {} .".format(channel.name))
                            function_pic(room, 'delete', token)
                            await msg.edit(
                                content="The Picture with the Token {} has been overwrited sucessfully".format(token))
                        else:
                            await msg.edit(content="A Picture with this Token is not found.")
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)

    @commands.command()
    async def list_banned(self, ctx, *args):
        if not ctx.author.bot:
            room = ' '.join(args)
            banned = function_room(room, 'request', 'banned')
            AuthorId = str(ctx.author.id)
            emote = self.bot.get_emoji(709414815130452028)
            msg = await ctx.send("{} In Process...".format(emote))
            if not mod_right_here(room, AuthorId):
                await msg.edit(content="Ops, you are not a Moderator of this Chatroom.")
            else:
                ban_list = ""
                for i in banned:
                    member = self.bot.get_user(int(i))
                    if member:
                        ban_list += "{} | {}\n".format(member.name, i)
                    else:
                        ban_list += "{}\n".format(i)
                embed = discord.Embed(title="Ban List", description=ban_list, color=ctx.author.color)
                embed.timestamp = datetime.utcnow()
                embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                embed.set_thumbnail(url=self.bot.user.avatar_url)
                try:
                    await ctx.author.send(embed=embed)
                    await msg.edit(content="You have recieve a mail")
                except PermissionError:
                    await ctx.send(
                        "Ops, it looks like you have close your Direct messages.\n"
                        "Please open it, to recieve the List")


def setup(bot):
    bot.add_cog(RoomMod(bot))
