import os
import sys
import time
from datetime import datetime

import discord
from discord.ext import commands

from lib.general import get_token
from lib.ranks import mod_right_here
from lib.room import is_connected, function_users, function_room, function_blacklist, function_pic, function_roles_room

os.chdir(r'/')


async def send_channel(channel, embed):
    await channel.send(embed=embed)


class ChatClass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if not message.author.bot:
                cid = is_connected(message.channel.id, 'cid')
                if cid:
                    await self.sending(message, cid)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

    async def sending(self, message, cid):
        token = get_token(12)
        server = message.guild
        msg = message.content
        uid = str(message.author.id)
        name = message.author.name + "#" + message.author.discriminator
        avatar = message.author.avatar_url
        color = message.author.color
        savatar = message.guild.icon_url
        invite = "https://lucys-dungeon.de/server"
        vote = "https://top.gg/bot/631149405965385759/vote"
        website = "https://lucys-dungeon.de/nellie"
        try:
            data = {}
            channels = function_room(cid, 'request', 'cid')
            ownerid = str(function_room(cid, 'request', 'owner'))
            spam = int(function_room(cid, 'request', 'spam'))
            banned = function_room(cid, 'request', 'banned')
            pictures = function_room(cid, 'request', 'pictures')
            user_time = function_users(cid, 'request', uid, 'time')
            try:
                t = round(time.time() - float(user_time))
            except TypeError:
                t = spam
            has_a_rank = function_users(cid, 'request', str(uid), 'roles')
            if function_blacklist(cid, 'request', message.content):
                try:
                    await message.delete()
                except PermissionError:
                    pass
                embed = discord.Embed(title='🚫System Alert🚫',
                                      description="Hello {},\n"
                                                  "A word in your message is blocked from the Chatroom chat.\n"
                                                  "Your message is not send".format(
                                          message.author.mention), color=0xff0000)
                embed.timestamp = datetime.utcnow()
                embed.set_footer(text=message.author.id, icon_url=message.guild.icon_url)
                await message.channel.send(embed=embed)
            else:
                if not mod_right_here(cid, uid):
                    if int(uid) in banned:
                        try:
                            await message.delete()
                        except PermissionError:
                            pass
                        embed = discord.Embed(title='🚫You are banned🚫',
                                              description="Hello {},\n"
                                                          "You are banned out of this Chatroom.".format(
                                                  message.author.mention),
                                              color=0xff0000)
                        embed.timestamp = datetime.utcnow()
                        embed.set_footer(text=uid,
                                         icon_url=self.bot.user.avatar_url)
                        await message.channel.send(embed=embed)
                        return
                    elif round(t) < spam:
                        try:
                            await message.delete()
                        except PermissionError:
                            pass
                        embed = discord.Embed(title='🚫Spam Alert🚫',
                                              description="Hello {},\n"
                                                          "Please be gentle and calm down with your message"
                                                          "speed.".format(
                                                  message.author.mention), color=0xff0000)
                        embed.timestamp = datetime.utcnow()
                        embed.set_footer(text=uid, icon_url=self.bot.user.avatar_url)
                        await message.channel.send(embed=embed)
                        return
                if len(message.attachments) != 0:
                    if pictures:
                        ends = [".jpg", ".jpeg", ".jfif", ".png", ".gif", ".mp4", ".m4v", ".mov",
                                ".mp3"]
                        for pic in message.attachments:
                            for end in ends:
                                if pic.filename.endswith(end):
                                    embed = discord.Embed(title='{} | {}'.format(server, name),
                                                          description=message.content,
                                                          color=color)
                                    embed.set_image(url=pic.url)
                                    embed.timestamp = datetime.utcnow()
                                    embed.set_footer(text="{} | {}\n".format(uid, token), icon_url=savatar)
                    else:
                        await message.channel.send(
                            "Ops, the Room Owner has disabled to send Pictures in this Chat.",
                            delete_after=10)
                        return
                elif str(uid) == '474947907913515019':
                    embed = discord.Embed(title='🛠 Developer | {} 🛠'.format(name),
                                          description="\n"
                                                      "{0}\n"
                                                      "\n"
                                                      "[Support]({1}) | [Website]({2}) | [Vote]({3})"
                                          .format(msg, invite, website, vote),
                                          color=color)
                    embed.timestamp = datetime.utcnow()
                    embed.set_footer(text=server, icon_url=savatar)
                    embed.set_thumbnail(url=avatar)
                elif str(uid) == str(ownerid):
                    embed = discord.Embed(title='📛 RoomOwner | {} 📛'.format(name),
                                          description="\n"
                                                      "{0}\n"
                                                      "\n"
                                                      "[Support]({1}) | [Website]({2}) | [Vote]({3})"
                                          .format(msg, invite, website, vote),
                                          color=color)
                    embed.timestamp = datetime.utcnow()
                    embed.set_footer(text=server, icon_url=savatar)
                    embed.set_thumbnail(url=avatar)
                elif mod_right_here(cid, uid):
                    embed = discord.Embed(title='🛡 Moderator | {} 🛡'.format(name),
                                          description="\n"
                                                      "{0}\n"
                                                      "\n"
                                                      "[Support]({1}) | [Website]({2}) | [Vote]({3})"
                                          .format(msg, invite, website, vote),
                                          color=color)
                    embed.timestamp = datetime.utcnow()
                    embed.set_footer(text=server, icon_url=savatar)
                    embed.set_thumbnail(url=avatar)
                elif has_a_rank:
                    role_info = function_roles_room(cid, 'request', has_a_rank)
                    if role_info:
                        in_put_in = f"[Vote]({vote})"
                        embed = discord.Embed(title=f"📧 {has_a_rank} | {name} 📧",
                                              description="\n"
                                                          "{0}\n"
                                                          "\n"
                                                          "[Support]({1}) | [Website]({2}) | {3}"
                                              .format(msg, invite, website, in_put_in),
                                              color=message.author.color)
                        embed.timestamp = datetime.utcnow()
                        embed.set_footer(text=uid, icon_url=savatar)
                        embed.set_thumbnail(url=avatar)
                    else:
                        embed = discord.Embed(title='{0} | {1}'.format(server, name),
                                              description="\n"
                                                          "{0}\n"
                                                          "\n"
                                                          "[Support]({1}) | [Website]({2}) | [Vote]({3})"
                                              .format(msg, invite, website, vote), color=color)
                        embed.timestamp = datetime.utcnow()
                        embed.set_footer(text=uid, icon_url=savatar)
                        embed.set_thumbnail(url=avatar)
                else:
                    embed = discord.Embed(title='{0} | {1}'.format(server, name),
                                          description="\n"
                                                      "{0}\n"
                                                      "\n"
                                                      "[Support]({1}) | [Website]({2}) | [Vote]({3})"
                                          .format(msg, invite, website, vote), color=color)
                    embed.timestamp = datetime.utcnow()
                    embed.set_footer(text=uid, icon_url=savatar)
                    embed.set_thumbnail(url=avatar)
                function_users(cid, 'set_time', uid)
                start = time.time()
                if len(message.attachments) == 0:
                    channels.remove(message.channel.id)
                for i in channels:
                    channel = self.bot.get_channel(i)
                    if channel:
                        try:
                            if len(message.attachments) != 0:
                                if pictures:
                                    try:
                                        await send_channel(channel, embed)
                                        data[str(i)] = str(msg.id)
                                    except Exception as e:
                                        pass
                            else:
                                try:
                                    await send_channel(channel, embed)
                                except Exception as e:
                                    print(e)
                        except Exception as e:
                            exc_type, exc_obj, exc_tb = sys.exc_info()
                            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                            print(exc_type, fname, exc_tb.tb_lineno)
                t2 = round(time.time() - start)
                if len(message.attachments) != 0:
                    await message.delete()
                else:
                    emote = "✅"
                    await message.add_reaction(emote)
                if data:
                    function_pic(cid, 'add', token, int(uid), time.time(), data)
                print("[SENDING] {}, {}, Time: {}".format(message.author, t, t2))

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)


def setup(bot):
    bot.add_cog(ChatClass(bot))
