import os
import sys
from datetime import datetime

import discord
from discord.ext import commands

from lib.general import prefix
from lib.pics import request_pic_msg, remove_pic, request_pic_room
from lib.ranks import mod_right_here
from lib.room_wb import add_word_to_room, remove_word_to_room, room_blacklist
from lib.set_room import edit_banned, get_info

bot = commands.Bot(command_prefix='nl!')

botcolor = 0x00ff06

bot.remove_command('help')


class RoomMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def addword(self, ctx, *args: str):
        if ctx.message.author.bot is False:
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
                    await ctx.send(add_word_to_room(room, word))
            else:
                await ctx.send("Please provide the Word and the Chatroomname.\n"
                               "How to use addword 101:\n"
                               "`{}addword EvilBot² #Neko Dev. Army³\n"
                               "*² the Word that you would like add to the Blacklist,\n"
                               "*³ the name of the Chatroom.".format(current))

    @commands.command()
    async def removeword(self, ctx, *args: str):
        if ctx.message.author.bot is False:
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
                    await ctx.send(remove_word_to_room(room, word))
            else:
                await ctx.send("Please provide the Word and the Chatroomname.\n"
                               "How to use removeword 101:\n"
                               "`{}addword EvilBot², #Neko Dev. Army³\n"
                               "*² the Word that you would like remove from the Blacklist,\n"
                               "*³ the name of the Chatroom.".format(current))

    @commands.command()
    async def blacklist(self, ctx, *args: str):
        if ctx.message.author.bot is False:
            room = ' '.join(args)
            AuthorId = str(ctx.author.id)
            if not room:
                await ctx.send("Please provide the Chatroom.")
            elif not mod_right_here(room, AuthorId):
                await ctx.send("Ops, you are not a Moderator of this Chatroom.")
            else:
                liste = room_blacklist(room)
                BlackList = ""
                for i in liste:
                    BlackList += "{}\n".format(i)
                embed = discord.Embed(title="Wordblacklist", description=BlackList, color=botcolor)
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
        if not ctx.message.author.bot:
            current = prefix(str(ctx.author.guild.id))
            name = ' '.join(args)
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
                else:
                    edit_banned(name, int(number), 'append')
                    await ctx.send("{} has been banned.".format(number))
            except Exception as error:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno, error)

    @commands.command()
    async def unban(self, ctx, number = None, *args: str):
        if not ctx.message.author.bot:
            current = prefix(str(ctx.author.guild.id))
            name = ' '.join(args)
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
            else:
                edit_banned(name, int(number), 'remove')
                await ctx.send("{} has been unbanned.".format(number))

    @commands.command()
    async def del_pic(self, ctx, *args):
        token = ' '.join(args)
        msgs = request_pic_msg(token)
        room = request_pic_room(token)
        AuthorId = str(ctx.author.id)
        emote = self.bot.get_emoji(709414815130452028)
        msg = await ctx.send("{} Deleting in process...".format(emote))
        if not mod_right_here(room, AuthorId):
            await msg.edit(content="Ops, you are not a Moderator of this Chatroom.")
        elif token == "":
            await msg.edit("Please insert the Picture Token, which you can find under the Picture.")
        elif msgs:
            for i in msgs:
                channel = self.bot.get_channel(int(i))
                if channel:
                    message = await channel.fetch_message(msgs[i])
                    if message:
                        try:
                            await message.delete()
                        except PermissionError:
                            await ctx.send(
                                "I can't delete the Picture in {} .".format(channel.name))
                            pass
                    else:
                        await ctx.send(
                            "I can't delete the Picture in {} .".format(channel.name))
                else:
                    await ctx.send(
                        "I can't delete the Picture in {} .".format(channel.name))
            remove_pic(token)
            await msg.edit(content="The Picture with the Token {} has been deleted sucessfully".format(token))
        else:
            await msg.edit(content="A Picture with this Token is not found.")

    @commands.command()
    async def list_banned(self, ctx, *args):
        room = ' '.join(args)
        banned = get_info(room, "banned")
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
            embed = discord.Embed(title="Ban List", description=ban_list, color=botcolor)
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
